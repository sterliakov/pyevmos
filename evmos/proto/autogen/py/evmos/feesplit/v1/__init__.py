# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: evmos/feesplit/v1/feesplit.proto, evmos/feesplit/v1/genesis.proto, evmos/feesplit/v1/query.proto, evmos/feesplit/v1/tx.proto
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

from ....cosmos.base.query import v1beta1 as ___cosmos_base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class FeeSplit(betterproto.Message):
    """
    FeeSplit defines an instance that organizes fee distribution conditions for
    the owner of a given smart contract
    """

    contract_address: str = betterproto.string_field(1)
    """hex address of registered contract"""

    deployer_address: str = betterproto.string_field(2)
    """bech32 address of contract deployer"""

    withdrawer_address: str = betterproto.string_field(3)
    """
    bech32 address of account receiving the transaction fees it defaults to
    deployer_address
    """


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the module's genesis state."""

    params: 'Params' = betterproto.message_field(1)
    """module parameters"""

    fee_splits: List['FeeSplit'] = betterproto.message_field(2)
    """active registered contracts for fee distribution"""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the feesplit module params"""

    enable_fee_split: bool = betterproto.bool_field(1)
    """enable_fee_split defines a parameter to enable the feesplit module"""

    developer_shares: str = betterproto.string_field(2)
    """
    developer_shares defines the proportion of the transaction fees to be
    distributed to the registered contract owner
    """

    addr_derivation_cost_create: int = betterproto.uint64_field(3)
    """
    addr_derivation_cost_create defines the cost of address derivation for
    verifying the contract deployer at fee registration
    """


@dataclass(eq=False, repr=False)
class QueryFeeSplitsRequest(betterproto.Message):
    """
    QueryFeeSplitsRequest is the request type for the Query/FeeSplits RPC method.
    """

    pagination: '___cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(1)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryFeeSplitsResponse(betterproto.Message):
    """
    QueryFeeSplitsResponse is the response type for the Query/FeeSplits RPC method.
    """

    fee_splits: List['FeeSplit'] = betterproto.message_field(1)
    pagination: '___cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryFeeSplitRequest(betterproto.Message):
    """
    QueryFeeSplitRequest is the request type for the Query/FeeSplit RPC method.
    """

    contract_address: str = betterproto.string_field(1)
    """contract identifier is the hex contract address of a contract"""


@dataclass(eq=False, repr=False)
class QueryFeeSplitResponse(betterproto.Message):
    """
    QueryFeeSplitResponse is the response type for the Query/FeeSplit RPC method.
    """

    fee_split: 'FeeSplit' = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC method.
    """

    params: 'Params' = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryDeployerFeeSplitsRequest(betterproto.Message):
    """
    QueryDeployerFeeSplitsRequest is the request type for the
    Query/DeployerFeeSplits RPC method.
    """

    deployer_address: str = betterproto.string_field(1)
    """deployer bech32 address"""

    pagination: '___cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(2)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryDeployerFeeSplitsResponse(betterproto.Message):
    """
    QueryDeployerFeeSplitsResponse is the response type for the
    Query/DeployerFeeSplits RPC method.
    """

    contract_addresses: List[str] = betterproto.string_field(1)
    pagination: '___cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryWithdrawerFeeSplitsRequest(betterproto.Message):
    """
    QueryWithdrawerFeeSplitsRequest is the request type for the
    Query/WithdrawerFeeSplits RPC method.
    """

    withdrawer_address: str = betterproto.string_field(1)
    """withdrawer bech32 address"""

    pagination: '___cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(2)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryWithdrawerFeeSplitsResponse(betterproto.Message):
    """
    QueryWithdrawerFeeSplitsResponse is the response type for the
    Query/WithdrawerFeeSplits RPC method.
    """

    contract_addresses: List[str] = betterproto.string_field(1)
    pagination: '___cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class MsgRegisterFeeSplit(betterproto.Message):
    """MsgRegisterFeeSplit defines a message that registers a FeeSplit"""

    contract_address: str = betterproto.string_field(1)
    """contract hex address"""

    deployer_address: str = betterproto.string_field(2)
    """
    bech32 address of message sender, must be the same as the origin EOA
    sending the transaction which deploys the contract
    """

    withdrawer_address: str = betterproto.string_field(3)
    """bech32 address of account receiving the transaction fees"""

    nonces: List[int] = betterproto.uint64_field(4)
    """
    array of nonces from the address path, where the last nonce is the nonce
    that determines the contract's address - it can be an EOA nonce or a
    factory contract nonce
    """


