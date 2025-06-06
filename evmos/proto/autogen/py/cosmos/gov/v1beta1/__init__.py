# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/gov/v1beta1/genesis.proto, cosmos/gov/v1beta1/gov.proto, cosmos/gov/v1beta1/query.proto, cosmos/gov/v1beta1/tx.proto
# plugin: python-betterproto
# This file has been @generated
import warnings
from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...base import v1beta1 as __base_v1_beta1__
from ...base.query import v1beta1 as __base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class VoteOption(betterproto.Enum):
    """VoteOption enumerates the valid vote options for a given governance proposal."""

    VOTE_OPTION_UNSPECIFIED = 0
    """VOTE_OPTION_UNSPECIFIED defines a no-op vote option."""

    VOTE_OPTION_YES = 1
    """VOTE_OPTION_YES defines a yes vote option."""

    VOTE_OPTION_ABSTAIN = 2
    """VOTE_OPTION_ABSTAIN defines an abstain vote option."""

    VOTE_OPTION_NO = 3
    """VOTE_OPTION_NO defines a no vote option."""

    VOTE_OPTION_NO_WITH_VETO = 4
    """VOTE_OPTION_NO_WITH_VETO defines a no with veto vote option."""


class ProposalStatus(betterproto.Enum):
    """ProposalStatus enumerates the valid statuses of a proposal."""

    PROPOSAL_STATUS_UNSPECIFIED = 0
    """PROPOSAL_STATUS_UNSPECIFIED defines the default proposal status."""

    PROPOSAL_STATUS_DEPOSIT_PERIOD = 1
    """
    PROPOSAL_STATUS_DEPOSIT_PERIOD defines a proposal status during the deposit
    period.
    """

    PROPOSAL_STATUS_VOTING_PERIOD = 2
    """
    PROPOSAL_STATUS_VOTING_PERIOD defines a proposal status during the voting
    period.
    """

    PROPOSAL_STATUS_PASSED = 3
    """
    PROPOSAL_STATUS_PASSED defines a proposal status of a proposal that has
    passed.
    """

    PROPOSAL_STATUS_REJECTED = 4
    """
    PROPOSAL_STATUS_REJECTED defines a proposal status of a proposal that has
    been rejected.
    """

    PROPOSAL_STATUS_FAILED = 5
    """
    PROPOSAL_STATUS_FAILED defines a proposal status of a proposal that has
    failed.
    """


@dataclass(eq=False, repr=False)
class WeightedVoteOption(betterproto.Message):
    """
    WeightedVoteOption defines a unit of vote for vote split.
    Since: cosmos-sdk 0.43
    """

    option: "VoteOption" = betterproto.enum_field(1)
    """
    option defines the valid vote options, it must not contain duplicate vote options.
    """

    weight: str = betterproto.string_field(2)
    """weight is the vote weight associated with the vote option."""


@dataclass(eq=False, repr=False)
class TextProposal(betterproto.Message):
    """
    TextProposal defines a standard text proposal whose changes need to be
    manually updated in case of approval.
    """

    title: str = betterproto.string_field(1)
    """title of the proposal."""

    description: str = betterproto.string_field(2)
    """description associated with the proposal."""


@dataclass(eq=False, repr=False)
class Deposit(betterproto.Message):
    """
    Deposit defines an amount deposited by an account address to an active
    proposal.
    """

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    depositor: str = betterproto.string_field(2)
    """depositor defines the deposit addresses from the proposals."""

    amount: List["__base_v1_beta1__.Coin"] = betterproto.message_field(3)
    """amount to be deposited by depositor."""


@dataclass(eq=False, repr=False)
class Proposal(betterproto.Message):
    """Proposal defines the core field members of a governance proposal."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    content: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)
    """content is the proposal's content."""

    status: "ProposalStatus" = betterproto.enum_field(3)
    """status defines the proposal status."""

    final_tally_result: "TallyResult" = betterproto.message_field(4)
    """
    final_tally_result is the final tally result of the proposal. When
    querying a proposal via gRPC, this field is not populated until the
    proposal's voting period has ended.
    """

    submit_time: datetime = betterproto.message_field(5)
    """submit_time is the time of proposal submission."""

    deposit_end_time: datetime = betterproto.message_field(6)
    """deposit_end_time is the end time for deposition."""

    total_deposit: List["__base_v1_beta1__.Coin"] = betterproto.message_field(7)
    """total_deposit is the total deposit on the proposal."""

    voting_start_time: datetime = betterproto.message_field(8)
    """voting_start_time is the starting time to vote on a proposal."""

    voting_end_time: datetime = betterproto.message_field(9)
    """voting_end_time is the end time of voting on a proposal."""


