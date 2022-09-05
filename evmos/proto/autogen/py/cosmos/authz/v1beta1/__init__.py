# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/authz/v1beta1/authz.proto, cosmos/authz/v1beta1/event.proto, cosmos/authz/v1beta1/genesis.proto, cosmos/authz/v1beta1/query.proto, cosmos/authz/v1beta1/tx.proto
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
class EventGrant(betterproto.Message):
    """EventGrant is emitted on Msg/Grant"""

    msg_type_url: str = betterproto.string_field(2)
    """Msg type URL for which an autorization is granted"""

    granter: str = betterproto.string_field(3)
    """Granter account address"""

    grantee: str = betterproto.string_field(4)
    """Grantee account address"""


@dataclass(eq=False, repr=False)
class EventRevoke(betterproto.Message):
    """EventRevoke is emitted on Msg/Revoke"""

    msg_type_url: str = betterproto.string_field(2)
    """Msg type URL for which an autorization is revoked"""

    granter: str = betterproto.string_field(3)
    """Granter account address"""

    grantee: str = betterproto.string_field(4)
    """Grantee account address"""


@dataclass(eq=False, repr=False)
class GenericAuthorization(betterproto.Message):
    """
    GenericAuthorization gives the grantee unrestricted permissions to execute
    the provided method on behalf of the granter's account.
    """

    msg: str = betterproto.string_field(1)
    """
    Msg, identified by it's type URL, to grant unrestricted permissions to
    execute
    """


@dataclass(eq=False, repr=False)
class Grant(betterproto.Message):
    """
    Grant gives permissions to execute the provide method with expiration time.
    """

    authorization: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(1)
    expiration: datetime = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class GrantAuthorization(betterproto.Message):
    """
    GrantAuthorization extends a grant with both the addresses of the grantee
    and granter. It is used in genesis.proto and query.proto Since: cosmos-sdk
    0.45.2
    """

    granter: str = betterproto.string_field(1)
    grantee: str = betterproto.string_field(2)
    authorization: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(3)
    expiration: datetime = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class QueryGrantsRequest(betterproto.Message):
    """
    QueryGrantsRequest is the request type for the Query/Grants RPC method.
    """

    granter: str = betterproto.string_field(1)
    grantee: str = betterproto.string_field(2)
    msg_type_url: str = betterproto.string_field(3)
    """
    Optional, msg_type_url, when set, will query only grants matching given msg
    type.
    """

    pagination: '__base_query_v1_beta1__.PageRequest' = betterproto.message_field(4)
    """pagination defines an pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryGrantsResponse(betterproto.Message):
    """
    QueryGrantsResponse is the response type for the Query/Authorizations RPC
    method.
    """

    grants: List['Grant'] = betterproto.message_field(1)
    """authorizations is a list of grants granted for grantee by granter."""

    pagination: '__base_query_v1_beta1__.PageResponse' = betterproto.message_field(2)
    """pagination defines an pagination for the response."""


@dataclass(eq=False, repr=False)
class QueryGranterGrantsRequest(betterproto.Message):
    """
    QueryGranterGrantsRequest is the request type for the Query/GranterGrants
    RPC method.
    """

    granter: str = betterproto.string_field(1)
    pagination: '__base_query_v1_beta1__.PageRequest' = betterproto.message_field(2)
    """pagination defines an pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryGranterGrantsResponse(betterproto.Message):
    """
    QueryGranterGrantsResponse is the response type for the Query/GranterGrants
    RPC method.
    """

    grants: List['GrantAuthorization'] = betterproto.message_field(1)
    """grants is a list of grants granted by the granter."""

    pagination: '__base_query_v1_beta1__.PageResponse' = betterproto.message_field(2)
    """pagination defines an pagination for the response."""


@dataclass(eq=False, repr=False)
class QueryGranteeGrantsRequest(betterproto.Message):
    """
    QueryGranteeGrantsRequest is the request type for the Query/IssuedGrants
    RPC method.
    """

    grantee: str = betterproto.string_field(1)
    pagination: '__base_query_v1_beta1__.PageRequest' = betterproto.message_field(2)
    """pagination defines an pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryGranteeGrantsResponse(betterproto.Message):
    """
    QueryGranteeGrantsResponse is the response type for the Query/GranteeGrants
    RPC method.
    """

    grants: List['GrantAuthorization'] = betterproto.message_field(1)
    """grants is a list of grants granted to the grantee."""

    pagination: '__base_query_v1_beta1__.PageResponse' = betterproto.message_field(2)
    """pagination defines an pagination for the response."""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the authz module's genesis state."""

    authorization: List['GrantAuthorization'] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MsgGrant(betterproto.Message):
    """
    MsgGrant is a request type for Grant method. It declares authorization to
    the grantee on behalf of the granter with the provided expiration time.
    """

    granter: str = betterproto.string_field(1)
    grantee: str = betterproto.string_field(2)
    grant: 'Grant' = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class MsgExecResponse(betterproto.Message):
    """MsgExecResponse defines the Msg/MsgExecResponse response type."""

    results: List[bytes] = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class MsgExec(betterproto.Message):
    """
    MsgExec attempts to execute the provided messages using authorizations
    granted to the grantee. Each message should have only one signer
    corresponding to the granter of the authorization.
    """

    grantee: str = betterproto.string_field(1)
    msgs: List['betterproto_lib_google_protobuf.Any'] = betterproto.message_field(2)
    """
    Authorization Msg requests to execute. Each msg must implement
    Authorization interface The x/authz will try to find a grant matching
    (msg.signers[0], grantee, MsgTypeURL(msg)) triple and validate it.
    """


