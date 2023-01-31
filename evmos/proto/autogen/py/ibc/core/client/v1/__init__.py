# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/core/client/v1/client.proto, ibc/core/client/v1/genesis.proto, ibc/core/client/v1/query.proto, ibc/core/client/v1/tx.proto
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
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from .....cosmos.base.query import v1beta1 as ____cosmos_base_query_v1_beta1__
from .....cosmos.upgrade import v1beta1 as ____cosmos_upgrade_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class IdentifiedClientState(betterproto.Message):
    """
    IdentifiedClientState defines a client state with an additional client
    identifier field.
    """

    client_id: str = betterproto.string_field(1)
    """client identifier"""

    client_state: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(2)
    """client state"""


@dataclass(eq=False, repr=False)
class ConsensusStateWithHeight(betterproto.Message):
    """
    ConsensusStateWithHeight defines a consensus state with an additional height
    field.
    """

    height: 'Height' = betterproto.message_field(1)
    """consensus state height"""

    consensus_state: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(
        2
    )
    """consensus state"""


@dataclass(eq=False, repr=False)
class ClientConsensusStates(betterproto.Message):
    """
    ClientConsensusStates defines all the stored consensus states for a given
    client.
    """

    client_id: str = betterproto.string_field(1)
    """client identifier"""

    consensus_states: List['ConsensusStateWithHeight'] = betterproto.message_field(2)
    """consensus states and their heights associated with the client"""


@dataclass(eq=False, repr=False)
class ClientUpdateProposal(betterproto.Message):
    """
    ClientUpdateProposal is a governance proposal. If it passes, the substitute
    client's latest consensus state is copied over to the subject client. The
    proposal handler may fail if the subject and the substitute do not match in
    client and chain parameters (with exception to latest height, frozen height,
    and chain-id).
    """

    title: str = betterproto.string_field(1)
    """the title of the update proposal"""

    description: str = betterproto.string_field(2)
    """the description of the proposal"""

    subject_client_id: str = betterproto.string_field(3)
    """the client identifier for the client to be updated if the proposal passes"""

    substitute_client_id: str = betterproto.string_field(4)
    """
    the substitute client identifier for the client standing in for the subject
    client
    """


@dataclass(eq=False, repr=False)
class UpgradeProposal(betterproto.Message):
    """
    UpgradeProposal is a gov Content type for initiating an IBC breaking
    upgrade.
    """

    title: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)
    plan: '____cosmos_upgrade_v1_beta1__.Plan' = betterproto.message_field(3)
    upgraded_client_state: 'betterproto_lib_google_protobuf.Any' = (
        betterproto.message_field(4)
    )
    """
    An UpgradedClientState must be provided to perform an IBC breaking upgrade.
    This will make the chain commit to the correct upgraded (self) client state
    before the upgrade occurs, so that connecting chains can verify that the
    new upgraded client is valid by verifying a proof on the previous version
    of the chain. This will allow IBC connections to persist smoothly across
    planned chain upgrades
    """