@dataclass(eq=False, repr=False)
class TallyResult(betterproto.Message):
    """TallyResult defines a standard tally for a governance proposal."""

    yes: str = betterproto.string_field(1)
    """yes is the number of yes votes on a proposal."""

    abstain: str = betterproto.string_field(2)
    """abstain is the number of abstain votes on a proposal."""

    no: str = betterproto.string_field(3)
    """no is the number of no votes on a proposal."""

    no_with_veto: str = betterproto.string_field(4)
    """no_with_veto is the number of no with veto votes on a proposal."""


@dataclass(eq=False, repr=False)
class Vote(betterproto.Message):
    """
    Vote defines a vote on a governance proposal.
    A Vote consists of a proposal ID, the voter, and the vote option.
    """

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    voter: str = betterproto.string_field(2)
    """voter is the voter address of the proposal."""

    option: "VoteOption" = betterproto.enum_field(3)
    """
    Deprecated: Prefer to use `options` instead. This field is set in queries
    if and only if `len(options) == 1` and that option has weight 1. In all
    other cases, this field will default to VOTE_OPTION_UNSPECIFIED.
    """

    options: List["WeightedVoteOption"] = betterproto.message_field(4)
    """
    options is the weighted vote options.
    Since: cosmos-sdk 0.43
    """

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.is_set("option"):
            warnings.warn("Vote.option is deprecated", DeprecationWarning)


@dataclass(eq=False, repr=False)
class DepositParams(betterproto.Message):
    """DepositParams defines the params for deposits on governance proposals."""

    min_deposit: List["__base_v1_beta1__.Coin"] = betterproto.message_field(1)
    """Minimum deposit for a proposal to enter voting period."""

    max_deposit_period: timedelta = betterproto.message_field(2)
    """
    Maximum period for Atom holders to deposit on a proposal. Initial value: 2
    months.
    """


@dataclass(eq=False, repr=False)
class VotingParams(betterproto.Message):
    """VotingParams defines the params for voting on governance proposals."""

    voting_period: timedelta = betterproto.message_field(1)
    """Duration of the voting period."""


@dataclass(eq=False, repr=False)
class TallyParams(betterproto.Message):
    """TallyParams defines the params for tallying votes on governance proposals."""

    quorum: bytes = betterproto.bytes_field(1)
    """
    Minimum percentage of total stake needed to vote for a result to be
    considered valid.
    """

    threshold: bytes = betterproto.bytes_field(2)
    """Minimum proportion of Yes votes for proposal to pass. Default value: 0.5."""

    veto_threshold: bytes = betterproto.bytes_field(3)
    """
    Minimum value of Veto votes to Total votes ratio for proposal to be
    vetoed. Default value: 1/3.
    """


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the gov module's genesis state."""

    starting_proposal_id: int = betterproto.uint64_field(1)
    """starting_proposal_id is the ID of the starting proposal."""

    deposits: List["Deposit"] = betterproto.message_field(2)
    """deposits defines all the deposits present at genesis."""

    votes: List["Vote"] = betterproto.message_field(3)
    """votes defines all the votes present at genesis."""

    proposals: List["Proposal"] = betterproto.message_field(4)
    """proposals defines all the proposals present at genesis."""

    deposit_params: "DepositParams" = betterproto.message_field(5)
    """deposit_params defines all the parameters related to deposit."""

    voting_params: "VotingParams" = betterproto.message_field(6)
    """voting_params defines all the parameters related to voting."""

    tally_params: "TallyParams" = betterproto.message_field(7)
    """tally_params defines all the parameters related to tally."""


