# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/params/v1beta1/params.proto, cosmos/params/v1beta1/query.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
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
class ParameterChangeProposal(betterproto.Message):
    """ParameterChangeProposal defines a proposal to change one or more parameters."""

    title: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)
    changes: List['ParamChange'] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class ParamChange(betterproto.Message):
    """
    ParamChange defines an individual parameter change, for use in
    ParameterChangeProposal.
    """

    subspace: str = betterproto.string_field(1)
    key: str = betterproto.string_field(2)
    value: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest is request type for the Query/Params RPC method."""

    subspace: str = betterproto.string_field(1)
    """subspace defines the module to query the parameter for."""

    key: str = betterproto.string_field(2)
    """key defines the key of the parameter in the subspace."""


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """QueryParamsResponse is response type for the Query/Params RPC method."""

    param: 'ParamChange' = betterproto.message_field(1)
    """param defines the queried parameter."""


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
            '/cosmos.params.v1beta1.Query/Params',
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
            '/cosmos.params.v1beta1.Query/Params': grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }
