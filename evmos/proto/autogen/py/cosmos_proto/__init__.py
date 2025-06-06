# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos_proto/cosmos.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto


class ScalarType(betterproto.Enum):
    SCALAR_TYPE_UNSPECIFIED = 0
    SCALAR_TYPE_STRING = 1
    SCALAR_TYPE_BYTES = 2


@dataclass(eq=False, repr=False)
class InterfaceDescriptor(betterproto.Message):
    """
    InterfaceDescriptor describes an interface type to be used with
    accepts_interface and implements_interface and declared by declare_interface.
    """

    name: str = betterproto.string_field(1)
    """
    name is the name of the interface. It should be a short-name (without
    a period) such that the fully qualified name of the interface will be
    package.name, ex. for the package a.b and interface named C, the
    fully-qualified name will be a.b.C.
    """

    description: str = betterproto.string_field(2)
    """
    description is a human-readable description of the interface and its
    purpose.
    """


@dataclass(eq=False, repr=False)
class ScalarDescriptor(betterproto.Message):
    """
    ScalarDescriptor describes an scalar type to be used with
    the scalar field option and declared by declare_scalar.
    Scalars extend simple protobuf built-in types with additional
    syntax and semantics, for instance to represent big integers.
    Scalars should ideally define an encoding such that there is only one
    valid syntactical representation for a given semantic meaning,
    i.e. the encoding should be deterministic.
    """

    name: str = betterproto.string_field(1)
    """
    name is the name of the scalar. It should be a short-name (without
    a period) such that the fully qualified name of the scalar will be
    package.name, ex. for the package a.b and scalar named C, the
    fully-qualified name will be a.b.C.
    """

    description: str = betterproto.string_field(2)
    """
    description is a human-readable description of the scalar and its
    encoding format. For instance a big integer or decimal scalar should
    specify precisely the expected encoding format.
    """

    field_type: List["ScalarType"] = betterproto.enum_field(3)
    """
    field_type is the type of field with which this scalar can be used.
    Scalars can be used with one and only one type of field so that
    encoding standards and simple and clear. Currently only string and
    bytes fields are supported for scalars.
    """