@dataclass(eq=False, repr=False)
class QueryProposalRequest(betterproto.Message):
    """QueryProposalRequest is the request type for the Query/Proposal RPC method."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""


@dataclass(eq=False, repr=False)
class QueryProposalResponse(betterproto.Message):
    """QueryProposalResponse is the response type for the Query/Proposal RPC method."""

    proposal: "Proposal" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryProposalsRequest(betterproto.Message):
    """QueryProposalsRequest is the request type for the Query/Proposals RPC method."""

    proposal_status: "ProposalStatus" = betterproto.enum_field(1)
    """proposal_status defines the status of the proposals."""

    voter: str = betterproto.string_field(2)
    """voter defines the voter address for the proposals."""

    depositor: str = betterproto.string_field(3)
    """depositor defines the deposit addresses from the proposals."""

    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(4)
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryProposalsResponse(betterproto.Message):
    """
    QueryProposalsResponse is the response type for the Query/Proposals RPC
    method.
    """

    proposals: List["Proposal"] = betterproto.message_field(1)
    """proposals defines all the requested governance proposals."""

    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryVoteRequest(betterproto.Message):
    """QueryVoteRequest is the request type for the Query/Vote RPC method."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    voter: str = betterproto.string_field(2)
    """voter defines the voter address for the proposals."""


@dataclass(eq=False, repr=False)
class QueryVoteResponse(betterproto.Message):
    """QueryVoteResponse is the response type for the Query/Vote RPC method."""

    vote: "Vote" = betterproto.message_field(1)
    """vote defines the queried vote."""


@dataclass(eq=False, repr=False)
class QueryVotesRequest(betterproto.Message):
    """QueryVotesRequest is the request type for the Query/Votes RPC method."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(2)
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryVotesResponse(betterproto.Message):
    """QueryVotesResponse is the response type for the Query/Votes RPC method."""

    votes: List["Vote"] = betterproto.message_field(1)
    """votes defines the queried votes."""

    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""

    params_type: str = betterproto.string_field(1)
    """
    params_type defines which parameters to query for, can be one of "voting",
    "tallying" or "deposit".
    """


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""

    voting_params: "VotingParams" = betterproto.message_field(1)
    """voting_params defines the parameters related to voting."""

    deposit_params: "DepositParams" = betterproto.message_field(2)
    """deposit_params defines the parameters related to deposit."""

    tally_params: "TallyParams" = betterproto.message_field(3)
    """tally_params defines the parameters related to tally."""


@dataclass(eq=False, repr=False)
class QueryDepositRequest(betterproto.Message):
    """QueryDepositRequest is the request type for the Query/Deposit RPC method."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    depositor: str = betterproto.string_field(2)
    """depositor defines the deposit addresses from the proposals."""


@dataclass(eq=False, repr=False)
class QueryDepositResponse(betterproto.Message):
    """QueryDepositResponse is the response type for the Query/Deposit RPC method."""

    deposit: "Deposit" = betterproto.message_field(1)
    """deposit defines the requested deposit."""


@dataclass(eq=False, repr=False)
class QueryDepositsRequest(betterproto.Message):
    """QueryDepositsRequest is the request type for the Query/Deposits RPC method."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(2)
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryDepositsResponse(betterproto.Message):
    """QueryDepositsResponse is the response type for the Query/Deposits RPC method."""

    deposits: List["Deposit"] = betterproto.message_field(1)
    """deposits defines the requested deposits."""

    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryTallyResultRequest(betterproto.Message):
    """QueryTallyResultRequest is the request type for the Query/Tally RPC method."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""


@dataclass(eq=False, repr=False)
class QueryTallyResultResponse(betterproto.Message):
    """QueryTallyResultResponse is the response type for the Query/Tally RPC method."""

    tally: "TallyResult" = betterproto.message_field(1)
    """tally defines the requested tally."""


@dataclass(eq=False, repr=False)
class MsgSubmitProposal(betterproto.Message):
    """
    MsgSubmitProposal defines an sdk.Msg type that supports submitting arbitrary
    proposal Content.
    """

    content: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)
    """content is the proposal's content."""

    initial_deposit: List["__base_v1_beta1__.Coin"] = betterproto.message_field(2)
    """
    initial_deposit is the deposit value that must be paid at proposal submission.
    """

    proposer: str = betterproto.string_field(3)
    """proposer is the account address of the proposer."""


@dataclass(eq=False, repr=False)
class MsgSubmitProposalResponse(betterproto.Message):
    """MsgSubmitProposalResponse defines the Msg/SubmitProposal response type."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""


@dataclass(eq=False, repr=False)
class MsgVote(betterproto.Message):
    """MsgVote defines a message to cast a vote."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    voter: str = betterproto.string_field(2)
    """voter is the voter address for the proposal."""

    option: "VoteOption" = betterproto.enum_field(3)
    """option defines the vote option."""


