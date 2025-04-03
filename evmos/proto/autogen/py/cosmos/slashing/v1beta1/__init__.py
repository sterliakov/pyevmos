# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/slashing/v1beta1/genesis.proto, cosmos/slashing/v1beta1/query.proto, cosmos/slashing/v1beta1/slashing.proto, cosmos/slashing/v1beta1/tx.proto
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
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...base.query import v1beta1 as __base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class ValidatorSigningInfo(betterproto.Message):
    """
    ValidatorSigningInfo defines a validator's signing info for monitoring their
    liveness activity.
    """

    address: str = betterproto.string_field(1)
    start_height: int = betterproto.int64_field(2)
    """Height at which validator was first a candidate OR was un-jailed"""

    index_offset: int = betterproto.int64_field(3)
    """
    Index which is incremented every time a validator is bonded in a block and
    _may_ have signed a pre-commit or not. This in conjunction with the
    signed_blocks_window param determines the index in the missed block bitmap.
    """

    jailed_until: datetime = betterproto.message_field(4)
    """Timestamp until which the validator is jailed due to liveness downtime."""

    tombstoned: bool = betterproto.bool_field(5)
    """
    Whether or not a validator has been tombstoned (killed out of validator
    set). It is set once the validator commits an equivocation or for any other
    configured misbehavior.
    """

    missed_blocks_counter: int = betterproto.int64_field(6)
    """
    A counter of missed (unsigned) blocks. It is used to avoid unnecessary
    reads in the missed block bitmap.
    """


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params represents the parameters used for by the slashing module."""

    signed_blocks_window: int = betterproto.int64_field(1)
    min_signed_per_window: bytes = betterproto.bytes_field(2)
    downtime_jail_duration: timedelta = betterproto.message_field(3)
    slash_fraction_double_sign: bytes = betterproto.bytes_field(4)
    slash_fraction_downtime: bytes = betterproto.bytes_field(5)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the slashing module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    """params defines all the parameters of the module."""

    signing_infos: List["SigningInfo"] = betterproto.message_field(2)
    """
    signing_infos represents a map between validator addresses and their
    signing infos.
    """

    missed_blocks: List["ValidatorMissedBlocks"] = betterproto.message_field(3)
    """
    missed_blocks represents a map between validator addresses and their
    missed blocks.
    """


@dataclass(eq=False, repr=False)
class SigningInfo(betterproto.Message):
    """SigningInfo stores validator signing info of corresponding address."""

    address: str = betterproto.string_field(1)
    """address is the validator address."""

    validator_signing_info: "ValidatorSigningInfo" = betterproto.message_field(2)
    """validator_signing_info represents the signing info of this validator."""


@dataclass(eq=False, repr=False)
class ValidatorMissedBlocks(betterproto.Message):
    """
    ValidatorMissedBlocks contains array of missed blocks of corresponding
    address.
    """

    address: str = betterproto.string_field(1)
    """address is the validator address."""

    missed_blocks: List["MissedBlock"] = betterproto.message_field(2)
    """missed_blocks is an array of missed blocks by the validator."""


@dataclass(eq=False, repr=False)
class MissedBlock(betterproto.Message):
    """MissedBlock contains height and missed status as boolean."""

    index: int = betterproto.int64_field(1)
    """index is the height at which the block was missed."""

    missed: bool = betterproto.bool_field(2)
    """missed is the missed status."""


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method"""

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method"""

    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QuerySigningInfoRequest(betterproto.Message):
    """
    QuerySigningInfoRequest is the request type for the Query/SigningInfo RPC
    method
    """

    cons_address: str = betterproto.string_field(1)
    """cons_address is the address to query signing info of"""


@dataclass(eq=False, repr=False)
class QuerySigningInfoResponse(betterproto.Message):
    """
    QuerySigningInfoResponse is the response type for the Query/SigningInfo RPC
    method
    """

    val_signing_info: "ValidatorSigningInfo" = betterproto.message_field(1)
    """val_signing_info is the signing info of requested val cons address"""


@dataclass(eq=False, repr=False)
class QuerySigningInfosRequest(betterproto.Message):
    """
    QuerySigningInfosRequest is the request type for the Query/SigningInfos RPC
    method
    """

    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QuerySigningInfosResponse(betterproto.Message):
    """
    QuerySigningInfosResponse is the response type for the Query/SigningInfos RPC
    method
    """

    info: List["ValidatorSigningInfo"] = betterproto.message_field(1)
    """info is the signing info of all validators"""

    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MsgUnjail(betterproto.Message):
    """MsgUnjail defines the Msg/Unjail request type"""

    validator_addr: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgUnjailResponse(betterproto.Message):
    """MsgUnjailResponse defines the Msg/Unjail response type"""

    pass


@dataclass(eq=False, repr=False)
class MsgUpdateParams(betterproto.Message):
    """
    MsgUpdateParams is the Msg/UpdateParams request type.
    Since: cosmos-sdk 0.47
    """

    authority: str = betterproto.string_field(1)
    """
    authority is the address that controls the module (defaults to x/gov unless
    overwritten).
    """

    params: "Params" = betterproto.message_field(2)
    """
    params defines the x/slashing parameters to update.
    NOTE: All parameters must be supplied.
    """


@dataclass(eq=False, repr=False)
class MsgUpdateParamsResponse(betterproto.Message):
    """
    MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message.
    Since: cosmos-sdk 0.47
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def signing_info(
        self,
        query_signing_info_request: "QuerySigningInfoRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QuerySigningInfoResponse":
        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Query/SigningInfo",
            query_signing_info_request,
            QuerySigningInfoResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def signing_infos(
        self,
        query_signing_infos_request: "QuerySigningInfosRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QuerySigningInfosResponse":
        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Query/SigningInfos",
            query_signing_infos_request,
            QuerySigningInfosResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def unjail(
        self,
        msg_unjail: "MsgUnjail",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgUnjailResponse":
        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Msg/Unjail",
            msg_unjail,
            MsgUnjailResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def update_params(
        self,
        msg_update_params: "MsgUpdateParams",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgUpdateParamsResponse":
        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Msg/UpdateParams",
            msg_update_params,
            MsgUpdateParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def params(
        self, query_params_request: "QueryParamsRequest"
    ) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def signing_info(
        self, query_signing_info_request: "QuerySigningInfoRequest"
    ) -> "QuerySigningInfoResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def signing_infos(
        self, query_signing_infos_request: "QuerySigningInfosRequest"
    ) -> "QuerySigningInfosResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(
        self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_signing_info(
        self,
        stream: "grpclib.server.Stream[QuerySigningInfoRequest, QuerySigningInfoResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.signing_info(request)
        await stream.send_message(response)

    async def __rpc_signing_infos(
        self,
        stream: "grpclib.server.Stream[QuerySigningInfosRequest, QuerySigningInfosResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.signing_infos(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.slashing.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/cosmos.slashing.v1beta1.Query/SigningInfo": grpclib.const.Handler(
                self.__rpc_signing_info,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySigningInfoRequest,
                QuerySigningInfoResponse,
            ),
            "/cosmos.slashing.v1beta1.Query/SigningInfos": grpclib.const.Handler(
                self.__rpc_signing_infos,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySigningInfosRequest,
                QuerySigningInfosResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def unjail(self, msg_unjail: "MsgUnjail") -> "MsgUnjailResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_params(
        self, msg_update_params: "MsgUpdateParams"
    ) -> "MsgUpdateParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_unjail(
        self, stream: "grpclib.server.Stream[MsgUnjail, MsgUnjailResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.unjail(request)
        await stream.send_message(response)

    async def __rpc_update_params(
        self, stream: "grpclib.server.Stream[MsgUpdateParams, MsgUpdateParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.slashing.v1beta1.Msg/Unjail": grpclib.const.Handler(
                self.__rpc_unjail,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUnjail,
                MsgUnjailResponse,
            ),
            "/cosmos.slashing.v1beta1.Msg/UpdateParams": grpclib.const.Handler(
                self.__rpc_update_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateParams,
                MsgUpdateParamsResponse,
            ),
        }
