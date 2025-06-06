# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/feegrant/v1beta1/feegrant.proto, cosmos/feegrant/v1beta1/genesis.proto, cosmos/feegrant/v1beta1/query.proto, cosmos/feegrant/v1beta1/tx.proto
# plugin: python-betterproto
# This file has been @generated

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


@dataclass(eq=False, repr=False)
class BasicAllowance(betterproto.Message):
    """
    BasicAllowance implements Allowance with a one-time grant of coins
    that optionally expires. The grantee can use up to SpendLimit to cover fees.
    """

    spend_limit: List["__base_v1_beta1__.Coin"] = betterproto.message_field(1)
    """
    spend_limit specifies the maximum amount of coins that can be spent
    by this allowance and will be updated as coins are spent. If it is
    empty, there is no spend limit and any amount of coins can be spent.
    """

    expiration: datetime = betterproto.message_field(2)
    """expiration specifies an optional time when this allowance expires"""


@dataclass(eq=False, repr=False)
class PeriodicAllowance(betterproto.Message):
    """
    PeriodicAllowance extends Allowance to allow for both a maximum cap,
    as well as a limit per time period.
    """

    basic: "BasicAllowance" = betterproto.message_field(1)
    """basic specifies a struct of `BasicAllowance`"""

    period: timedelta = betterproto.message_field(2)
    """
    period specifies the time duration in which period_spend_limit coins can
    be spent before that allowance is reset
    """

    period_spend_limit: List["__base_v1_beta1__.Coin"] = betterproto.message_field(3)
    """
    period_spend_limit specifies the maximum number of coins that can be spent
    in the period
    """

    period_can_spend: List["__base_v1_beta1__.Coin"] = betterproto.message_field(4)
    """
    period_can_spend is the number of coins left to be spent before the period_reset
    time
    """

    period_reset: datetime = betterproto.message_field(5)
    """
    period_reset is the time at which this period resets and a new one begins,
    it is calculated from the start time of the first transaction after the
    last period ended
    """


@dataclass(eq=False, repr=False)
class AllowedMsgAllowance(betterproto.Message):
    """AllowedMsgAllowance creates allowance only for specified message types."""

    allowance: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)
    """allowance can be any of basic and periodic fee allowance."""

    allowed_messages: List[str] = betterproto.string_field(2)
    """allowed_messages are the messages for which the grantee has the access."""


@dataclass(eq=False, repr=False)
class Grant(betterproto.Message):
    """Grant is stored in the KVStore to record a grant with full context"""

    granter: str = betterproto.string_field(1)
    """granter is the address of the user granting an allowance of their funds."""

    grantee: str = betterproto.string_field(2)
    """
    grantee is the address of the user being granted an allowance of another user's
    funds.
    """

    allowance: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(3)
    """allowance can be any of basic, periodic, allowed fee allowance."""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState contains a set of fee allowances, persisted from the store"""

    allowances: List["Grant"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAllowanceRequest(betterproto.Message):
    """QueryAllowanceRequest is the request type for the Query/Allowance RPC method."""

    granter: str = betterproto.string_field(1)
    """granter is the address of the user granting an allowance of their funds."""

    grantee: str = betterproto.string_field(2)
    """
    grantee is the address of the user being granted an allowance of another user's
    funds.
    """


@dataclass(eq=False, repr=False)
class QueryAllowanceResponse(betterproto.Message):
    """
    QueryAllowanceResponse is the response type for the Query/Allowance RPC method.
    """

    allowance: "Grant" = betterproto.message_field(1)
    """allowance is a allowance granted for grantee by granter."""


@dataclass(eq=False, repr=False)
class QueryAllowancesRequest(betterproto.Message):
    """
    QueryAllowancesRequest is the request type for the Query/Allowances RPC method.
    """

    grantee: str = betterproto.string_field(1)
    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(2)
    """pagination defines an pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryAllowancesResponse(betterproto.Message):
    """
    QueryAllowancesResponse is the response type for the Query/Allowances RPC method.
    """

    allowances: List["Grant"] = betterproto.message_field(1)
    """allowances are allowance's granted for grantee by granter."""

    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)
    """pagination defines an pagination for the response."""