@dataclass(eq=False, repr=False)
class MsgVoteResponse(betterproto.Message):
    """MsgVoteResponse defines the Msg/Vote response type."""

    pass


@dataclass(eq=False, repr=False)
class MsgVoteWeighted(betterproto.Message):
    """
    MsgVoteWeighted defines a message to cast a vote.
    Since: cosmos-sdk 0.43
    """

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    voter: str = betterproto.string_field(2)
    """voter is the voter address for the proposal."""

    options: List["WeightedVoteOption"] = betterproto.message_field(3)
    """options defines the weighted vote options."""


@dataclass(eq=False, repr=False)
class MsgVoteWeightedResponse(betterproto.Message):
    """
    MsgVoteWeightedResponse defines the Msg/VoteWeighted response type.
    Since: cosmos-sdk 0.43
    """

    pass


@dataclass(eq=False, repr=False)
class MsgDeposit(betterproto.Message):
    """MsgDeposit defines a message to submit a deposit to an existing proposal."""

    proposal_id: int = betterproto.uint64_field(1)
    """proposal_id defines the unique id of the proposal."""

    depositor: str = betterproto.string_field(2)
    """depositor defines the deposit addresses from the proposals."""

    amount: List["__base_v1_beta1__.Coin"] = betterproto.message_field(3)
    """amount to be deposited by depositor."""


@dataclass(eq=False, repr=False)
class MsgDepositResponse(betterproto.Message):
    """MsgDepositResponse defines the Msg/Deposit response type."""

    pass


