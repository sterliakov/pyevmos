# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/crisis/v1beta1/genesis.proto, cosmos/crisis/v1beta1/tx.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...base import v1beta1 as __base_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the crisis module's genesis state."""

    constant_fee: '__base_v1_beta1__.Coin' = betterproto.message_field(3)
    """
    constant_fee is the fee used to verify the invariant in the crisis
    module.
    """


@dataclass(eq=False, repr=False)
class MsgVerifyInvariant(betterproto.Message):
    """MsgVerifyInvariant represents a message to verify a particular invariance."""

    sender: str = betterproto.string_field(1)
    invariant_module_name: str = betterproto.string_field(2)
    invariant_route: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgVerifyInvariantResponse(betterproto.Message):
    """MsgVerifyInvariantResponse defines the Msg/VerifyInvariant response type."""

    pass


class MsgStub(betterproto.ServiceStub):
    async def verify_invariant(
        self,
        msg_verify_invariant: 'MsgVerifyInvariant',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgVerifyInvariantResponse':
        return await self._unary_unary(
            '/cosmos.crisis.v1beta1.Msg/VerifyInvariant',
            msg_verify_invariant,
            MsgVerifyInvariantResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgBase(ServiceBase):
    async def verify_invariant(
        self, msg_verify_invariant: 'MsgVerifyInvariant'
    ) -> 'MsgVerifyInvariantResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_verify_invariant(
        self,
        stream: 'grpclib.server.Stream[MsgVerifyInvariant, MsgVerifyInvariantResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.verify_invariant(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/cosmos.crisis.v1beta1.Msg/VerifyInvariant': grpclib.const.Handler(
                self.__rpc_verify_invariant,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgVerifyInvariant,
                MsgVerifyInvariantResponse,
            ),
        }
