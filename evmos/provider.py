from __future__ import annotations

from enum import Enum
from typing import Sequence, TypedDict

from typing_extensions import NotRequired

# Enums


class BroadcastMode(str, Enum):
    """Broadcasting mode."""

    UNSPECIFIED = 'BROADCAST_MODE_UNSPECIFIED'
    """Broadcasting mode unset."""
    BLOCK = 'BROADCAST_MODE_BLOCK'
    """Broadcasting mode - block."""
    SYNC = 'BROADCAST_MODE_SYNC'
    """Broadcasting mode - synchronous."""
    ASYNC = 'BROADCAST_MODE_ASYNC'
    """Broadcasting mode - asynchronous."""


class ProposalStatus(str, Enum):
    """Proposal status."""

    UNSPECIFIED = 'PROPOSAL_STATUS_UNSPECIFIED'
    """Proposal status unset."""
    DEPOSIT = 'PROPOSAL_STATUS_DEPOSIT_PERIOD'
    """Proposal during deposit period."""
    VOTING = 'PROPOSAL_STATUS_VOTING_PERIOD'
    """Proposal during voting period."""
    PASSED = 'PROPOSAL_STATUS_PASSED'
    """Proposal passed."""
    REJECTED = 'PROPOSAL_STATUS_REJECTED'
    """Proposal rejected."""
    FAILED = 'PROPOSAL_STATUS_FAILED'
    """Proposal failed."""


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


# account.ts


class PubkeyAccountResponse(TypedDict):
    """Response with account public key.

    Also has "@type" key with corresponding `str` value.
    """

    key: str
    """Account public key (base64 encoded)."""


class BaseAccountResponse(TypedDict):
    """``base_account`` response field.

    This is similar to :class:`evmos.transactions.common.Sender`.
    """

    address: str
    """Account address (bech32)."""
    pub_key: NotRequired[PubkeyAccountResponse]
    """Account public key as dict."""
    account_number: str
    """Account internal number."""
    sequence: str
    """Account nonce - number of previously sent transactions."""


class AccountResponseBody(TypedDict):
    """Account body from response.

    Also has "@type" key with corresponding `str` value.
    """

    base_account: BaseAccountResponse
    """Account response content."""
    code_hash: str
    """Response status."""


class AccountResponse(TypedDict):
    """Full response of account endpoint."""

    account: AccountResponseBody
    """Account full response content, wrapped in another dict."""


# balance.ts


class PaginationResponse(TypedDict):
    """Pagination response part."""

    next_key: str
    """Next key to fetch."""
    total: int
    """Total amount of records."""


class BalancesResponse(TypedDict):
    """Response of balance endpoint."""

    balances: Sequence[Coin]
    """All coin balances of account."""
    pagination: PaginationResponse
    """Pagination part."""


# broadcast.ts


class BroadcastPostBody(TypedDict):
    """Body of POST request for transaction broadcasting."""

    tx_bytes: str
    """base64-encoded transaction bytes."""
    mode: str
    """Broadcasting mode."""


# claims.ts


class Claim(TypedDict):
    """Single claim record."""

    action: str
    """Claiming action."""
    completed: bool
    """Whether claim is completed."""
    claimable_amount: str
    """Amount to claim."""


class ClaimsRecordResponse(TypedDict):
    """Response of claims endpoint."""

    initial_claimable_amount: int
    """Amount available to claim before processing."""
    claims: Sequence[Claim]
    """All claims performed."""


# coin.ts


class Coin(TypedDict):
    """Coin structure."""

    denom: str
    """Coin denomination."""
    amount: str
    """Amount, as string (like '1000')."""


# gov.ts


class ProposalContent(TypedDict):
    """Proposal content.

    Also has "@type" key with corresponding `str` value.
    """

    title: str
    """Proposal title."""
    description: str
    """Proposal description."""


class TallyResults(TypedDict):
    """Tally results for a single proposal."""

    yes: str
    """Number of positive votes, as string (like '1234')."""
    abstain: str
    """Number of abstain votes, as string (like '1234')."""
    no: str
    """Number of negative votes, as string (like '1234')."""
    no_with_veto: str
    """Number of negative votes with veto, as string (like '1234')."""


class Proposal(TypedDict):
    """Single proposal."""

    proposal_id: str
    """Internal proposal ID."""
    content: ProposalContent
    """Proposal content."""
    status: str
    """Proposal status."""
    final_tally_result: TallyResults
    """Proposal final voting results."""
    submit_time: str
    """Proposal submission time, as timestamp str."""
    deposit_end_time: str
    """Proposal deposit end time, as timestamp str."""
    total_deposit: Sequence[Coin]
    """Proposal total deposit, as str number."""
    voting_start_time: str
    """Proposal voting start time, as timestamp str."""
    voting_end_time: str
    """Proposal voting end time, as timestamp str."""


