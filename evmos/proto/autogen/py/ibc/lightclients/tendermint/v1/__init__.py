# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/lightclients/tendermint/v1/tendermint.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)
from typing import List

import betterproto

from ..... import ics23 as ____ics23__
from .....tendermint import types as ____tendermint_types__
from ....core.client import v1 as ___core_client_v1__
from ....core.commitment import v1 as ___core_commitment_v1__


@dataclass(eq=False, repr=False)
class ClientState(betterproto.Message):
    """
    ClientState from Tendermint tracks the current validator set, latest height,
    and a possible frozen height.
    """

    chain_id: str = betterproto.string_field(1)
    trust_level: "Fraction" = betterproto.message_field(2)
    trusting_period: timedelta = betterproto.message_field(3)
    """
    duration of the period since the LastestTimestamp during which the
    submitted headers are valid for upgrade
    """

    unbonding_period: timedelta = betterproto.message_field(4)
    """duration of the staking unbonding period"""

    max_clock_drift: timedelta = betterproto.message_field(5)
    """defines how much new (untrusted) header's Time can drift into the future."""

    frozen_height: "___core_client_v1__.Height" = betterproto.message_field(6)
    """Block height when the client was frozen due to a misbehaviour"""

    latest_height: "___core_client_v1__.Height" = betterproto.message_field(7)
    """Latest height the client was updated to"""

    proof_specs: List["____ics23__.ProofSpec"] = betterproto.message_field(8)
    """Proof specifications used in verifying counterparty state"""

    upgrade_path: List[str] = betterproto.string_field(9)
    """
    Path at which next upgraded client will be committed.
    Each element corresponds to the key for a single CommitmentProof in the
    chained proof. NOTE: ClientState must stored under
    `{upgradePath}/{upgradeHeight}/clientState` ConsensusState must be stored
    under `{upgradepath}/{upgradeHeight}/consensusState` For SDK chains using
    the default upgrade module, upgrade_path should be []string{"upgrade",
    "upgradedIBCState"}`
    """

    allow_update_after_expiry: bool = betterproto.bool_field(10)
    """
    This flag, when set to true, will allow governance to recover a client
    which has expired
    """

    allow_update_after_misbehaviour: bool = betterproto.bool_field(11)
    """
    This flag, when set to true, will allow governance to unfreeze a client
    whose chain has experienced a misbehaviour event
    """


@dataclass(eq=False, repr=False)
class ConsensusState(betterproto.Message):
    """ConsensusState defines the consensus state from Tendermint."""

    timestamp: datetime = betterproto.message_field(1)
    """
    timestamp that corresponds to the block height in which the ConsensusState
    was stored.
    """

    root: "___core_commitment_v1__.MerkleRoot" = betterproto.message_field(2)
    """commitment root (i.e app hash)"""

    next_validators_hash: bytes = betterproto.bytes_field(3)


@dataclass(eq=False, repr=False)
class Misbehaviour(betterproto.Message):
    """
    Misbehaviour is a wrapper over two conflicting Headers
    that implements Misbehaviour interface expected by ICS-02
    """

    client_id: str = betterproto.string_field(1)
    header_1: "Header" = betterproto.message_field(2)
    header_2: "Header" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class Header(betterproto.Message):
    """
    Header defines the Tendermint client consensus Header.
    It encapsulates all the information necessary to update from a trusted
    Tendermint ConsensusState. The inclusion of TrustedHeight and
    TrustedValidators allows this update to process correctly, so long as the
    ConsensusState for the TrustedHeight exists, this removes race conditions
    among relayers The SignedHeader and ValidatorSet are the new untrusted update
    fields for the client. The TrustedHeight is the height of a stored
    ConsensusState on the client that will be used to verify the new untrusted
    header. The Trusted ConsensusState must be within the unbonding period of
    current time in order to correctly verify, and the TrustedValidators must
    hash to TrustedConsensusState.NextValidatorsHash since that is the last
    trusted validator set at the TrustedHeight.
    """

    signed_header: "____tendermint_types__.SignedHeader" = betterproto.message_field(1)
    validator_set: "____tendermint_types__.ValidatorSet" = betterproto.message_field(2)
    trusted_height: "___core_client_v1__.Height" = betterproto.message_field(3)
    trusted_validators: "____tendermint_types__.ValidatorSet" = (
        betterproto.message_field(4)
    )


@dataclass(eq=False, repr=False)
class Fraction(betterproto.Message):
    """
    Fraction defines the protobuf message type for tmmath.Fraction that only
    supports positive values.
    """

    numerator: int = betterproto.uint64_field(1)
    denominator: int = betterproto.uint64_field(2)
