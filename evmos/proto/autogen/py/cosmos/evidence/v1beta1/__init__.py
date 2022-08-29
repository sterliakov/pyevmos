# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/evidence/v1beta1/evidence.proto, cosmos/evidence/v1beta1/genesis.proto, cosmos/evidence/v1beta1/query.proto, cosmos/evidence/v1beta1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...base.query import v1beta1 as __base_query_v1_beta1__

if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class Equivocation(betterproto.Message):
    """
    Equivocation implements the Evidence interface and defines evidence of
    double signing misbehavior.
    """

    height: int = betterproto.int64_field(1)
    time: datetime = betterproto.message_field(2)
    power: int = betterproto.int64_field(3)
    consensus_address: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class QueryEvidenceRequest(betterproto.Message):
    """
    QueryEvidenceRequest is the request type for the Query/Evidence RPC method.
    """

    evidence_hash: bytes = betterproto.bytes_field(1)
    """evidence_hash defines the hash of the requested evidence."""


@dataclass(eq=False, repr=False)
class QueryEvidenceResponse(betterproto.Message):
    """
    QueryEvidenceResponse is the response type for the Query/Evidence RPC
    method.
    """

    evidence: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(1)
    """evidence returns the requested evidence."""


@dataclass(eq=False, repr=False)
class QueryAllEvidenceRequest(betterproto.Message):
    """
    QueryEvidenceRequest is the request type for the Query/AllEvidence RPC
    method.
    """

    pagination: '__base_query_v1_beta1__.PageRequest' = betterproto.message_field(1)
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryAllEvidenceResponse(betterproto.Message):
    """
    QueryAllEvidenceResponse is the response type for the Query/AllEvidence RPC
    method.
    """

    evidence: List['betterproto_lib_google_protobuf.Any'] = betterproto.message_field(1)
    """evidence returns all evidences."""

    pagination: '__base_query_v1_beta1__.PageResponse' = betterproto.message_field(2)
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the evidence module's genesis state."""

    evidence: List['betterproto_lib_google_protobuf.Any'] = betterproto.message_field(1)
    """evidence defines all the evidence at genesis."""


@dataclass(eq=False, repr=False)
class MsgSubmitEvidence(betterproto.Message):
    """
    MsgSubmitEvidence represents a message that supports submitting arbitrary
    Evidence of misbehavior such as equivocation or counterfactual signing.
    """

    submitter: str = betterproto.string_field(1)
    evidence: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MsgSubmitEvidenceResponse(betterproto.Message):
    """
    MsgSubmitEvidenceResponse defines the Msg/SubmitEvidence response type.
    """

    hash: bytes = betterproto.bytes_field(4)
    """hash defines the hash of the evidence."""


class QueryStub(betterproto.ServiceStub):
    async def evidence(
        self,
        query_evidence_request: 'QueryEvidenceRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryEvidenceResponse':
        return await self._unary_unary(
            '/cosmos.evidence.v1beta1.Query/Evidence',
            query_evidence_request,
            QueryEvidenceResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def all_evidence(
        self,
        query_all_evidence_request: 'QueryAllEvidenceRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryAllEvidenceResponse':
        return await self._unary_unary(
            '/cosmos.evidence.v1beta1.Query/AllEvidence',
            query_all_evidence_request,
            QueryAllEvidenceResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def submit_evidence(
        self,
        msg_submit_evidence: 'MsgSubmitEvidence',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgSubmitEvidenceResponse':
        return await self._unary_unary(
            '/cosmos.evidence.v1beta1.Msg/SubmitEvidence',
            msg_submit_evidence,
            MsgSubmitEvidenceResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def evidence(
        self, query_evidence_request: 'QueryEvidenceRequest'
    ) -> 'QueryEvidenceResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def all_evidence(
        self, query_all_evidence_request: 'QueryAllEvidenceRequest'
    ) -> 'QueryAllEvidenceResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_evidence(
        self,
        stream: 'grpclib.server.Stream[QueryEvidenceRequest, QueryEvidenceResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.evidence(request)
        await stream.send_message(response)

    async def __rpc_all_evidence(
        self,
        stream: 'grpclib.server.Stream[QueryAllEvidenceRequest, QueryAllEvidenceResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.all_evidence(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/cosmos.evidence.v1beta1.Query/Evidence': grpclib.const.Handler(
                self.__rpc_evidence,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryEvidenceRequest,
                QueryEvidenceResponse,
            ),
            '/cosmos.evidence.v1beta1.Query/AllEvidence': grpclib.const.Handler(
                self.__rpc_all_evidence,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllEvidenceRequest,
                QueryAllEvidenceResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def submit_evidence(
        self, msg_submit_evidence: 'MsgSubmitEvidence'
    ) -> 'MsgSubmitEvidenceResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_submit_evidence(
        self,
        stream: 'grpclib.server.Stream[MsgSubmitEvidence, MsgSubmitEvidenceResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.submit_evidence(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/cosmos.evidence.v1beta1.Msg/SubmitEvidence': grpclib.const.Handler(
                self.__rpc_submit_evidence,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSubmitEvidence,
                MsgSubmitEvidenceResponse,
            ),
        }