class QueryStub(betterproto.ServiceStub):
    async def proposal(
        self,
        query_proposal_request: "QueryProposalRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryProposalResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Query/Proposal",
            query_proposal_request,
            QueryProposalResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def proposals(
        self,
        query_proposals_request: "QueryProposalsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryProposalsResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Query/Proposals",
            query_proposals_request,
            QueryProposalsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def vote(
        self,
        query_vote_request: "QueryVoteRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryVoteResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Query/Vote",
            query_vote_request,
            QueryVoteResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def votes(
        self,
        query_votes_request: "QueryVotesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryVotesResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Query/Votes",
            query_votes_request,
            QueryVotesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def deposit(
        self,
        query_deposit_request: "QueryDepositRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryDepositResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Query/Deposit",
            query_deposit_request,
            QueryDepositResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def deposits(
        self,
        query_deposits_request: "QueryDepositsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryDepositsResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Query/Deposits",
            query_deposits_request,
            QueryDepositsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def tally_result(
        self,
        query_tally_result_request: "QueryTallyResultRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryTallyResultResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Query/TallyResult",
            query_tally_result_request,
            QueryTallyResultResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def submit_proposal(
        self,
        msg_submit_proposal: "MsgSubmitProposal",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgSubmitProposalResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Msg/SubmitProposal",
            msg_submit_proposal,
            MsgSubmitProposalResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def vote(
        self,
        msg_vote: "MsgVote",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgVoteResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Msg/Vote",
            msg_vote,
            MsgVoteResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def vote_weighted(
        self,
        msg_vote_weighted: "MsgVoteWeighted",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgVoteWeightedResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Msg/VoteWeighted",
            msg_vote_weighted,
            MsgVoteWeightedResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def deposit(
        self,
        msg_deposit: "MsgDeposit",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgDepositResponse":
        return await self._unary_unary(
            "/cosmos.gov.v1beta1.Msg/Deposit",
            msg_deposit,
            MsgDepositResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def proposal(
        self, query_proposal_request: "QueryProposalRequest"
    ) -> "QueryProposalResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def proposals(
        self, query_proposals_request: "QueryProposalsRequest"
    ) -> "QueryProposalsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def vote(self, query_vote_request: "QueryVoteRequest") -> "QueryVoteResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def votes(
        self, query_votes_request: "QueryVotesRequest"
    ) -> "QueryVotesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(
        self, query_params_request: "QueryParamsRequest"
    ) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def deposit(
        self, query_deposit_request: "QueryDepositRequest"
    ) -> "QueryDepositResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def deposits(
        self, query_deposits_request: "QueryDepositsRequest"
    ) -> "QueryDepositsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def tally_result(
        self, query_tally_result_request: "QueryTallyResultRequest"
    ) -> "QueryTallyResultResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_proposal(
        self,
        stream: "grpclib.server.Stream[QueryProposalRequest, QueryProposalResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.proposal(request)
        await stream.send_message(response)

    async def __rpc_proposals(
        self,
        stream: "grpclib.server.Stream[QueryProposalsRequest, QueryProposalsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.proposals(request)
        await stream.send_message(response)

    async def __rpc_vote(
        self, stream: "grpclib.server.Stream[QueryVoteRequest, QueryVoteResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.vote(request)
        await stream.send_message(response)

    async def __rpc_votes(
        self, stream: "grpclib.server.Stream[QueryVotesRequest, QueryVotesResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.votes(request)
        await stream.send_message(response)

    async def __rpc_params(
        self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_deposit(
        self, stream: "grpclib.server.Stream[QueryDepositRequest, QueryDepositResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.deposit(request)
        await stream.send_message(response)

    async def __rpc_deposits(
        self,
        stream: "grpclib.server.Stream[QueryDepositsRequest, QueryDepositsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.deposits(request)
        await stream.send_message(response)

    async def __rpc_tally_result(
        self,
        stream: "grpclib.server.Stream[QueryTallyResultRequest, QueryTallyResultResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.tally_result(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.gov.v1beta1.Query/Proposal": grpclib.const.Handler(
                self.__rpc_proposal,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryProposalRequest,
                QueryProposalResponse,
            ),
            "/cosmos.gov.v1beta1.Query/Proposals": grpclib.const.Handler(
                self.__rpc_proposals,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryProposalsRequest,
                QueryProposalsResponse,
            ),
            "/cosmos.gov.v1beta1.Query/Vote": grpclib.const.Handler(
                self.__rpc_vote,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryVoteRequest,
                QueryVoteResponse,
            ),
            "/cosmos.gov.v1beta1.Query/Votes": grpclib.const.Handler(
                self.__rpc_votes,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryVotesRequest,
                QueryVotesResponse,
            ),
            "/cosmos.gov.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/cosmos.gov.v1beta1.Query/Deposit": grpclib.const.Handler(
                self.__rpc_deposit,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDepositRequest,
                QueryDepositResponse,
            ),
            "/cosmos.gov.v1beta1.Query/Deposits": grpclib.const.Handler(
                self.__rpc_deposits,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDepositsRequest,
                QueryDepositsResponse,
            ),
            "/cosmos.gov.v1beta1.Query/TallyResult": grpclib.const.Handler(
                self.__rpc_tally_result,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTallyResultRequest,
                QueryTallyResultResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def submit_proposal(
        self, msg_submit_proposal: "MsgSubmitProposal"
    ) -> "MsgSubmitProposalResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def vote(self, msg_vote: "MsgVote") -> "MsgVoteResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def vote_weighted(
        self, msg_vote_weighted: "MsgVoteWeighted"
    ) -> "MsgVoteWeightedResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def deposit(self, msg_deposit: "MsgDeposit") -> "MsgDepositResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_submit_proposal(
        self,
        stream: "grpclib.server.Stream[MsgSubmitProposal, MsgSubmitProposalResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.submit_proposal(request)
        await stream.send_message(response)

    async def __rpc_vote(
        self, stream: "grpclib.server.Stream[MsgVote, MsgVoteResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.vote(request)
        await stream.send_message(response)

    async def __rpc_vote_weighted(
        self, stream: "grpclib.server.Stream[MsgVoteWeighted, MsgVoteWeightedResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.vote_weighted(request)
        await stream.send_message(response)

    async def __rpc_deposit(
        self, stream: "grpclib.server.Stream[MsgDeposit, MsgDepositResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.deposit(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.gov.v1beta1.Msg/SubmitProposal": grpclib.const.Handler(
                self.__rpc_submit_proposal,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSubmitProposal,
                MsgSubmitProposalResponse,
            ),
            "/cosmos.gov.v1beta1.Msg/Vote": grpclib.const.Handler(
                self.__rpc_vote,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgVote,
                MsgVoteResponse,
            ),
            "/cosmos.gov.v1beta1.Msg/VoteWeighted": grpclib.const.Handler(
                self.__rpc_vote_weighted,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgVoteWeighted,
                MsgVoteWeightedResponse,
            ),
            "/cosmos.gov.v1beta1.Msg/Deposit": grpclib.const.Handler(
                self.__rpc_deposit,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgDeposit,
                MsgDepositResponse,
            ),
        }
