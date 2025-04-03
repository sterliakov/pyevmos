# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/base/v1beta1/coin.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class Coin(betterproto.Message):
    """
    Coin defines a token with a denomination and an amount.
    NOTE: The amount field is an Int which implements the custom method
    signatures required by gogoproto.
    """

    denom: str = betterproto.string_field(1)
    amount: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class DecCoin(betterproto.Message):
    """
    DecCoin defines a token with a denomination and a decimal amount.
    NOTE: The amount field is an Dec which implements the custom method
    signatures required by gogoproto.
    """

    denom: str = betterproto.string_field(1)
    amount: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class IntProto(betterproto.Message):
    """IntProto defines a Protobuf wrapper around an Int object."""

    int: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class DecProto(betterproto.Message):
    """DecProto defines a Protobuf wrapper around a Dec object."""

    dec: str = betterproto.string_field(1)