@dataclass(eq=False, repr=False)
class Height(betterproto.Message):
    """
    Height is a monotonically increasing data type
    that can be compared against another Height for the purposes of updating and
    freezing clients
    Normally the RevisionHeight is incremented at each height while keeping
    RevisionNumber the same. However some consensus algorithms may choose to
    reset the height in certain conditions e.g. hard forks, state-machine
    breaking changes In these cases, the RevisionNumber is incremented so that
    height continues to be monitonically increasing even as the RevisionHeight
    gets reset
    """

    revision_number: int = betterproto.uint64_field(1)
    """the revision that the client is currently on"""

    revision_height: int = betterproto.uint64_field(2)
    """the height within the given revision"""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the set of IBC light client parameters."""

    allowed_clients: List[str] = betterproto.string_field(1)
    """allowed_clients defines the list of allowed client state types."""


@dataclass(eq=False, repr=False)
class QueryClientStateRequest(betterproto.Message):
    """
    QueryClientStateRequest is the request type for the Query/ClientState RPC
    method
    """

    client_id: str = betterproto.string_field(1)
    """client state unique identifier"""


@dataclass(eq=False, repr=False)
class QueryClientStateResponse(betterproto.Message):
    """
    QueryClientStateResponse is the response type for the Query/ClientState RPC
    method. Besides the client state, it includes a proof and the height from
    which the proof was retrieved.
    """

    client_state: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(1)
    """client state associated with the request identifier"""

    proof: bytes = betterproto.bytes_field(2)
    """merkle proof of existence"""

    proof_height: 'Height' = betterproto.message_field(3)
    """height at which the proof was retrieved"""


@dataclass(eq=False, repr=False)
class QueryClientStatesRequest(betterproto.Message):
    """
    QueryClientStatesRequest is the request type for the Query/ClientStates RPC
    method
    """

    pagination: '____cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(1)
    )
    """pagination request"""


@dataclass(eq=False, repr=False)
class QueryClientStatesResponse(betterproto.Message):
    """
    QueryClientStatesResponse is the response type for the Query/ClientStates RPC
    method.
    """

    client_states: List['IdentifiedClientState'] = betterproto.message_field(1)
    """list of stored ClientStates of the chain."""

    pagination: '____cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )
    """pagination response"""


@dataclass(eq=False, repr=False)
class QueryConsensusStateRequest(betterproto.Message):
    """
    QueryConsensusStateRequest is the request type for the Query/ConsensusState
    RPC method. Besides the consensus state, it includes a proof and the height
    from which the proof was retrieved.
    """

    client_id: str = betterproto.string_field(1)
    """client identifier"""

    revision_number: int = betterproto.uint64_field(2)
    """consensus state revision number"""

    revision_height: int = betterproto.uint64_field(3)
    """consensus state revision height"""

    latest_height: bool = betterproto.bool_field(4)
    """
    latest_height overrrides the height field and queries the latest stored
    ConsensusState
    """


@dataclass(eq=False, repr=False)
class QueryConsensusStateResponse(betterproto.Message):
    """
    QueryConsensusStateResponse is the response type for the Query/ConsensusState
    RPC method
    """

    consensus_state: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(
        1
    )
    """consensus state associated with the client identifier at the given height"""

    proof: bytes = betterproto.bytes_field(2)
    """merkle proof of existence"""

    proof_height: 'Height' = betterproto.message_field(3)
    """height at which the proof was retrieved"""


@dataclass(eq=False, repr=False)
class QueryConsensusStatesRequest(betterproto.Message):
    """
    QueryConsensusStatesRequest is the request type for the Query/ConsensusStates
    RPC method.
    """

    client_id: str = betterproto.string_field(1)
    """client identifier"""

    pagination: '____cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(2)
    )
    """pagination request"""


@dataclass(eq=False, repr=False)
class QueryConsensusStatesResponse(betterproto.Message):
    """
    QueryConsensusStatesResponse is the response type for the
    Query/ConsensusStates RPC method
    """

    consensus_states: List['ConsensusStateWithHeight'] = betterproto.message_field(1)
    """consensus states associated with the identifier"""

    pagination: '____cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )
    """pagination response"""


@dataclass(eq=False, repr=False)
class QueryClientStatusRequest(betterproto.Message):
    """
    QueryClientStatusRequest is the request type for the Query/ClientStatus RPC
    method
    """

    client_id: str = betterproto.string_field(1)
    """client unique identifier"""


@dataclass(eq=False, repr=False)
class QueryClientStatusResponse(betterproto.Message):
    """
    QueryClientStatusResponse is the response type for the Query/ClientStatus RPC
    method. It returns the current status of the IBC client.
    """

    status: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryClientParamsRequest(betterproto.Message):
    """
    QueryClientParamsRequest is the request type for the Query/ClientParams RPC
    method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryClientParamsResponse(betterproto.Message):
    """
    QueryClientParamsResponse is the response type for the Query/ClientParams RPC
    method.
    """

    params: 'Params' = betterproto.message_field(1)
    """params defines the parameters of the module."""


@dataclass(eq=False, repr=False)
class QueryUpgradedClientStateRequest(betterproto.Message):
    """
    QueryUpgradedClientStateRequest is the request type for the
    Query/UpgradedClientState RPC method
    """

    pass


@dataclass(eq=False, repr=False)
class QueryUpgradedClientStateResponse(betterproto.Message):
    """
    QueryUpgradedClientStateResponse is the response type for the
    Query/UpgradedClientState RPC method.
    """

    upgraded_client_state: 'betterproto_lib_google_protobuf.Any' = (
        betterproto.message_field(1)
    )
    """client state associated with the request identifier"""


@dataclass(eq=False, repr=False)
class QueryUpgradedConsensusStateRequest(betterproto.Message):
    """
    QueryUpgradedConsensusStateRequest is the request type for the
    Query/UpgradedConsensusState RPC method
    """

    pass


