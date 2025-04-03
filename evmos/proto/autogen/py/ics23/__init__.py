# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: proofs.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto


class HashOp(betterproto.Enum):
    NO_HASH = 0
    """
    NO_HASH is the default if no data passed. Note this is an illegal argument
    some places.
    """

    SHA256 = 1
    SHA512 = 2
    KECCAK = 3
    RIPEMD160 = 4
    BITCOIN = 5


class LengthOp(betterproto.Enum):
    """
    *
    LengthOp defines how to process the key and value of the LeafOp
    to include length information. After encoding the length with the given
    algorithm, the length will be prepended to the key and value bytes.
    (Each one with it's own encoded length)
    """

    NO_PREFIX = 0
    """NO_PREFIX don't include any length info"""

    VAR_PROTO = 1
    """VAR_PROTO uses protobuf (and go-amino) varint encoding of the length"""

    VAR_RLP = 2
    """VAR_RLP uses rlp int encoding of the length"""

    FIXED32_BIG = 3
    """FIXED32_BIG uses big-endian encoding of the length as a 32 bit integer"""

    FIXED32_LITTLE = 4
    """
    FIXED32_LITTLE uses little-endian encoding of the length as a 32 bit
    integer
    """

    FIXED64_BIG = 5
    """FIXED64_BIG uses big-endian encoding of the length as a 64 bit integer"""

    FIXED64_LITTLE = 6
    """
    FIXED64_LITTLE uses little-endian encoding of the length as a 64 bit
    integer
    """

    REQUIRE_32_BYTES = 7
    """
    REQUIRE_32_BYTES is like NONE, but will fail if the input is not exactly 32
    bytes (sha256 output)
    """

    REQUIRE_64_BYTES = 8
    """
    REQUIRE_64_BYTES is like NONE, but will fail if the input is not exactly 64
    bytes (sha512 output)
    """


@dataclass(eq=False, repr=False)
class ExistenceProof(betterproto.Message):
    """
    *
    ExistenceProof takes a key and a value and a set of steps to perform on it.
    The result of peforming all these steps will provide a "root hash", which can
    be compared to the value in a header.
    Since it is computationally infeasible to produce a hash collission for any of
    the used cryptographic hash functions, if someone can provide a series of
    operations to transform a given key and value into a root hash that matches some
    trusted root, these key and values must be in the referenced merkle tree.
    The only possible issue is maliablity in LeafOp, such as providing extra prefix
    data, which should be controlled by a spec. Eg. with lengthOp as NONE, prefix =
    FOO, key = BAR, value = CHOICE and prefix = F, key = OOBAR, value = CHOICE would
    produce the same value.
    With LengthOp this is tricker but not impossible. Which is why the
    "leafPrefixEqual" field in the ProofSpec is valuable to prevent this mutability.
    And why all trees should length-prefix the data before hashing it.
    """

    key: bytes = betterproto.bytes_field(1)
    value: bytes = betterproto.bytes_field(2)
    leaf: "LeafOp" = betterproto.message_field(3)
    path: List["InnerOp"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class NonExistenceProof(betterproto.Message):
    """
    NonExistenceProof takes a proof of two neighbors, one left of the desired key,
    one right of the desired key. If both proofs are valid AND they are neighbors,
    then there is no valid proof for the given key.
    """

    key: bytes = betterproto.bytes_field(1)
    left: "ExistenceProof" = betterproto.message_field(2)
    right: "ExistenceProof" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class CommitmentProof(betterproto.Message):
    """
    CommitmentProof is either an ExistenceProof or a NonExistenceProof, or a Batch
    of such messages
    """

    exist: "ExistenceProof" = betterproto.message_field(1, group="proof")
    nonexist: "NonExistenceProof" = betterproto.message_field(2, group="proof")
    batch: "BatchProof" = betterproto.message_field(3, group="proof")
    compressed: "CompressedBatchProof" = betterproto.message_field(4, group="proof")


@dataclass(eq=False, repr=False)
class LeafOp(betterproto.Message):
    """
    *
    LeafOp represents the raw key-value data we wish to prove, and
    must be flexible to represent the internal transformation from
    the original key-value pairs into the basis hash, for many existing
    merkle trees.
    key and value are passed in. So that the signature of this operation is:
    leafOp(key, value) -> output
    To process this, first prehash the keys and values if needed (ANY means no hash
    in this case): hkey = prehashKey(key) hvalue = prehashValue(value)
    Then combine the bytes, and hash it
    output = hash(prefix || length(hkey) || hkey || length(hvalue) || hvalue)
    """

    hash: "HashOp" = betterproto.enum_field(1)
    prehash_key: "HashOp" = betterproto.enum_field(2)
    prehash_value: "HashOp" = betterproto.enum_field(3)
    length: "LengthOp" = betterproto.enum_field(4)
    prefix: bytes = betterproto.bytes_field(5)
    """
    prefix is a fixed bytes that may optionally be included at the beginning to
    differentiate a leaf node from an inner node.
    """


@dataclass(eq=False, repr=False)
class InnerOp(betterproto.Message):
    """
    *
    InnerOp represents a merkle-proof step that is not a leaf.
    It represents concatenating two children and hashing them to provide the next
    result.
    The result of the previous step is passed in, so the signature of this op is:
    innerOp(child) -> output
    The result of applying InnerOp should be:
    output = op.hash(op.prefix || child || op.suffix)
    where the || operator is concatenation of binary data,
    and child is the result of hashing all the tree below this step.
    Any special data, like prepending child with the length, or prepending the
    entire operation with some value to differentiate from leaf nodes, should be
    included in prefix and suffix. If either of prefix or suffix is empty, we just
    treat it as an empty string
    """

    hash: "HashOp" = betterproto.enum_field(1)
    prefix: bytes = betterproto.bytes_field(2)
    suffix: bytes = betterproto.bytes_field(3)


@dataclass(eq=False, repr=False)
class ProofSpec(betterproto.Message):
    """
    *
    ProofSpec defines what the expected parameters are for a given proof type.
    This can be stored in the client and used to validate any incoming proofs.
    verify(ProofSpec, Proof) -> Proof | Error
    As demonstrated in tests, if we don't fix the algorithm used to calculate the
    LeafHash for a given tree, there are many possible key-value pairs that can
    generate a given hash (by interpretting the preimage differently).
    We need this for proper security, requires client knows a priori what
    tree format server uses. But not in code, rather a configuration object.
    """

    leaf_spec: "LeafOp" = betterproto.message_field(1)
    """
    any field in the ExistenceProof must be the same as in this spec.
    except Prefix, which is just the first bytes of prefix (spec can be longer)
    """

    inner_spec: "InnerSpec" = betterproto.message_field(2)
    max_depth: int = betterproto.int32_field(3)
    """
    max_depth (if > 0) is the maximum number of InnerOps allowed (mainly for
    fixed-depth tries)
    """

    min_depth: int = betterproto.int32_field(4)
    """
    min_depth (if > 0) is the minimum number of InnerOps allowed (mainly for
    fixed-depth tries)
    """


@dataclass(eq=False, repr=False)
class InnerSpec(betterproto.Message):
    """
    InnerSpec contains all store-specific structure info to determine if two proofs
    from a given store are neighbors.
    This enables:
    isLeftMost(spec: InnerSpec, op: InnerOp)
    isRightMost(spec: InnerSpec, op: InnerOp)
    isLeftNeighbor(spec: InnerSpec, left: InnerOp, right: InnerOp)
    """

    child_order: List[int] = betterproto.int32_field(1)
    """
    Child order is the ordering of the children node, must count from 0
    iavl tree is [0, 1] (left then right)
    merk is [0, 2, 1] (left, right, here)
    """

    child_size: int = betterproto.int32_field(2)
    min_prefix_length: int = betterproto.int32_field(3)
    max_prefix_length: int = betterproto.int32_field(4)
    empty_child: bytes = betterproto.bytes_field(5)
    """
    empty child is the prehash image that is used when one child is nil (eg. 20
    bytes of 0)
    """

    hash: "HashOp" = betterproto.enum_field(6)
    """hash is the algorithm that must be used for each InnerOp"""


@dataclass(eq=False, repr=False)
class BatchProof(betterproto.Message):
    """BatchProof is a group of multiple proof types than can be compressed"""

    entries: List["BatchEntry"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class BatchEntry(betterproto.Message):
    """Use BatchEntry not CommitmentProof, to avoid recursion"""

    exist: "ExistenceProof" = betterproto.message_field(1, group="proof")
    nonexist: "NonExistenceProof" = betterproto.message_field(2, group="proof")


@dataclass(eq=False, repr=False)
class CompressedBatchProof(betterproto.Message):
    entries: List["CompressedBatchEntry"] = betterproto.message_field(1)
    lookup_inners: List["InnerOp"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class CompressedBatchEntry(betterproto.Message):
    """Use BatchEntry not CommitmentProof, to avoid recursion"""

    exist: "CompressedExistenceProof" = betterproto.message_field(1, group="proof")
    nonexist: "CompressedNonExistenceProof" = betterproto.message_field(
        2, group="proof"
    )


@dataclass(eq=False, repr=False)
class CompressedExistenceProof(betterproto.Message):
    key: bytes = betterproto.bytes_field(1)
    value: bytes = betterproto.bytes_field(2)
    leaf: "LeafOp" = betterproto.message_field(3)
    path: List[int] = betterproto.int32_field(4)
    """these are indexes into the lookup_inners table in CompressedBatchProof"""


@dataclass(eq=False, repr=False)
class CompressedNonExistenceProof(betterproto.Message):
    key: bytes = betterproto.bytes_field(1)
    left: "CompressedExistenceProof" = betterproto.message_field(2)
    right: "CompressedExistenceProof" = betterproto.message_field(3)