@dataclass(eq=False, repr=False)
class MsgRegisterFeeSplitResponse(betterproto.Message):
    """
    MsgRegisterFeeSplitResponse defines the MsgRegisterFeeSplit response type
    """

    pass


@dataclass(eq=False, repr=False)
class MsgUpdateFeeSplit(betterproto.Message):
    """
    MsgUpdateFeeSplit defines a message that updates the withdrawer address for a
    registered FeeSplit
    """

    contract_address: str = betterproto.string_field(1)
    """contract hex address"""

    deployer_address: str = betterproto.string_field(2)
    """deployer bech32 address"""

    withdrawer_address: str = betterproto.string_field(3)
    """new withdrawer bech32 address for receiving the transaction fees"""


@dataclass(eq=False, repr=False)
class MsgUpdateFeeSplitResponse(betterproto.Message):
    """
    MsgUpdateFeeSplitResponse defines the MsgUpdateFeeSplit response type
    """

    pass


@dataclass(eq=False, repr=False)
class MsgCancelFeeSplit(betterproto.Message):
    """
    MsgCancelFeeSplit defines a message that cancels a registered FeeSplit
    """

    contract_address: str = betterproto.string_field(1)
    """contract hex address"""

    deployer_address: str = betterproto.string_field(2)
    """deployer bech32 address"""