@dataclass(eq=False, repr=False)
class QueryUpgradedConsensusStateResponse(betterproto.Message):
    """
    QueryUpgradedConsensusStateResponse is the response type for the
    Query/UpgradedConsensusState RPC method.
    """

    upgraded_consensus_state: 'betterproto_lib_google_protobuf.Any' = (
        betterproto.message_field(1)
    )
    """Consensus state associated with the request identifier"""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the ibc client submodule's genesis state."""

    clients: List['IdentifiedClientState'] = betterproto.message_field(1)
    """client states with their corresponding identifiers"""

    clients_consensus: List['ClientConsensusStates'] = betterproto.message_field(2)
    """consensus states from each client"""

    clients_metadata: List['IdentifiedGenesisMetadata'] = betterproto.message_field(3)
    """metadata from each client"""

    params: 'Params' = betterproto.message_field(4)
    create_localhost: bool = betterproto.bool_field(5)
    """create localhost on initialization"""

    next_client_sequence: int = betterproto.uint64_field(6)
    """the sequence for the next generated client identifier"""


@dataclass(eq=False, repr=False)
class GenesisMetadata(betterproto.Message):
    """
    GenesisMetadata defines the genesis type for metadata that clients may return
    with ExportMetadata
    """

    key: bytes = betterproto.bytes_field(1)
    """store key of metadata without clientID-prefix"""

    value: bytes = betterproto.bytes_field(2)
    """metadata value"""


@dataclass(eq=False, repr=False)
class IdentifiedGenesisMetadata(betterproto.Message):
    """
    IdentifiedGenesisMetadata has the client metadata with the corresponding
    client id.
    """

    client_id: str = betterproto.string_field(1)
    client_metadata: List['GenesisMetadata'] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MsgCreateClient(betterproto.Message):
    """MsgCreateClient defines a message to create an IBC client"""

    client_state: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(1)
    """light client state"""

    consensus_state: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(
        2
    )
    """
    consensus state associated with the client that corresponds to a given
    height.
    """

    signer: str = betterproto.string_field(3)
    """signer address"""


@dataclass(eq=False, repr=False)
class MsgCreateClientResponse(betterproto.Message):
    """MsgCreateClientResponse defines the Msg/CreateClient response type."""

    pass


@dataclass(eq=False, repr=False)
class MsgUpdateClient(betterproto.Message):
    """
    MsgUpdateClient defines an sdk.Msg to update a IBC client state using
    the given header.
    """

    client_id: str = betterproto.string_field(1)
    """client unique identifier"""

    header: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(2)
    """header to update the light client"""

    signer: str = betterproto.string_field(3)
    """signer address"""


@dataclass(eq=False, repr=False)
class MsgUpdateClientResponse(betterproto.Message):
    """MsgUpdateClientResponse defines the Msg/UpdateClient response type."""

    pass


@dataclass(eq=False, repr=False)
class MsgUpgradeClient(betterproto.Message):
    """
    MsgUpgradeClient defines an sdk.Msg to upgrade an IBC client to a new client
    state
    """

    client_id: str = betterproto.string_field(1)
    """client unique identifier"""

    client_state: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(2)
    """upgraded client state"""

    consensus_state: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(
        3
    )
    """
    upgraded consensus state, only contains enough information to serve as a
    basis of trust in update logic
    """

    proof_upgrade_client: bytes = betterproto.bytes_field(4)
    """proof that old chain committed to new client"""

    proof_upgrade_consensus_state: bytes = betterproto.bytes_field(5)
    """proof that old chain committed to new consensus state"""

    signer: str = betterproto.string_field(6)
    """signer address"""


@dataclass(eq=False, repr=False)
class MsgUpgradeClientResponse(betterproto.Message):
    """MsgUpgradeClientResponse defines the Msg/UpgradeClient response type."""

    pass


@dataclass(eq=False, repr=False)
class MsgSubmitMisbehaviour(betterproto.Message):
    """
    MsgSubmitMisbehaviour defines an sdk.Msg type that submits Evidence for
    light client misbehaviour.
    """

    client_id: str = betterproto.string_field(1)
    """client unique identifier"""

    misbehaviour: 'betterproto_lib_google_protobuf.Any' = betterproto.message_field(2)
    """misbehaviour used for freezing the light client"""

    signer: str = betterproto.string_field(3)
    """signer address"""


