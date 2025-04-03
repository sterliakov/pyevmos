# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ethermint/crypto/v1/ethsecp256k1/keys.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class PubKey(betterproto.Message):
    """
    PubKey defines a type alias for an ecdsa.PublicKey that implements
    Tendermint's PubKey interface. It represents the 33-byte compressed public
    key format.
    """

    key: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class PrivKey(betterproto.Message):
    """
    PrivKey defines a type alias for an ecdsa.PrivateKey that implements
    Tendermint's PrivateKey interface.
    """

    key: bytes = betterproto.bytes_field(1)
