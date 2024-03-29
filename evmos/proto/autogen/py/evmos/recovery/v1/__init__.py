# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: evmos/recovery/v1/genesis.proto, evmos/recovery/v1/query.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from datetime import timedelta
from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the recovery module's genesis state."""

    params: 'Params' = betterproto.message_field(1)
    """params defines all the paramaters of the module."""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params holds parameters for the recovery module"""

    enable_recovery: bool = betterproto.bool_field(1)
    """enable recovery IBC middleware"""

    packet_timeout_duration: timedelta = betterproto.message_field(2)
    """duration added to timeout timestamp for balances recovered via IBC packets"""


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""

    params: 'Params' = betterproto.message_field(1)
    """params defines the parameters of the module."""


class QueryStub(betterproto.ServiceStub):
    async def params(
        self,
        query_params_request: 'QueryParamsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryParamsResponse':
        return await self._unary_unary(
            '/evmos.recovery.v1.Query/Params',
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def params(
        self, query_params_request: 'QueryParamsRequest'
    ) -> 'QueryParamsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(
        self, stream: 'grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/evmos.recovery.v1.Query/Params': grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }
