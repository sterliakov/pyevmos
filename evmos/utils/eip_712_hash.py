"""Hashing utilities for EIP-712 messages.

Copied under the Apache 2.0 license from
https://github.com/ApeWorX/eip712/blob/main/eip712/hashing.py
with modification.

Modifications:

* Fixed type dependency finding (to consifer array types as well)
* Fix hashing application
  (hash structs always in encode_data, it was lost for user-defined structs arrays)
* Added typing
* Linted to current project needs
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping
from dataclasses import asdict
from itertools import groupby
from operator import itemgetter
from typing import Any, Sequence, TypedDict

from eth_abi import encode, is_encodable, is_encodable_type
from eth_abi.grammar import parse
from eth_utils import ValidationError, keccak, to_tuple, toolz
from typing_extensions import TypeAlias

from evmos.eip712 import EIPToSign


class _FieldT(TypedDict):
    name: str
    type: str  # noqa: A003


_TypesT: TypeAlias = Mapping[str, Sequence[_FieldT]]


def get_dependencies(primary_type: str, types: _TypesT) -> tuple[str, ...]:
    """Perform DFS to get all the dependencies of the `primary_type`."""
    deps = set()
    struct_names_yet_to_be_expanded = [primary_type]

    while len(struct_names_yet_to_be_expanded) > 0:
        struct_name = struct_names_yet_to_be_expanded.pop()

        deps.add(struct_name)
        fields = types[struct_name]
        for field in fields:
            type_, *_ = field['type'].partition('[')
            if type_ in types and type_ not in deps:
                # We don't need to expand types that are not user defined (customized)
                # also skip types that we have already encountered
                struct_names_yet_to_be_expanded.append(type_)

    # Don't need to make a struct as dependency of itself
    deps.remove(primary_type)
    # breakpoint()

    return tuple(deps)


def field_identifier(field: _FieldT) -> str:
    """Stringify a field in 'TYPE NAME' format."""
    return f'{field["type"]} {field["name"]}'


def encode_struct(struct_name: str, struct_field_types: Iterable[_FieldT]) -> str:
    """Stringify a single struct in 'NAME(type1 name1,type2 name2,...)' format."""
    return '{name}({args})'.format(
        name=struct_name,
        args=','.join(map(field_identifier, struct_field_types)),
    )


def encode_type(primary_type: str, types: _TypesT) -> str:
    """Encode type as concatenation of itself and all dependencies (alphabetical order).

    The type of a struct is encoded as

    ..code-block:: text

        name ‖ "(" ‖ member₁ ‖ "," ‖ member₂ ‖ "," ‖ … ‖ memberₙ ")"

    where each member is written as ``type ‖ " " ‖ name``.
    """
    # Getting the dependencies and sorting them alphabetically as per EIP712
    deps = get_dependencies(primary_type, types)
    sorted_deps = (primary_type,) + tuple(sorted(deps))

    return ''.join(
        encode_struct(struct_name, types[struct_name]) for struct_name in sorted_deps
    )


def is_array_type(type_: str) -> bool:
    """Identify if type such as ``person[]`` or ``person[2]`` is an array."""
    return parse(type_).is_array


@to_tuple
def get_depths_and_dimensions(data: Any, depth: int) -> Iterator[tuple[int, int]]:
    """Generate tuples of depth and dimension of each element at that depth."""
    if not isinstance(data, (list, tuple)):
        # Not checking for Iterable instance, because even Dictionaries and strings
        # are considered as iterables, but that's not what we want the condition to be.
        return ()

    yield depth, len(data)

    for item in data:
        # iterating over all 1 dimension less sub-data items
        yield from get_depths_and_dimensions(item, depth + 1)


def get_array_dimensions(data: Any) -> tuple[int, ...]:
    """Given an data item, check that it is an array and return the dimensions.

    Examples:
        >>> get_array_dimensions([[1, 2, 3], [4, 5, 6]])
        (2, 3)

    """
    depths_and_dimensions = get_depths_and_dimensions(data, 0)
    # re-form as a dictionary with `depth` as key, and all of the dimensions
    # found at that depth.
    grouped_by_depth = {
        depth: tuple(dimension for depth, dimension in group)
        for depth, group in groupby(depths_and_dimensions, itemgetter(0))
    }

    # validate that there is only one dimension for any given depth.
    invalid_depths_dimensions = tuple(
        (depth, dimensions)
        for depth, dimensions in grouped_by_depth.items()
        if len(set(dimensions)) != 1
    )
    if invalid_depths_dimensions:
        raise ValidationError(
            '\n'.join(
                (
                    f'Depth {depth} of array data has more than'
                    ' one dimensions: {dimensions}'
                )
                for depth, dimensions in invalid_depths_dimensions
            )
        )

    return tuple(
        toolz.first(set(dimensions))
        for depth, dimensions in sorted(grouped_by_depth.items())
    )


@to_tuple
def flatten_multidimensional_array(array: Iterable[Any]) -> Iterator[Any]:
    """Flatten nd-array to 1d-array."""
    for item in array:
        if isinstance(item, (list, tuple)):
            # Not checking for Iterable instance, because even Dictionaries
            # and strings are considered iterables,
            # but that's not what we want the condition to be.
            yield from flatten_multidimensional_array(item)
        else:
            yield item


def _check_unknown_type(
    primary_type: str, field: _FieldT, value: Any
) -> tuple[str, Any]:
    # First checking to see if type is valid as per abi
    if not is_encodable_type(field['type']):
        raise TypeError(
            'Received Invalid type `{}` in the struct `{}`'.format(
                field['type'],
                primary_type,
            )
        )

    # Next see if the data fits the specified encoding type
    if not is_encodable(field['type'], value):
        raise TypeError(
            'Value of `{name}` ({value}) in the struct `{struct}` is of '
            'type `{type_}`, but expected {exp_type} value'.format(
                name=field['name'],
                struct=primary_type,
                value=value,
                type_=type(value),
                exp_type=field['type'],
            )
        )

    # field["type"] is a valid type and this value corresponds to that type.
    return field['type'], value


@to_tuple
def _encode_data(
    primary_type: str, types: _TypesT, data: Mapping[str, Any]
) -> Iterator[tuple[str, Any]]:
    # Add typehash
    yield 'bytes32', keccak(text=encode_type(primary_type, types))

    # Add field contents
    for field in types[primary_type]:
        value = data[field['name']]
        if field['type'] == 'string':
            if not isinstance(value, str):
                raise TypeError(
                    (
                        'Value of `{name}` ({value}) in the struct `{struct}` is of '
                        'type `{type_}`, but expected string value'
                    ).format(
                        name=field['name'],
                        value=value,
                        struct=primary_type,
                        type_=type(value),
                    )
                )
            # Special case where the values need to be keccak hashed
            # before they are encoded
            hashed_value = keccak(text=value)
            yield 'bytes32', hashed_value
        elif field['type'] == 'bytes':
            if not isinstance(value, bytes):
                raise TypeError(
                    (
                        'Value of `{name}` ({value}) in the struct `{struct}` is of '
                        'type `{type_}`, but expected bytes value'
                    ).format(
                        name=field['name'],
                        value=value,
                        struct=primary_type,
                        type_=type(value),
                    )
                )
            # Special case where the values need to be keccak hashed
            # before they are encoded
            hashed_value = keccak(primitive=value)
            yield 'bytes32', hashed_value
        elif field['type'] in types:
            # This means that this type is a user defined type
            hashed_value = encode_data(field['type'], types, value)
            yield 'bytes32', hashed_value
        elif is_array_type(field['type']):
            # Get the dimensions from the value
            array_dimensions = get_array_dimensions(value)
            # Get the dimensions from what was declared in the schema
            parsed_type = parse(field['type'])
            for given, expected in zip(array_dimensions, parsed_type.arrlist):
                if expected and given != expected[0]:
                    # Dimensions should match with declared schema
                    raise TypeError(
                        'Array data `{value}` has dimensions `{given}` whereas the '
                        'schema has dimensions `{expected}`'.format(
                            value=value,
                            given=array_dimensions,
                            expected=tuple(map(lambda x: x[0], parsed_type.arrlist)),
                        )
                    )

            concatenated_encodings = b''.join(
                encode_data(parsed_type.base, types, array_item)
                for array_item in flatten_multidimensional_array(value)
            )
            hashed_value = keccak(concatenated_encodings)
            yield 'bytes32', hashed_value
        else:
            yield _check_unknown_type(primary_type, field, value)


def encode_data(primary_type: str, types: _TypesT, data: Mapping[str, Any]) -> bytes:
    """Encode data according to given type declarations."""
    data_types_and_hashes = _encode_data(primary_type, types, data)
    data_types, data_hashes = zip(*data_types_and_hashes)
    enc = encode(data_types, data_hashes)
    if primary_type in types:
        return keccak(enc)
    return enc


def hash_domain(structured_data: EIPToSign) -> bytes:
    """Hash domain part of EIP-712 message."""
    return encode_data(
        'EIP712Domain', structured_data.types, asdict(structured_data.domain)
    )


def hash_message(structured_data: EIPToSign) -> bytes:
    """Hash message part of EIP-712 message."""
    return encode_data(
        structured_data.primaryType,
        structured_data.types,
        structured_data.message,
    )
