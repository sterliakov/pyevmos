# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/crypto/keys.proto, tendermint/crypto/proof.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class Proof(betterproto.Message):
    total: int = betterproto.int64_field(1)
    index: int = betterproto.int64_field(2)
    leaf_hash: bytes = betterproto.bytes_field(3)
    aunts: List[bytes] = betterproto.bytes_field(4)


@dataclass(eq=False, repr=False)
class ValueOp(betterproto.Message):
    key: bytes = betterproto.bytes_field(1)
    """Encoded in ProofOp.Key."""

    proof: "Proof" = betterproto.message_field(2)
    """To encode in ProofOp.Data"""


@dataclass(eq=False, repr=False)
class DominoOp(betterproto.Message):
    key: str = betterproto.string_field(1)
    input: str = betterproto.string_field(2)
    output: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class ProofOp(betterproto.Message):
    """
    ProofOp defines an operation used for calculating Merkle root
    The data could be arbitrary format, providing nessecary data
    for example neighbouring node hash
    """

    type: str = betterproto.string_field(1)
    key: bytes = betterproto.bytes_field(2)
    data: bytes = betterproto.bytes_field(3)


@dataclass(eq=False, repr=False)
class ProofOps(betterproto.Message):
    """ProofOps is Merkle proof defined by the list of ProofOps"""

    ops: List["ProofOp"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class PublicKey(betterproto.Message):
    """PublicKey defines the keys available for use with Validators"""

    ed25519: bytes = betterproto.bytes_field(1, group="sum")
    secp256_k1: bytes = betterproto.bytes_field(2, group="sum")