class ProposalsResponse(TypedDict):
    """Response type of proposals endpoint."""

    proposals: Sequence[Proposal]
    """Response of proposals endpoint."""
    pagination: PaginationResponse
    """Pagination block."""


class TallyResponse(TypedDict):
    """Response type of tally endpoint."""

    tally: TallyResults
    """Results."""


# ibc.ts


class CounterParty(TypedDict):
    """IBC counterparty."""

    port_id: str
    """IBC port ID."""
    channel_id: str
    """IBC channel ID."""


class IBCChannel(TypedDict):
    """IBC channel."""

    state: str
    """IBC channel state."""
    ordering: str
    """IBC channel ordering."""
    counterparty: CounterParty
    """IBC channel counterparty."""
    connection_hops: Sequence[str]
    """IBC channel connection hops."""
    version: str
    """IBC channel version."""
    port_id: str
    """IBC channel port id."""
    channel_id: str
    """IBC channel id."""


class ChannelsResponseHeight(TypedDict):
    """``height`` field type of channels endpoint response."""

    revision_number: str
    """Current revision number."""
    revision_height: str
    """Current revision height."""


class ChannelsResponse(TypedDict):
    """Response type of channels endpoint."""

    channels: Sequence[IBCChannel]
    """Actual channels."""
    pagination: PaginationResponse
    """Pagination block."""
    height: ChannelsResponseHeight
    """Response height."""


# staking.ts


class Reward(TypedDict):
    """Reward."""

    validator_address: str
    """Validator address."""
    reward: Sequence[Coin]
    """Reward (in all coin types)."""


class DistributionRewardsResponse(TypedDict):
    """Response type of rewards distribution endpoint."""

    rewards: Sequence[Reward]
    """Reward (in all coin types)."""
    total: Sequence[Coin]
    """Total rewards (in all coin types)."""


class ValidatorCommissionRates(TypedDict):
    """Validator commission rates."""

    max_change_rate: str
    """Max change rate, number as str."""
    max_rate: str
    """Max overall rate, number as str."""
    rate: str
    """Rate, number as str."""


class ValidatorCommission(TypedDict):
    """Commission rates of validator."""

    commission_rates: ValidatorCommissionRates
    """Actual rates."""
    update_time: str
    """Last update time, as str timestamp."""


class ValidatorDescription(TypedDict):
    """Validator details."""

    details: str
    """Validator details."""
    identity: str
    """Validator identity."""
    moniker: str
    """Validator moniker."""
    security_contact: str
    """Validator security contact."""
    website: str
    """Validator website."""


class Validator(TypedDict):
    """Validator definition."""

    commission: ValidatorCommission
    """Validator commissions."""
    consensus_pubkey: PubkeyAccountResponse
    """Consensus public key."""
    delegator_shares: str
    """Total delegator shares."""
    description: ValidatorDescription
    """Description."""
    jailed: bool
    """Whether validator is jailed."""
    min_self_delegation: str
    """Minimal self delegation amount, int as str."""
    operator_address: str
    """Operator address."""
    status: str
    """Validator status."""
    tokens: str
    """Validator tokens."""
    unbonding_height: str
    """Validator unbounding height."""
    unbonding_time: str
    """Validator unbounding time."""


class GetValidatorsResponse(TypedDict):
    """Response type of validators endpoint."""

    validators: Sequence[Validator]
    """All validators present."""
    pagination: PaginationResponse
    """Pagination block."""


class DelegationParams(TypedDict):
    """Parameters of delegation deal."""

    delegator_address: str
    """Address of delegator."""
    shares: str
    """Total delegator shares."""
    validator_address: str
    """Validator address."""


class DelegationResponse(TypedDict):
    """Single delegation item received from delegation endpoint."""

    balance: Coin
    """Balance of delegated coin."""
    delegation: DelegationParams
    """Deal options."""


class GetDelegationsResponse(TypedDict):
    """Response type of delegation endpoint."""

    delegation_responses: Sequence[DelegationResponse]
    """All response blocks."""
    pagination: PaginationResponse
    """Pagination block."""


class UndelegationEntry(TypedDict):
    """Undelegation entry."""

    creation_height: str
    """Height of block when this item was created."""
    completion_time: str
    """Completion time."""
    initial_balance: str
    """Initial owner balance."""
    balance: str
    """Resulting owner balance."""


class UndelegationResponse(TypedDict):
    """Single undelegation item received from delegation endpoint."""

    delegator_address: str
    """Delegator address."""
    validator_address: str
    """Validator address."""
    entries: Sequence[UndelegationEntry]
    """Actual undelegation descriptions."""


class GetUndelegationsResponse(TypedDict):
    """Response type of undelegation endpoint."""

    unbonding_responses: Sequence[UndelegationResponse]
    """All responses as a sequence."""
    pagination: PaginationResponse
    """Pagination block."""