@dataclass(eq=False, repr=False)
class QueryAllowancesByGranterRequest(betterproto.Message):
    """
    QueryAllowancesByGranterRequest is the request type for the
    Query/AllowancesByGranter RPC method.
    Since: cosmos-sdk 0.46
    """

    granter: str = betterproto.string_field(1)
    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(2)
    """pagination defines an pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryAllowancesByGranterResponse(betterproto.Message):
    """
    QueryAllowancesByGranterResponse is the response type for the
    Query/AllowancesByGranter RPC method.
    Since: cosmos-sdk 0.46
    """

    allowances: List["Grant"] = betterproto.message_field(1)
    """allowances that have been issued by the granter."""

    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)
    """pagination defines an pagination for the response."""


@dataclass(eq=False, repr=False)
class MsgGrantAllowance(betterproto.Message):
    """
    MsgGrantAllowance adds permission for Grantee to spend up to Allowance
    of fees from the account of Granter.
    """

    granter: str = betterproto.string_field(1)
    """granter is the address of the user granting an allowance of their funds."""

    grantee: str = betterproto.string_field(2)
    """
    grantee is the address of the user being granted an allowance of another user's
    funds.
    """

    allowance: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(3)
    """allowance can be any of basic, periodic, allowed fee allowance."""


@dataclass(eq=False, repr=False)
class MsgGrantAllowanceResponse(betterproto.Message):
    """
    MsgGrantAllowanceResponse defines the Msg/GrantAllowanceResponse response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgRevokeAllowance(betterproto.Message):
    """MsgRevokeAllowance removes any existing Allowance from Granter to Grantee."""

    granter: str = betterproto.string_field(1)
    """granter is the address of the user granting an allowance of their funds."""

    grantee: str = betterproto.string_field(2)
    """
    grantee is the address of the user being granted an allowance of another user's
    funds.
    """


@dataclass(eq=False, repr=False)
class MsgRevokeAllowanceResponse(betterproto.Message):
    """
    MsgRevokeAllowanceResponse defines the Msg/RevokeAllowanceResponse response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgPruneAllowances(betterproto.Message):
    """
    MsgPruneAllowances prunes expired fee allowances.
    Since cosmos-sdk 0.50
    """

    pruner: str = betterproto.string_field(1)
    """pruner is the address of the user pruning expired allowances."""


@dataclass(eq=False, repr=False)
class MsgPruneAllowancesResponse(betterproto.Message):
    """
    MsgPruneAllowancesResponse defines the Msg/PruneAllowancesResponse response type.
    Since cosmos-sdk 0.50
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def allowance(
        self,
        query_allowance_request: "QueryAllowanceRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryAllowanceResponse":
        return await self._unary_unary(
            "/cosmos.feegrant.v1beta1.Query/Allowance",
            query_allowance_request,
            QueryAllowanceResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def allowances(
        self,
        query_allowances_request: "QueryAllowancesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryAllowancesResponse":
        return await self._unary_unary(
            "/cosmos.feegrant.v1beta1.Query/Allowances",
            query_allowances_request,
            QueryAllowancesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def allowances_by_granter(
        self,
        query_allowances_by_granter_request: "QueryAllowancesByGranterRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryAllowancesByGranterResponse":
        return await self._unary_unary(
            "/cosmos.feegrant.v1beta1.Query/AllowancesByGranter",
            query_allowances_by_granter_request,
            QueryAllowancesByGranterResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def grant_allowance(
        self,
        msg_grant_allowance: "MsgGrantAllowance",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgGrantAllowanceResponse":
        return await self._unary_unary(
            "/cosmos.feegrant.v1beta1.Msg/GrantAllowance",
            msg_grant_allowance,
            MsgGrantAllowanceResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def revoke_allowance(
        self,
        msg_revoke_allowance: "MsgRevokeAllowance",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgRevokeAllowanceResponse":
        return await self._unary_unary(
            "/cosmos.feegrant.v1beta1.Msg/RevokeAllowance",
            msg_revoke_allowance,
            MsgRevokeAllowanceResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def prune_allowances(
        self,
        msg_prune_allowances: "MsgPruneAllowances",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgPruneAllowancesResponse":
        return await self._unary_unary(
            "/cosmos.feegrant.v1beta1.Msg/PruneAllowances",
            msg_prune_allowances,
            MsgPruneAllowancesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def allowance(
        self, query_allowance_request: "QueryAllowanceRequest"
    ) -> "QueryAllowanceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def allowances(
        self, query_allowances_request: "QueryAllowancesRequest"
    ) -> "QueryAllowancesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def allowances_by_granter(
        self, query_allowances_by_granter_request: "QueryAllowancesByGranterRequest"
    ) -> "QueryAllowancesByGranterResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_allowance(
        self,
        stream: "grpclib.server.Stream[QueryAllowanceRequest, QueryAllowanceResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.allowance(request)
        await stream.send_message(response)

    async def __rpc_allowances(
        self,
        stream: "grpclib.server.Stream[QueryAllowancesRequest, QueryAllowancesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.allowances(request)
        await stream.send_message(response)

    async def __rpc_allowances_by_granter(
        self,
        stream: "grpclib.server.Stream[QueryAllowancesByGranterRequest, QueryAllowancesByGranterResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.allowances_by_granter(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.feegrant.v1beta1.Query/Allowance": grpclib.const.Handler(
                self.__rpc_allowance,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllowanceRequest,
                QueryAllowanceResponse,
            ),
            "/cosmos.feegrant.v1beta1.Query/Allowances": grpclib.const.Handler(
                self.__rpc_allowances,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllowancesRequest,
                QueryAllowancesResponse,
            ),
            "/cosmos.feegrant.v1beta1.Query/AllowancesByGranter": grpclib.const.Handler(
                self.__rpc_allowances_by_granter,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllowancesByGranterRequest,
                QueryAllowancesByGranterResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def grant_allowance(
        self, msg_grant_allowance: "MsgGrantAllowance"
    ) -> "MsgGrantAllowanceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def revoke_allowance(
        self, msg_revoke_allowance: "MsgRevokeAllowance"
    ) -> "MsgRevokeAllowanceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def prune_allowances(
        self, msg_prune_allowances: "MsgPruneAllowances"
    ) -> "MsgPruneAllowancesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_grant_allowance(
        self,
        stream: "grpclib.server.Stream[MsgGrantAllowance, MsgGrantAllowanceResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.grant_allowance(request)
        await stream.send_message(response)

    async def __rpc_revoke_allowance(
        self,
        stream: "grpclib.server.Stream[MsgRevokeAllowance, MsgRevokeAllowanceResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.revoke_allowance(request)
        await stream.send_message(response)

    async def __rpc_prune_allowances(
        self,
        stream: "grpclib.server.Stream[MsgPruneAllowances, MsgPruneAllowancesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.prune_allowances(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.feegrant.v1beta1.Msg/GrantAllowance": grpclib.const.Handler(
                self.__rpc_grant_allowance,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgGrantAllowance,
                MsgGrantAllowanceResponse,
            ),
            "/cosmos.feegrant.v1beta1.Msg/RevokeAllowance": grpclib.const.Handler(
                self.__rpc_revoke_allowance,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgRevokeAllowance,
                MsgRevokeAllowanceResponse,
            ),
            "/cosmos.feegrant.v1beta1.Msg/PruneAllowances": grpclib.const.Handler(
                self.__rpc_prune_allowances,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgPruneAllowances,
                MsgPruneAllowancesResponse,
            ),
        }
