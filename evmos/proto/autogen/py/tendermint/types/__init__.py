# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/types/block.proto, tendermint/types/evidence.proto, tendermint/types/params.proto, tendermint/types/types.proto, tendermint/types/validator.proto
# plugin: python-betterproto
# This file has been @generated
import builtins
from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)
from typing import List

import betterproto

from .. import (
    crypto as _crypto__,
    version as _version__,
)


class BlockIdFlag(betterproto.Enum):
    """BlockIdFlag indicates which BlockID the signature is for"""

    BLOCK_ID_FLAG_UNKNOWN = 0
    BLOCK_ID_FLAG_ABSENT = 1
    BLOCK_ID_FLAG_COMMIT = 2
    BLOCK_ID_FLAG_NIL = 3


class SignedMsgType(betterproto.Enum):
    """SignedMsgType is a type of signed message in the consensus."""

    SIGNED_MSG_TYPE_UNKNOWN = 0
    SIGNED_MSG_TYPE_PREVOTE = 1
    """Votes"""

    SIGNED_MSG_TYPE_PRECOMMIT = 2
    SIGNED_MSG_TYPE_PROPOSAL = 32
    """Proposals"""


@dataclass(eq=False, repr=False)
class ConsensusParams(betterproto.Message):
    """
    ConsensusParams contains consensus critical parameters that determine the
    validity of blocks.
    """

    block: "BlockParams" = betterproto.message_field(1)
    evidence: "EvidenceParams" = betterproto.message_field(2)
    validator: "ValidatorParams" = betterproto.message_field(3)
    version: "VersionParams" = betterproto.message_field(4)
    abci: "AbciParams" = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class BlockParams(betterproto.Message):
    """BlockParams contains limits on the block size."""

    max_bytes: int = betterproto.int64_field(1)
    """
    Max block size, in bytes.
    Note: must be greater than 0
    """

    max_gas: int = betterproto.int64_field(2)
    """
    Max gas per block.
    Note: must be greater or equal to -1
    """


@dataclass(eq=False, repr=False)
class EvidenceParams(betterproto.Message):
    """EvidenceParams determine how we handle evidence of malfeasance."""

    max_age_num_blocks: int = betterproto.int64_field(1)
    """
    Max age of evidence, in blocks.
    The basic formula for calculating this is: MaxAgeDuration / {average block
    time}.
    """

    max_age_duration: timedelta = betterproto.message_field(2)
    """
    Max age of evidence, in time.
    It should correspond with an app's "unbonding period" or other similar
    mechanism for handling Nothing-At-Stake attacks.
    """

    max_bytes: int = betterproto.int64_field(3)
    """
    This sets the maximum size of total evidence in bytes that can be committed in a
    single block.
    and should fall comfortably under the max block bytes.
    Default is 1048576 or 1MB
    """


@dataclass(eq=False, repr=False)
class ValidatorParams(betterproto.Message):
    """
    ValidatorParams restrict the public key types validators can use.
    NOTE: uses ABCI pubkey naming, not Amino names.
    """

    pub_key_types: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class VersionParams(betterproto.Message):
    """VersionParams contains the ABCI application version."""

    app: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class HashedParams(betterproto.Message):
    """
    HashedParams is a subset of ConsensusParams.
    It is hashed into the Header.ConsensusHash.
    """

    block_max_bytes: int = betterproto.int64_field(1)
    block_max_gas: int = betterproto.int64_field(2)


@dataclass(eq=False, repr=False)
class AbciParams(betterproto.Message):
    """
    ABCIParams configure functionality specific to the Application Blockchain Interface.
    """

    vote_extensions_enable_height: int = betterproto.int64_field(1)
    """
    vote_extensions_enable_height configures the first height during which
    vote extensions will be enabled. During this specified height, and for all
    subsequent heights, precommit messages that do not contain valid extension data
    will be considered invalid. Prior to this height, vote extensions will not
    be used or accepted by validators on the network.
    Once enabled, vote extensions will be created by the application in ExtendVote,
    passed to the application for validation in VerifyVoteExtension and given
    to the application to use when proposing a block during PrepareProposal.
    """


