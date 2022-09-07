"""Hashing utilities for EIP-712 messages.

Copied under the MIT license from
https://github.com/ethereum/eth-account/blob/master/eth_account/_utils/structured_data/hashing.py
with minor modifications.
"""
from __future__ import annotations

from dataclasses import asdict
from itertools import chain, groupby
from operator import itemgetter
from typing import Any, Iterable, Iterator, Mapping, Sequence, TypedDict

from eth_abi import encode, is_encodable, is_encodable_type
from eth_abi.grammar import parse
from eth_utils import keccak, to_tuple
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

    while struct_names_yet_to_be_expanded:
        struct_name = struct_names_yet_to_be_expanded.pop()

        deps.add(struct_name)
        fields = types[struct_name]
        for field in fields:
            field_type = field['type']

            # Handle array types
            if is_array_type(field_type):
                field_type = field_type[: field_type.index('[')]

            if field_type in types and field_type not in deps:
                # We don't need to expand types that are not user defined (customized)
                # Also skip types that we have already encountered
                struct_names_yet_to_be_expanded.append(field_type)

    # Don't need to make a struct as dependency of itself
    deps.remove(primary_type)

    return tuple(deps)


def field_identifier(field: _FieldT) -> str:
    """Stringify a field in ``'TYPE NAME'`` format."""
    return f'{field["type"]} {field["name"]}'


def encode_struct(struct_name: str, struct_field_types: Iterable[_FieldT]) -> str:
    """Stringify a single struct in ``'NAME(type1 name1,type2 name2,...)'`` format."""
    return '{name}({args})'.format(
        name=struct_name,
        args=','.join(map(field_identifier, struct_field_types)),
    )


def encode_type(primary_type: str, types: _TypesT) -> str:
    """Encode type as concatenation of itself and all dependencies (alphabetical order).

    The type of a struct is encoded as

    .. code-block:: text

        name ‖ "(" ‖ member₁ ‖ "," ‖ member₂ ‖ "," ‖ … ‖ memberₙ ")"

    where each member is written as ``type ‖ " " ‖ name``.
    """
    # Getting the dependencies and sorting them alphabetically as per EIP712
    deps = get_dependencies(primary_type, types)

    return ''.join(
        encode_struct(struct_name, types[struct_name])
        for struct_name in chain((primary_type,), sorted(deps))
    )


def hash_struct_type(primary_type: str, types: _TypesT) -> bytes:
    """Hash string representation of type of struct."""
    return keccak(text=encode_type(primary_type, types))


def is_array_type(type_: str) -> bool:
    """Identify if type such as ``person[]`` or ``person[2]`` is an array."""
    return type_.endswith(']')


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


def get_array_dimensions(data: Any) -> tuple[int | str, ...]:
    """Given an data item, check that it is an array and return the dimensions.

    Examples:
        >>> get_array_dimensions([[1, 2, 3], [4, 5, 6]])
        (3, 2)

    """
    depths_and_dimensions = get_depths_and_dimensions(data, 0)
    # re-form as a dictionary with `depth` as key, and all of the dimensions
    # found at that depth.
    grouped_by_depth = {
        depth: tuple(dimension for depth, dimension in group)
        for depth, group in groupby(depths_and_dimensions, itemgetter(0))
    }

    return tuple(
        # check that all dimensions are the same, else use "dynamic"
        dimensions[0] if all(dim == dimensions[0] for dim in dimensions) else 'dynamic'
        for _depth, dimensions in sorted(grouped_by_depth.items(), reverse=True)
    )


def _check_dimensions(field_type: str, value: Any) -> None:
    # Get the dimensions from the value
    array_dimensions = get_array_dimensions(value)
    # Get the dimensions from what was declared in the schema
    parsed_field_type = parse(field_type)

    for given, expected in zip(array_dimensions, parsed_field_type.arrlist):
        if not expected:
            # Skip empty or dynamically declared dimensions
            continue
        if given != expected[0]:
            # Dimensions should match with declared schema
            expected_dimensions_repr = tuple(
                map(lambda x: x[0] if x else 'dynamic', parsed_field_type.arrlist)
            )
            raise TypeError(
                f'Array data `{value}` has dimensions `{array_dimensions}`'
                f' whereas the schema has dimensions `{expected_dimensions_repr}`'
            )


def _encode_array_field(
    types: _TypesT, name: str, field_type: str, value: Any
) -> bytes:
    _check_dimensions(field_type, value)

    if value:
        field_type_of_inside_array = field_type[: field_type.rindex('[')]
        field_type_value_pairs = [
            encode_field(types, name, field_type_of_inside_array, item)
            for item in value
        ]

        data_types, data_hashes = zip(*field_type_value_pairs)
    else:
        data_types = data_hashes = tuple()

    return keccak(encode(data_types, data_hashes))


def encode_field(
    types: _TypesT, name: str, field_type: str, value: Any
) -> tuple[str, bytes]:
    """Encode field according to given type.

    Args:
        types: mapping with all known types
        name: field name
        field_type: type of field (must be present in ``types`` or be basic type)
        value: value to encode

    Returns:
        tuple of form (result_type, encoded_bytes)
    """
    if value is None:
        raise ValueError(f'Missing value for field {name} of type {field_type}')

    if field_type in types:
        return ('bytes32', keccak(encode_data(field_type, types, value)))

    if field_type == 'bytes':
        if not isinstance(value, bytes):
            raise TypeError(
                f'Value of field `{name}` ({value}) is of the type `{type(value)}`, '
                f'but expected bytes value'
            )

        return ('bytes32', keccak(value))

    if field_type == 'string':
        if not isinstance(value, str):
            raise TypeError(
                f'Value of field `{name}` ({value}) is of the type `{type(value)}`, '
                f'but expected string value'
            )

        return ('bytes32', keccak(text=value))

    if is_array_type(field_type):
        encoded = _encode_array_field(types, name, field_type, value)
        return ('bytes32', encoded)

    # First checking to see if field_type is valid as per abi
    if not is_encodable_type(field_type):
        raise TypeError(f'Received Invalid type `{field_type}` in field `{name}`')

    # Next, see if the value is encodable as the specified field_type
    if is_encodable(field_type, value):
        # field_type is a valid type and the provided value is encodable as that type
        return (field_type, value)

    raise TypeError(
        f'Value of `{name}` ({value}) is not encodable as type `{field_type}`. '
        f'If the base type is correct, verify that the value does not '
        f'exceed the specified size for the type.'
    )


def encode_data(primary_type: str, types: _TypesT, data: Any) -> bytes:
    """Encode data defined by ``primary_type``."""
    encoded_types = ['bytes32']
    encoded_values = [hash_struct_type(primary_type, types)]

    for field in types[primary_type]:
        type_, value = encode_field(
            types, field['name'], field['type'], data[field['name']]
        )
        encoded_types.append(type_)
        encoded_values.append(value)

    return encode(encoded_types, encoded_values)


def hash_domain(structured_data: EIPToSign) -> bytes:
    """Hash domain part of EIP-712 message."""
    return keccak(
        encode_data(
            'EIP712Domain', structured_data.types, asdict(structured_data.domain)
        )
    )


def hash_message(structured_data: EIPToSign) -> bytes:
    """Hash message part of EIP-712 message."""
    return keccak(
        encode_data(
            structured_data.primaryType,
            structured_data.types,
            structured_data.message,
        )
    )
