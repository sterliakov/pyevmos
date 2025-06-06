# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: evmos/epochs/v1/genesis.proto, evmos/epochs/v1/query.proto
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

from ....cosmos.base.query import v1beta1 as ___cosmos_base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class EpochInfo(betterproto.Message):
    """
    EpochInfo defines the message interface containing the relevant informations about
    an epoch.
    """

    identifier: str = betterproto.string_field(1)
    """identifier of the epoch"""

    start_time: datetime = betterproto.message_field(2)
    """start_time of the epoch"""

    duration: timedelta = betterproto.message_field(3)
    """duration of the epoch"""

    current_epoch: int = betterproto.int64_field(4)
    """current_epoch is the integer identifier of the epoch"""

    current_epoch_start_time: datetime = betterproto.message_field(5)
    """current_epoch_start_time defines the timestamp of the start of the epoch"""

    epoch_counting_started: bool = betterproto.bool_field(6)
    """epoch_counting_started reflects if the counting for the epoch has started"""

    current_epoch_start_height: int = betterproto.int64_field(7)
    """current_epoch_start_height of the epoch"""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the epochs module's genesis state."""

    epochs: List["EpochInfo"] = betterproto.message_field(1)
    """epochs is a slice of EpochInfo that defines the epochs in the genesis state"""


@dataclass(eq=False, repr=False)
class QueryEpochsInfoRequest(betterproto.Message):
    """
    QueryEpochsInfoRequest is the request type for the Query/EpochInfos RPC
    method.
    """

    pagination: "___cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryEpochsInfoResponse(betterproto.Message):
    """
    QueryEpochsInfoResponse is the response type for the Query/EpochInfos RPC
    method.
    """

    epochs: List["EpochInfo"] = betterproto.message_field(1)
    """epochs is a slice of all EpochInfos"""

    pagination: "___cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryCurrentEpochRequest(betterproto.Message):
    """
    QueryCurrentEpochRequest is the request type for the Query/EpochInfos RPC
    method.
    """

    identifier: str = betterproto.string_field(1)
    """identifier of the current epoch"""


@dataclass(eq=False, repr=False)
class QueryCurrentEpochResponse(betterproto.Message):
    """
    QueryCurrentEpochResponse is the response type for the Query/EpochInfos RPC
    method.
    """

    current_epoch: int = betterproto.int64_field(1)
    """current_epoch is the number of the current epoch"""


class QueryStub(betterproto.ServiceStub):
    async def epoch_infos(
        self,
        query_epochs_info_request: "QueryEpochsInfoRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryEpochsInfoResponse":
        return await self._unary_unary(
            "/evmos.epochs.v1.Query/EpochInfos",
            query_epochs_info_request,
            QueryEpochsInfoResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def current_epoch(
        self,
        query_current_epoch_request: "QueryCurrentEpochRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryCurrentEpochResponse":
        return await self._unary_unary(
            "/evmos.epochs.v1.Query/CurrentEpoch",
            query_current_epoch_request,
            QueryCurrentEpochResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def epoch_infos(
        self, query_epochs_info_request: "QueryEpochsInfoRequest"
    ) -> "QueryEpochsInfoResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def current_epoch(
        self, query_current_epoch_request: "QueryCurrentEpochRequest"
    ) -> "QueryCurrentEpochResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_epoch_infos(
        self,
        stream: "grpclib.server.Stream[QueryEpochsInfoRequest, QueryEpochsInfoResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.epoch_infos(request)
        await stream.send_message(response)

    async def __rpc_current_epoch(
        self,
        stream: "grpclib.server.Stream[QueryCurrentEpochRequest, QueryCurrentEpochResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.current_epoch(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/evmos.epochs.v1.Query/EpochInfos": grpclib.const.Handler(
                self.__rpc_epoch_infos,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryEpochsInfoRequest,
                QueryEpochsInfoResponse,
            ),
            "/evmos.epochs.v1.Query/CurrentEpoch": grpclib.const.Handler(
                self.__rpc_current_epoch,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryCurrentEpochRequest,
                QueryCurrentEpochResponse,
            ),
        }