@dataclass(eq=False, repr=False)
class ValidatorSet(betterproto.Message):
    validators: List["Validator"] = betterproto.message_field(1)
    proposer: "Validator" = betterproto.message_field(2)
    total_voting_power: int = betterproto.int64_field(3)


@dataclass(eq=False, repr=False)
class Validator(betterproto.Message):
    address: bytes = betterproto.bytes_field(1)
    pub_key: "_crypto__.PublicKey" = betterproto.message_field(2)
    voting_power: int = betterproto.int64_field(3)
    proposer_priority: int = betterproto.int64_field(4)


@dataclass(eq=False, repr=False)
class SimpleValidator(betterproto.Message):
    pub_key: "_crypto__.PublicKey" = betterproto.message_field(1)
    voting_power: int = betterproto.int64_field(2)


@dataclass(eq=False, repr=False)
class PartSetHeader(betterproto.Message):
    """PartsetHeader"""

    total: int = betterproto.uint32_field(1)
    hash: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class Part(betterproto.Message):
    index: int = betterproto.uint32_field(1)
    bytes: builtins.bytes = betterproto.bytes_field(2)
    proof: "_crypto__.Proof" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class BlockId(betterproto.Message):
    """BlockID"""

    hash: bytes = betterproto.bytes_field(1)
    part_set_header: "PartSetHeader" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Header(betterproto.Message):
    """Header defines the structure of a block header."""

    version: "_version__.Consensus" = betterproto.message_field(1)
    """basic block info"""

    chain_id: str = betterproto.string_field(2)
    height: int = betterproto.int64_field(3)
    time: datetime = betterproto.message_field(4)
    last_block_id: "BlockId" = betterproto.message_field(5)
    """prev block info"""

    last_commit_hash: bytes = betterproto.bytes_field(6)
    """hashes of block data"""

    data_hash: bytes = betterproto.bytes_field(7)
    validators_hash: bytes = betterproto.bytes_field(8)
    """hashes from the app output from the prev block"""

    next_validators_hash: bytes = betterproto.bytes_field(9)
    consensus_hash: bytes = betterproto.bytes_field(10)
    app_hash: bytes = betterproto.bytes_field(11)
    last_results_hash: bytes = betterproto.bytes_field(12)
    evidence_hash: bytes = betterproto.bytes_field(13)
    """consensus info"""

    proposer_address: bytes = betterproto.bytes_field(14)


@dataclass(eq=False, repr=False)
class Data(betterproto.Message):
    """Data contains the set of transactions included in the block"""

    txs: List[bytes] = betterproto.bytes_field(1)
    """
    Txs that will be applied by state @ block.Height+1.
    NOTE: not all txs here are valid.  We're just agreeing on the order first.
    This means that block.AppHash does not include these txs.
    """


@dataclass(eq=False, repr=False)
class Vote(betterproto.Message):
    """
    Vote represents a prevote or precommit vote from validators for
    consensus.
    """

    type: "SignedMsgType" = betterproto.enum_field(1)
    height: int = betterproto.int64_field(2)
    round: int = betterproto.int32_field(3)
    block_id: "BlockId" = betterproto.message_field(4)
    timestamp: datetime = betterproto.message_field(5)
    validator_address: bytes = betterproto.bytes_field(6)
    validator_index: int = betterproto.int32_field(7)
    signature: bytes = betterproto.bytes_field(8)
    """
    Vote signature by the validator if they participated in consensus for the
    associated block.
    """

    extension: bytes = betterproto.bytes_field(9)
    """
    Vote extension provided by the application. Only valid for precommit
    messages.
    """

    extension_signature: bytes = betterproto.bytes_field(10)
    """
    Vote extension signature by the validator if they participated in
    consensus for the associated block.
    Only valid for precommit messages.
    """