@dataclass(eq=False, repr=False)
class MsgSubmitMisbehaviourResponse(betterproto.Message):
    """
    MsgSubmitMisbehaviourResponse defines the Msg/SubmitMisbehaviour response
    type.
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def client_state(
        self,
        query_client_state_request: 'QueryClientStateRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryClientStateResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Query/ClientState',
            query_client_state_request,
            QueryClientStateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def client_states(
        self,
        query_client_states_request: 'QueryClientStatesRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryClientStatesResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Query/ClientStates',
            query_client_states_request,
            QueryClientStatesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def consensus_state(
        self,
        query_consensus_state_request: 'QueryConsensusStateRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryConsensusStateResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Query/ConsensusState',
            query_consensus_state_request,
            QueryConsensusStateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def consensus_states(
        self,
        query_consensus_states_request: 'QueryConsensusStatesRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryConsensusStatesResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Query/ConsensusStates',
            query_consensus_states_request,
            QueryConsensusStatesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def client_status(
        self,
        query_client_status_request: 'QueryClientStatusRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryClientStatusResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Query/ClientStatus',
            query_client_status_request,
            QueryClientStatusResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def client_params(
        self,
        query_client_params_request: 'QueryClientParamsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryClientParamsResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Query/ClientParams',
            query_client_params_request,
            QueryClientParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def upgraded_client_state(
        self,
        query_upgraded_client_state_request: 'QueryUpgradedClientStateRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryUpgradedClientStateResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Query/UpgradedClientState',
            query_upgraded_client_state_request,
            QueryUpgradedClientStateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def upgraded_consensus_state(
        self,
        query_upgraded_consensus_state_request: 'QueryUpgradedConsensusStateRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryUpgradedConsensusStateResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Query/UpgradedConsensusState',
            query_upgraded_consensus_state_request,
            QueryUpgradedConsensusStateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def create_client(
        self,
        msg_create_client: 'MsgCreateClient',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgCreateClientResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Msg/CreateClient',
            msg_create_client,
            MsgCreateClientResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def update_client(
        self,
        msg_update_client: 'MsgUpdateClient',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgUpdateClientResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Msg/UpdateClient',
            msg_update_client,
            MsgUpdateClientResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def upgrade_client(
        self,
        msg_upgrade_client: 'MsgUpgradeClient',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgUpgradeClientResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Msg/UpgradeClient',
            msg_upgrade_client,
            MsgUpgradeClientResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def submit_misbehaviour(
        self,
        msg_submit_misbehaviour: 'MsgSubmitMisbehaviour',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgSubmitMisbehaviourResponse':
        return await self._unary_unary(
            '/ibc.core.client.v1.Msg/SubmitMisbehaviour',
            msg_submit_misbehaviour,
            MsgSubmitMisbehaviourResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def client_state(
        self, query_client_state_request: 'QueryClientStateRequest'
    ) -> 'QueryClientStateResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def client_states(
        self, query_client_states_request: 'QueryClientStatesRequest'
    ) -> 'QueryClientStatesResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def consensus_state(
        self, query_consensus_state_request: 'QueryConsensusStateRequest'
    ) -> 'QueryConsensusStateResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def consensus_states(
        self, query_consensus_states_request: 'QueryConsensusStatesRequest'
    ) -> 'QueryConsensusStatesResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def client_status(
        self, query_client_status_request: 'QueryClientStatusRequest'
    ) -> 'QueryClientStatusResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def client_params(
        self, query_client_params_request: 'QueryClientParamsRequest'
    ) -> 'QueryClientParamsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upgraded_client_state(
        self, query_upgraded_client_state_request: 'QueryUpgradedClientStateRequest'
    ) -> 'QueryUpgradedClientStateResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upgraded_consensus_state(
        self,
        query_upgraded_consensus_state_request: 'QueryUpgradedConsensusStateRequest',
    ) -> 'QueryUpgradedConsensusStateResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_client_state(
        self,
        stream: 'grpclib.server.Stream[QueryClientStateRequest, QueryClientStateResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.client_state(request)
        await stream.send_message(response)

    async def __rpc_client_states(
        self,
        stream: 'grpclib.server.Stream[QueryClientStatesRequest, QueryClientStatesResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.client_states(request)
        await stream.send_message(response)

    async def __rpc_consensus_state(
        self,
        stream: 'grpclib.server.Stream[QueryConsensusStateRequest, QueryConsensusStateResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.consensus_state(request)
        await stream.send_message(response)

    async def __rpc_consensus_states(
        self,
        stream: 'grpclib.server.Stream[QueryConsensusStatesRequest, QueryConsensusStatesResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.consensus_states(request)
        await stream.send_message(response)

    async def __rpc_client_status(
        self,
        stream: 'grpclib.server.Stream[QueryClientStatusRequest, QueryClientStatusResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.client_status(request)
        await stream.send_message(response)

    async def __rpc_client_params(
        self,
        stream: 'grpclib.server.Stream[QueryClientParamsRequest, QueryClientParamsResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.client_params(request)
        await stream.send_message(response)

    async def __rpc_upgraded_client_state(
        self,
        stream: 'grpclib.server.Stream[QueryUpgradedClientStateRequest, QueryUpgradedClientStateResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.upgraded_client_state(request)
        await stream.send_message(response)

    async def __rpc_upgraded_consensus_state(
        self,
        stream: 'grpclib.server.Stream[QueryUpgradedConsensusStateRequest, QueryUpgradedConsensusStateResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.upgraded_consensus_state(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/ibc.core.client.v1.Query/ClientState': grpclib.const.Handler(
                self.__rpc_client_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientStateRequest,
                QueryClientStateResponse,
            ),
            '/ibc.core.client.v1.Query/ClientStates': grpclib.const.Handler(
                self.__rpc_client_states,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientStatesRequest,
                QueryClientStatesResponse,
            ),
            '/ibc.core.client.v1.Query/ConsensusState': grpclib.const.Handler(
                self.__rpc_consensus_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConsensusStateRequest,
                QueryConsensusStateResponse,
            ),
            '/ibc.core.client.v1.Query/ConsensusStates': grpclib.const.Handler(
                self.__rpc_consensus_states,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConsensusStatesRequest,
                QueryConsensusStatesResponse,
            ),
            '/ibc.core.client.v1.Query/ClientStatus': grpclib.const.Handler(
                self.__rpc_client_status,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientStatusRequest,
                QueryClientStatusResponse,
            ),
            '/ibc.core.client.v1.Query/ClientParams': grpclib.const.Handler(
                self.__rpc_client_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientParamsRequest,
                QueryClientParamsResponse,
            ),
            '/ibc.core.client.v1.Query/UpgradedClientState': grpclib.const.Handler(
                self.__rpc_upgraded_client_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryUpgradedClientStateRequest,
                QueryUpgradedClientStateResponse,
            ),
            '/ibc.core.client.v1.Query/UpgradedConsensusState': grpclib.const.Handler(
                self.__rpc_upgraded_consensus_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryUpgradedConsensusStateRequest,
                QueryUpgradedConsensusStateResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def create_client(
        self, msg_create_client: 'MsgCreateClient'
    ) -> 'MsgCreateClientResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_client(
        self, msg_update_client: 'MsgUpdateClient'
    ) -> 'MsgUpdateClientResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def upgrade_client(
        self, msg_upgrade_client: 'MsgUpgradeClient'
    ) -> 'MsgUpgradeClientResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def submit_misbehaviour(
        self, msg_submit_misbehaviour: 'MsgSubmitMisbehaviour'
    ) -> 'MsgSubmitMisbehaviourResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_create_client(
        self, stream: 'grpclib.server.Stream[MsgCreateClient, MsgCreateClientResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.create_client(request)
        await stream.send_message(response)

    async def __rpc_update_client(
        self, stream: 'grpclib.server.Stream[MsgUpdateClient, MsgUpdateClientResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_client(request)
        await stream.send_message(response)

    async def __rpc_upgrade_client(
        self,
        stream: 'grpclib.server.Stream[MsgUpgradeClient, MsgUpgradeClientResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.upgrade_client(request)
        await stream.send_message(response)

    async def __rpc_submit_misbehaviour(
        self,
        stream: 'grpclib.server.Stream[MsgSubmitMisbehaviour, MsgSubmitMisbehaviourResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.submit_misbehaviour(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/ibc.core.client.v1.Msg/CreateClient': grpclib.const.Handler(
                self.__rpc_create_client,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgCreateClient,
                MsgCreateClientResponse,
            ),
            '/ibc.core.client.v1.Msg/UpdateClient': grpclib.const.Handler(
                self.__rpc_update_client,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateClient,
                MsgUpdateClientResponse,
            ),
            '/ibc.core.client.v1.Msg/UpgradeClient': grpclib.const.Handler(
                self.__rpc_upgrade_client,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpgradeClient,
                MsgUpgradeClientResponse,
            ),
            '/ibc.core.client.v1.Msg/SubmitMisbehaviour': grpclib.const.Handler(
                self.__rpc_submit_misbehaviour,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSubmitMisbehaviour,
                MsgSubmitMisbehaviourResponse,
            ),
        }
