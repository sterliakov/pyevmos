# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ethermint/feemarket/v1/feemarket.proto, ethermint/feemarket/v1/genesis.proto, ethermint/feemarket/v1/query.proto
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


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the EVM module parameters"""

    no_base_fee: bool = betterproto.bool_field(1)
    """no base fee forces the EIP-1559 base fee to 0 (needed for 0 price calls)"""

    base_fee_change_denominator: int = betterproto.uint32_field(2)
    """
    base fee change denominator bounds the amount the base fee can change
    between blocks.
    """

    elasticity_multiplier: int = betterproto.uint32_field(3)
    """
    elasticity multiplier bounds the maximum gas limit an EIP-1559 block may
    have.
    """

    enable_height: int = betterproto.int64_field(5)
    """height at which the base fee calculation is enabled."""

    base_fee: str = betterproto.string_field(6)
    """base fee for EIP-1559 blocks."""

    min_gas_price: str = betterproto.string_field(7)
    """
    min_gas_price defines the minimum gas price value for cosmos and eth transactions
    """

    min_gas_multiplier: str = betterproto.string_field(8)
    """
    min gas denominator bounds the minimum gasUsed to be charged
    to senders based on GasLimit
    """


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest defines the request type for querying x/evm parameters."""

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """QueryParamsResponse defines the response type for querying x/evm parameters."""

    params: 'Params' = betterproto.message_field(1)
    """params define the evm module parameters."""


@dataclass(eq=False, repr=False)
class QueryBaseFeeRequest(betterproto.Message):
    """
    QueryBaseFeeRequest defines the request type for querying the EIP1559 base
    fee.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryBaseFeeResponse(betterproto.Message):
    """BaseFeeResponse returns the EIP1559 base fee."""

    base_fee: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryBlockGasRequest(betterproto.Message):
    """
    QueryBlockGasRequest defines the request type for querying the EIP1559 base
    fee.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryBlockGasResponse(betterproto.Message):
    """QueryBlockGasResponse returns block gas used for a given height."""

    gas: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the feemarket module's genesis state."""

    params: 'Params' = betterproto.message_field(1)
    """params defines all the paramaters of the module."""

    block_gas: int = betterproto.uint64_field(3)
    """
    block gas is the amount of gas wanted on the last block before the upgrade.
    Zero by default.
    """


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
            '/ethermint.feemarket.v1.Query/Params',
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def base_fee(
        self,
        query_base_fee_request: 'QueryBaseFeeRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryBaseFeeResponse':
        return await self._unary_unary(
            '/ethermint.feemarket.v1.Query/BaseFee',
            query_base_fee_request,
            QueryBaseFeeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def block_gas(
        self,
        query_block_gas_request: 'QueryBlockGasRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryBlockGasResponse':
        return await self._unary_unary(
            '/ethermint.feemarket.v1.Query/BlockGas',
            query_block_gas_request,
            QueryBlockGasResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def params(
        self, query_params_request: 'QueryParamsRequest'
    ) -> 'QueryParamsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def base_fee(
        self, query_base_fee_request: 'QueryBaseFeeRequest'
    ) -> 'QueryBaseFeeResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def block_gas(
        self, query_block_gas_request: 'QueryBlockGasRequest'
    ) -> 'QueryBlockGasResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(
        self, stream: 'grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_base_fee(
        self, stream: 'grpclib.server.Stream[QueryBaseFeeRequest, QueryBaseFeeResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.base_fee(request)
        await stream.send_message(response)

    async def __rpc_block_gas(
        self,
        stream: 'grpclib.server.Stream[QueryBlockGasRequest, QueryBlockGasResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.block_gas(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/ethermint.feemarket.v1.Query/Params': grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            '/ethermint.feemarket.v1.Query/BaseFee': grpclib.const.Handler(
                self.__rpc_base_fee,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryBaseFeeRequest,
                QueryBaseFeeResponse,
            ),
            '/ethermint.feemarket.v1.Query/BlockGas': grpclib.const.Handler(
                self.__rpc_block_gas,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryBlockGasRequest,
                QueryBlockGasResponse,
            ),
        }
