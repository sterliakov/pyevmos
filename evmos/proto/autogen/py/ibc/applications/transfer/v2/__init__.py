# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/applications/transfer/v2/packet.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class FungibleTokenPacketData(betterproto.Message):
    """
    FungibleTokenPacketData defines a struct for the packet payload
    See FungibleTokenPacketData spec:
    https://github.com/cosmos/ibc/blob/main/spec/app/ics-020-fungible-token-transfer/README.md
    """

    denom: str = betterproto.string_field(1)
    """the token denomination to be transferred"""

    amount: str = betterproto.string_field(2)
    """the token amount to be transferred"""

    sender: str = betterproto.string_field(3)
    """the sender address"""

    receiver: str = betterproto.string_field(4)
    """the recipient address on the destination chain"""

    memo: str = betterproto.string_field(5)
    """optional memo"""