@dataclass(eq=False, repr=False)
class MsgGrantResponse(betterproto.Message):
    """MsgGrantResponse defines the Msg/MsgGrant response type."""

    pass


@dataclass(eq=False, repr=False)
class MsgRevoke(betterproto.Message):
    """
    MsgRevoke revokes any authorization with the provided sdk.Msg type on the
    granter's account with that has been granted to the grantee.
    """

    granter: str = betterproto.string_field(1)
    grantee: str = betterproto.string_field(2)
    msg_type_url: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class MsgRevokeResponse(betterproto.Message):
    """MsgRevokeResponse defines the Msg/MsgRevokeResponse response type."""

    pass


class QueryStub(betterproto.ServiceStub):
    async def grants(
        self,
        query_grants_request: 'QueryGrantsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryGrantsResponse':
        return await self._unary_unary(
            '/cosmos.authz.v1beta1.Query/Grants',
            query_grants_request,
            QueryGrantsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def granter_grants(
        self,
        query_granter_grants_request: 'QueryGranterGrantsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryGranterGrantsResponse':
        return await self._unary_unary(
            '/cosmos.authz.v1beta1.Query/GranterGrants',
            query_granter_grants_request,
            QueryGranterGrantsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def grantee_grants(
        self,
        query_grantee_grants_request: 'QueryGranteeGrantsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryGranteeGrantsResponse':
        return await self._unary_unary(
            '/cosmos.authz.v1beta1.Query/GranteeGrants',
            query_grantee_grants_request,
            QueryGranteeGrantsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def grant(
        self,
        msg_grant: 'MsgGrant',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgGrantResponse':
        return await self._unary_unary(
            '/cosmos.authz.v1beta1.Msg/Grant',
            msg_grant,
            MsgGrantResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def exec(
        self,
        msg_exec: 'MsgExec',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgExecResponse':
        return await self._unary_unary(
            '/cosmos.authz.v1beta1.Msg/Exec',
            msg_exec,
            MsgExecResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def revoke(
        self,
        msg_revoke: 'MsgRevoke',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgRevokeResponse':
        return await self._unary_unary(
            '/cosmos.authz.v1beta1.Msg/Revoke',
            msg_revoke,
            MsgRevokeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def grants(
        self, query_grants_request: 'QueryGrantsRequest'
    ) -> 'QueryGrantsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def granter_grants(
        self, query_granter_grants_request: 'QueryGranterGrantsRequest'
    ) -> 'QueryGranterGrantsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def grantee_grants(
        self, query_grantee_grants_request: 'QueryGranteeGrantsRequest'
    ) -> 'QueryGranteeGrantsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_grants(
        self, stream: 'grpclib.server.Stream[QueryGrantsRequest, QueryGrantsResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.grants(request)
        await stream.send_message(response)

    async def __rpc_granter_grants(
        self,
        stream: 'grpclib.server.Stream[QueryGranterGrantsRequest, QueryGranterGrantsResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.granter_grants(request)
        await stream.send_message(response)

    async def __rpc_grantee_grants(
        self,
        stream: 'grpclib.server.Stream[QueryGranteeGrantsRequest, QueryGranteeGrantsResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.grantee_grants(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/cosmos.authz.v1beta1.Query/Grants': grpclib.const.Handler(
                self.__rpc_grants,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryGrantsRequest,
                QueryGrantsResponse,
            ),
            '/cosmos.authz.v1beta1.Query/GranterGrants': grpclib.const.Handler(
                self.__rpc_granter_grants,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryGranterGrantsRequest,
                QueryGranterGrantsResponse,
            ),
            '/cosmos.authz.v1beta1.Query/GranteeGrants': grpclib.const.Handler(
                self.__rpc_grantee_grants,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryGranteeGrantsRequest,
                QueryGranteeGrantsResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def grant(self, msg_grant: 'MsgGrant') -> 'MsgGrantResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def exec(self, msg_exec: 'MsgExec') -> 'MsgExecResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def revoke(self, msg_revoke: 'MsgRevoke') -> 'MsgRevokeResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_grant(
        self, stream: 'grpclib.server.Stream[MsgGrant, MsgGrantResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.grant(request)
        await stream.send_message(response)

    async def __rpc_exec(
        self, stream: 'grpclib.server.Stream[MsgExec, MsgExecResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.exec(request)
        await stream.send_message(response)

    async def __rpc_revoke(
        self, stream: 'grpclib.server.Stream[MsgRevoke, MsgRevokeResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.revoke(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/cosmos.authz.v1beta1.Msg/Grant': grpclib.const.Handler(
                self.__rpc_grant,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgGrant,
                MsgGrantResponse,
            ),
            '/cosmos.authz.v1beta1.Msg/Exec': grpclib.const.Handler(
                self.__rpc_exec,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgExec,
                MsgExecResponse,
            ),
            '/cosmos.authz.v1beta1.Msg/Revoke': grpclib.const.Handler(
                self.__rpc_revoke,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgRevoke,
                MsgRevokeResponse,
            ),
        }