@dataclass(eq=False, repr=False)
class Commit(betterproto.Message):
    """
    Commit contains the evidence that a block was committed by a set of validators.
    """

    height: int = betterproto.int64_field(1)
    round: int = betterproto.int32_field(2)
    block_id: "BlockId" = betterproto.message_field(3)
    signatures: List["CommitSig"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class CommitSig(betterproto.Message):
    """CommitSig is a part of the Vote included in a Commit."""

    block_id_flag: "BlockIdFlag" = betterproto.enum_field(1)
    validator_address: bytes = betterproto.bytes_field(2)
    timestamp: datetime = betterproto.message_field(3)
    signature: bytes = betterproto.bytes_field(4)


@dataclass(eq=False, repr=False)
class ExtendedCommit(betterproto.Message):
    height: int = betterproto.int64_field(1)
    round: int = betterproto.int32_field(2)
    block_id: "BlockId" = betterproto.message_field(3)
    extended_signatures: List["ExtendedCommitSig"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ExtendedCommitSig(betterproto.Message):
    """
    ExtendedCommitSig retains all the same fields as CommitSig but adds vote
    extension-related fields. We use two signatures to ensure backwards compatibility.
    That is the digest of the original signature is still the same in prior versions
    """

    block_id_flag: "BlockIdFlag" = betterproto.enum_field(1)
    validator_address: bytes = betterproto.bytes_field(2)
    timestamp: datetime = betterproto.message_field(3)
    signature: bytes = betterproto.bytes_field(4)
    extension: bytes = betterproto.bytes_field(5)
    """Vote extension data"""

    extension_signature: bytes = betterproto.bytes_field(6)
    """Vote extension signature"""


@dataclass(eq=False, repr=False)
class Proposal(betterproto.Message):
    type: "SignedMsgType" = betterproto.enum_field(1)
    height: int = betterproto.int64_field(2)
    round: int = betterproto.int32_field(3)
    pol_round: int = betterproto.int32_field(4)
    block_id: "BlockId" = betterproto.message_field(5)
    timestamp: datetime = betterproto.message_field(6)
    signature: bytes = betterproto.bytes_field(7)


@dataclass(eq=False, repr=False)
class SignedHeader(betterproto.Message):
    header: "Header" = betterproto.message_field(1)
    commit: "Commit" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class LightBlock(betterproto.Message):
    signed_header: "SignedHeader" = betterproto.message_field(1)
    validator_set: "ValidatorSet" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class BlockMeta(betterproto.Message):
    block_id: "BlockId" = betterproto.message_field(1)
    block_size: int = betterproto.int64_field(2)
    header: "Header" = betterproto.message_field(3)
    num_txs: int = betterproto.int64_field(4)


@dataclass(eq=False, repr=False)
class TxProof(betterproto.Message):
    """
    TxProof represents a Merkle proof of the presence of a transaction in the Merkle
    tree.
    """

    root_hash: bytes = betterproto.bytes_field(1)
    data: bytes = betterproto.bytes_field(2)
    proof: "_crypto__.Proof" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class Evidence(betterproto.Message):
    duplicate_vote_evidence: "DuplicateVoteEvidence" = betterproto.message_field(
        1, group="sum"
    )
    light_client_attack_evidence: "LightClientAttackEvidence" = (
        betterproto.message_field(2, group="sum")
    )


@dataclass(eq=False, repr=False)
class DuplicateVoteEvidence(betterproto.Message):
    """
    DuplicateVoteEvidence contains evidence of a validator signed two conflicting votes.
    """

    vote_a: "Vote" = betterproto.message_field(1)
    vote_b: "Vote" = betterproto.message_field(2)
    total_voting_power: int = betterproto.int64_field(3)
    validator_power: int = betterproto.int64_field(4)
    timestamp: datetime = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class LightClientAttackEvidence(betterproto.Message):
    """
    LightClientAttackEvidence contains evidence of a set of validators attempting to
    mislead a light client.
    """

    conflicting_block: "LightBlock" = betterproto.message_field(1)
    common_height: int = betterproto.int64_field(2)
    byzantine_validators: List["Validator"] = betterproto.message_field(3)
    total_voting_power: int = betterproto.int64_field(4)
    timestamp: datetime = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class EvidenceList(betterproto.Message):
    evidence: List["Evidence"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Block(betterproto.Message):
    header: "Header" = betterproto.message_field(1)
    data: "Data" = betterproto.message_field(2)
    evidence: "EvidenceList" = betterproto.message_field(3)
    last_commit: "Commit" = betterproto.message_field(4)
