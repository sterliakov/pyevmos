# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/store/streaming/abci/grpc.proto
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

from .....tendermint import abci as ____tendermint_abci__
from ... import v1beta1 as __v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class ListenFinalizeBlockRequest(betterproto.Message):
    """ListenEndBlockRequest is the request type for the ListenEndBlock RPC method"""

    req: "____tendermint_abci__.RequestFinalizeBlock" = betterproto.message_field(1)
    res: "____tendermint_abci__.ResponseFinalizeBlock" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ListenFinalizeBlockResponse(betterproto.Message):
    """ListenEndBlockResponse is the response type for the ListenEndBlock RPC method"""

    pass


@dataclass(eq=False, repr=False)
class ListenCommitRequest(betterproto.Message):
    """ListenCommitRequest is the request type for the ListenCommit RPC method"""

    block_height: int = betterproto.int64_field(1)
    """explicitly pass in block height as ResponseCommit does not contain this info"""

    res: "____tendermint_abci__.ResponseCommit" = betterproto.message_field(2)
    change_set: List["__v1_beta1__.StoreKvPair"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class ListenCommitResponse(betterproto.Message):
    """ListenCommitResponse is the response type for the ListenCommit RPC method"""

    pass


class AbciListenerServiceStub(betterproto.ServiceStub):
    async def listen_finalize_block(
        self,
        listen_finalize_block_request: "ListenFinalizeBlockRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "ListenFinalizeBlockResponse":
        return await self._unary_unary(
            "/cosmos.store.streaming.abci.ABCIListenerService/ListenFinalizeBlock",
            listen_finalize_block_request,
            ListenFinalizeBlockResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def listen_commit(
        self,
        listen_commit_request: "ListenCommitRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "ListenCommitResponse":
        return await self._unary_unary(
            "/cosmos.store.streaming.abci.ABCIListenerService/ListenCommit",
            listen_commit_request,
            ListenCommitResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class AbciListenerServiceBase(ServiceBase):
    async def listen_finalize_block(
        self, listen_finalize_block_request: "ListenFinalizeBlockRequest"
    ) -> "ListenFinalizeBlockResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def listen_commit(
        self, listen_commit_request: "ListenCommitRequest"
    ) -> "ListenCommitResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_listen_finalize_block(
        self,
        stream: "grpclib.server.Stream[ListenFinalizeBlockRequest, ListenFinalizeBlockResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.listen_finalize_block(request)
        await stream.send_message(response)

    async def __rpc_listen_commit(
        self, stream: "grpclib.server.Stream[ListenCommitRequest, ListenCommitResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.listen_commit(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.store.streaming.abci.ABCIListenerService/ListenFinalizeBlock": grpclib.const.Handler(
                self.__rpc_listen_finalize_block,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListenFinalizeBlockRequest,
                ListenFinalizeBlockResponse,
            ),
            "/cosmos.store.streaming.abci.ABCIListenerService/ListenCommit": grpclib.const.Handler(
                self.__rpc_listen_commit,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListenCommitRequest,
                ListenCommitResponse,
            ),
        }
