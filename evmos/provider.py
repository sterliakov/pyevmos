from __future__ import annotations

import json
from enum import Enum
from typing import Callable, Sequence, TypedDict

from typing_extensions import NotRequired

# Enums


class BroadcastMode(str, Enum):
    """Broadcasting mode."""

    Unspecified = 'BROADCAST_MODE_UNSPECIFIED'
    Block = 'BROADCAST_MODE_BLOCK'
    Sync = 'BROADCAST_MODE_SYNC'
    Async = 'BROADCAST_MODE_ASYNC'


class ProposalStatus(str, Enum):
    """Proposal status."""

    Unspecified = 'PROPOSAL_STATUS_UNSPECIFIED'
    Deposit = 'PROPOSAL_STATUS_DEPOSIT_PERIOD'
    Voting = 'PROPOSAL_STATUS_VOTING_PERIOD'
    Passed = 'PROPOSAL_STATUS_PASSED'
    Rejected = 'PROPOSAL_STATUS_REJECTED'
    Failed = 'PROPOSAL_STATUS_FAILED'


# Functions


def generate_endpoint_account(address: str) -> str:
    """Generate endpoint for account details."""
    return f'/cosmos/auth/v1beta1/accounts/{address}'


def generate_endpoint_balances(address: str) -> str:
    """Generate endpoint for account balances."""
    return f'/cosmos/bank/v1beta1/balances/{address}'


def generate_endpoint_broadcast() -> str:
    """Generate endpoint for broadcasting."""
    return '/cosmos/tx/v1beta1/txs'


def generate_post_body_broadcast(
    tx_raw: TxToSend,
    broadcast_mode: BroadcastMode = BroadcastMode.Sync,
) -> str:
    """Generate POST request body for broadcasting."""
    return json.dumps(
        {
            'tx_bytes': [str(tx_raw['message']['serialize_binary']())],
            'mode': broadcast_mode,
        }
    )


def generate_endpoint_proposals() -> str:
    """Generate proposals endpoint.

    Note:
      This returns all the proposals.
    """
    # TODO: add pagination to the request
    return '/cosmos/gov/v1beta1/proposals'


def generate_endpoint_claims_record(address: str) -> str:
    """Generate endpoint for record claims."""
    return f'/evmos/claims/v1/claims_records/{address}'


def generate_endpoint_proposal_tally(proposal_id: str) -> str:
    """Generate endpoint for tally proposals."""
    return f'/cosmos/gov/v1beta1/proposals/{proposal_id}/tally'


def generate_endpoint_ibc_channels() -> str:
    """Get all the IBC channels."""
    return '/ibc/core/channel/v1/channels'


def generate_endpoint_distribution_rewards_by_address(address: str) -> str:
    """Generate endpoint for rewards distribution."""
    return f'/cosmos/distribution/v1beta1/delegators/${address}/rewards'


def generate_endpoint_get_validators() -> str:
    """Generate endpoint for validators list."""
    return '/cosmos/staking/v1beta1/validators'


def generate_endpoint_get_delegations(delegator_address: str) -> str:
    """Generate endpoint for delegation."""
    return f'/cosmos/staking/v1beta1/delegations/${delegator_address}'


def generate_endpoint_get_undelegations(delegator_address: str) -> str:
    """Generate endpoint for undelegation."""
    return (
        f'/cosmos/staking/v1beta1/delegators/${delegator_address}/unbonding_delegations'
    )


_WithAtType = TypedDict('_WithAtType', {'@type': str})


# account.ts


class _PubkeyAccountResponse(_WithAtType):
    key: str


class _BaseAccountResponse(TypedDict):
    address: str
    pub_key: NotRequired[_PubkeyAccountResponse]
    account_number: str
    sequence: str


class _AccountResponse(_WithAtType):
    base_account: _BaseAccountResponse
    code_hash: str


class AccountResponse(TypedDict):
    """Response of account endpoint."""

    account: _AccountResponse


# balance.ts


class _PaginationResponse(TypedDict):
    next_key: str
    total: int


class BalancesResponse(TypedDict):
    """Response of balance endpoint."""

    balances: Sequence[Coin]
    pagination: _PaginationResponse


# broadcast.ts


class _MessageToSend(TypedDict):
    serialize_binary: Callable[[], Sequence[int]]


class TxToSend(TypedDict):
    """Transaction interface to broadcast."""

    message: _MessageToSend
    path: str


class BroadcastPostBody(TypedDict):
    """Body of POST request for transaction broadcasting."""

    tx_bytes: Sequence[int]
    mode: str


# claims.ts


class Claim(TypedDict):
    """Single claim record."""

    action: str
    completed: bool
    claimable_amount: str


class ClaimsRecordResponse(TypedDict):
    """Response of claims endpoint."""

    initial_claimable_amount: int
    claims: Sequence[Claim]


# coin.ts
class Coin(TypedDict):
    """Coin structure."""

    denom: str
    amount: str


# gov.ts


class _ProposalContent(_WithAtType):
    title: str
    description: str


class TallyResults(TypedDict):
    """Tally results for a single proposal."""

    yes: str
    abstain: str
    no: str
    no_with_veto: str


class Proposal(TypedDict):
    """Single proposal."""

    proposal_id: str
    content: _ProposalContent
    status: str
    final_tally_result: TallyResults
    submit_time: str
    deposit_end_time: str
    total_deposit: Sequence[Coin]
    voting_start_time: str
    voting_end_time: str


class ProposalsResponse(TypedDict):
    """Response type of proposals endpoint."""

    proposals: Sequence[Proposal]
    pagination: _PaginationResponse


class TallyResponse(TypedDict):
    """Response type of tally endpoint."""

    tally: TallyResults


# ibc.ts


class CounterParty(TypedDict):
    """IBC counterparty."""

    port_id: str
    channel_id: str


class Channel(TypedDict):
    """IBC channel."""

    state: str
    ordering: str
    counterparty: CounterParty
    connection_hops: Sequence[str]
    version: str
    port_id: str
    channel_id: str


class _ChannelsResponseHeight(TypedDict):
    revision_number: str
    revision_height: str


class ChannelsResponse(TypedDict):
    """Response type of channels endpoint."""

    channels: Sequence[Channel]
    pagination: _PaginationResponse
    height: _ChannelsResponseHeight


# staking.ts


class Reward(TypedDict):
    """Reward."""

    validator_address: str
    reward: Sequence[Coin]


class DistributionRewardsResponse(TypedDict):
    """Response type of rewards distribution endpoint."""

    rewards: Sequence[Reward]
    total: Sequence[Coin]


class _ValidatorCommissionRates(TypedDict):
    max_change_rate: str
    max_rate: str
    rate: str


class _ValidatorCommission(TypedDict):
    commission_rates: _ValidatorCommissionRates
    update_time: str


class _ValidatorDescription(TypedDict):
    details: str
    identity: str
    moniker: str
    security_contact: str
    website: str


class Validator(TypedDict):
    """Validator definition."""

    commission: _ValidatorCommission
    consensus_pubkey: _PubkeyAccountResponse
    delegator_shares: str
    description: _ValidatorDescription
    jailed: bool
    min_self_delegation: str
    operator_address: str
    status: str
    tokens: str
    unbonding_height: str
    unbonding_time: str


class GetValidatorsResponse(TypedDict):
    """Response type of validators endpoint."""

    validators: Sequence[Validator]
    pagination: _PaginationResponse


class _DelegationParams(TypedDict):
    delegator_address: str
    shares: str
    validator_address: str


class DelegationResponse(TypedDict):
    """Single delegation item received from delegation endpoint."""

    balance: Coin
    delegation: _DelegationParams


class GetDelegationsResponse(TypedDict):
    """Response type of delegation endpoint."""

    delegation_responses: Sequence[DelegationResponse]
    pagination: _PaginationResponse


class _UndelegationEntry(TypedDict):
    creation_height: str
    completion_time: str
    initial_balance: str
    balance: str


class UndelegationResponse(TypedDict):
    """Single undelegation item received from delegation endpoint."""

    delegator_address: str
    validator_address: str
    entries: Sequence[_UndelegationEntry]


class GetUndelegationsResponse(TypedDict):
    """Response type of undelegation endpoint."""

    unbonding_responses: Sequence[UndelegationResponse]
    pagination: _PaginationResponse