@dataclass(eq=False, repr=False)
class MsgCancelFeeSplitResponse(betterproto.Message):
    """
    MsgCancelFeeSplitResponse defines the MsgCancelFeeSplit response type
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def fee_splits(
        self,
        query_fee_splits_request: 'QueryFeeSplitsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryFeeSplitsResponse':
        return await self._unary_unary(
            '/evmos.feesplit.v1.Query/FeeSplits',
            query_fee_splits_request,
            QueryFeeSplitsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def fee_split(
        self,
        query_fee_split_request: 'QueryFeeSplitRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryFeeSplitResponse':
        return await self._unary_unary(
            '/evmos.feesplit.v1.Query/FeeSplit',
            query_fee_split_request,
            QueryFeeSplitResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def params(
        self,
        query_params_request: 'QueryParamsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryParamsResponse':
        return await self._unary_unary(
            '/evmos.feesplit.v1.Query/Params',
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def deployer_fee_splits(
        self,
        query_deployer_fee_splits_request: 'QueryDeployerFeeSplitsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryDeployerFeeSplitsResponse':
        return await self._unary_unary(
            '/evmos.feesplit.v1.Query/DeployerFeeSplits',
            query_deployer_fee_splits_request,
            QueryDeployerFeeSplitsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def withdrawer_fee_splits(
        self,
        query_withdrawer_fee_splits_request: 'QueryWithdrawerFeeSplitsRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryWithdrawerFeeSplitsResponse':
        return await self._unary_unary(
            '/evmos.feesplit.v1.Query/WithdrawerFeeSplits',
            query_withdrawer_fee_splits_request,
            QueryWithdrawerFeeSplitsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def register_fee_split(
        self,
        msg_register_fee_split: 'MsgRegisterFeeSplit',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgRegisterFeeSplitResponse':
        return await self._unary_unary(
            '/evmos.feesplit.v1.Msg/RegisterFeeSplit',
            msg_register_fee_split,
            MsgRegisterFeeSplitResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def update_fee_split(
        self,
        msg_update_fee_split: 'MsgUpdateFeeSplit',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgUpdateFeeSplitResponse':
        return await self._unary_unary(
            '/evmos.feesplit.v1.Msg/UpdateFeeSplit',
            msg_update_fee_split,
            MsgUpdateFeeSplitResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def cancel_fee_split(
        self,
        msg_cancel_fee_split: 'MsgCancelFeeSplit',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgCancelFeeSplitResponse':
        return await self._unary_unary(
            '/evmos.feesplit.v1.Msg/CancelFeeSplit',
            msg_cancel_fee_split,
            MsgCancelFeeSplitResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def fee_splits(
        self, query_fee_splits_request: 'QueryFeeSplitsRequest'
    ) -> 'QueryFeeSplitsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def fee_split(
        self, query_fee_split_request: 'QueryFeeSplitRequest'
    ) -> 'QueryFeeSplitResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(
        self, query_params_request: 'QueryParamsRequest'
    ) -> 'QueryParamsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def deployer_fee_splits(
        self, query_deployer_fee_splits_request: 'QueryDeployerFeeSplitsRequest'
    ) -> 'QueryDeployerFeeSplitsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def withdrawer_fee_splits(
        self, query_withdrawer_fee_splits_request: 'QueryWithdrawerFeeSplitsRequest'
    ) -> 'QueryWithdrawerFeeSplitsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_fee_splits(
        self,
        stream: 'grpclib.server.Stream[QueryFeeSplitsRequest, QueryFeeSplitsResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.fee_splits(request)
        await stream.send_message(response)

    async def __rpc_fee_split(
        self,
        stream: 'grpclib.server.Stream[QueryFeeSplitRequest, QueryFeeSplitResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.fee_split(request)
        await stream.send_message(response)

    async def __rpc_params(
        self, stream: 'grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_deployer_fee_splits(
        self,
        stream: 'grpclib.server.Stream[QueryDeployerFeeSplitsRequest, QueryDeployerFeeSplitsResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.deployer_fee_splits(request)
        await stream.send_message(response)

    async def __rpc_withdrawer_fee_splits(
        self,
        stream: 'grpclib.server.Stream[QueryWithdrawerFeeSplitsRequest, QueryWithdrawerFeeSplitsResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.withdrawer_fee_splits(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/evmos.feesplit.v1.Query/FeeSplits': grpclib.const.Handler(
                self.__rpc_fee_splits,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryFeeSplitsRequest,
                QueryFeeSplitsResponse,
            ),
            '/evmos.feesplit.v1.Query/FeeSplit': grpclib.const.Handler(
                self.__rpc_fee_split,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryFeeSplitRequest,
                QueryFeeSplitResponse,
            ),
            '/evmos.feesplit.v1.Query/Params': grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            '/evmos.feesplit.v1.Query/DeployerFeeSplits': grpclib.const.Handler(
                self.__rpc_deployer_fee_splits,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDeployerFeeSplitsRequest,
                QueryDeployerFeeSplitsResponse,
            ),
            '/evmos.feesplit.v1.Query/WithdrawerFeeSplits': grpclib.const.Handler(
                self.__rpc_withdrawer_fee_splits,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryWithdrawerFeeSplitsRequest,
                QueryWithdrawerFeeSplitsResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def register_fee_split(
        self, msg_register_fee_split: 'MsgRegisterFeeSplit'
    ) -> 'MsgRegisterFeeSplitResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_fee_split(
        self, msg_update_fee_split: 'MsgUpdateFeeSplit'
    ) -> 'MsgUpdateFeeSplitResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def cancel_fee_split(
        self, msg_cancel_fee_split: 'MsgCancelFeeSplit'
    ) -> 'MsgCancelFeeSplitResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_register_fee_split(
        self,
        stream: 'grpclib.server.Stream[MsgRegisterFeeSplit, MsgRegisterFeeSplitResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.register_fee_split(request)
        await stream.send_message(response)

    async def __rpc_update_fee_split(
        self,
        stream: 'grpclib.server.Stream[MsgUpdateFeeSplit, MsgUpdateFeeSplitResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_fee_split(request)
        await stream.send_message(response)

    async def __rpc_cancel_fee_split(
        self,
        stream: 'grpclib.server.Stream[MsgCancelFeeSplit, MsgCancelFeeSplitResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.cancel_fee_split(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/evmos.feesplit.v1.Msg/RegisterFeeSplit': grpclib.const.Handler(
                self.__rpc_register_fee_split,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgRegisterFeeSplit,
                MsgRegisterFeeSplitResponse,
            ),
            '/evmos.feesplit.v1.Msg/UpdateFeeSplit': grpclib.const.Handler(
                self.__rpc_update_fee_split,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateFeeSplit,
                MsgUpdateFeeSplitResponse,
            ),
            '/evmos.feesplit.v1.Msg/CancelFeeSplit': grpclib.const.Handler(
                self.__rpc_cancel_fee_split,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgCancelFeeSplit,
                MsgCancelFeeSplitResponse,
            ),
        }
