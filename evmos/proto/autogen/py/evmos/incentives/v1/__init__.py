# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: evmos/incentives/v1/genesis.proto, evmos/incentives/v1/incentives.proto, evmos/incentives/v1/query.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ....cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__
from ....cosmos.base.query import v1beta1 as ___cosmos_base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class Incentive(betterproto.Message):
    """
    Incentive defines an instance that organizes distribution conditions for a
    given smart contract
    """

    contract: str = betterproto.string_field(1)
    """contract address"""

    allocations: List['___cosmos_base_v1_beta1__.DecCoin'] = betterproto.message_field(
        2
    )
    """denoms and percentage of rewards to be allocated"""

    epochs: int = betterproto.uint32_field(3)
    """number of remaining epochs"""

    start_time: datetime = betterproto.message_field(4)
    """distribution start time"""

    total_gas: int = betterproto.uint64_field(5)
    """
    cumulative gas spent by all gasmeters of the incentive during the epoch
    """


@dataclass(eq=False, repr=False)
class GasMeter(betterproto.Message):
    """
    GasMeter tracks the cumulative gas spent per participant in one epoch
    """

    contract: str = betterproto.string_field(1)
    """hex address of the incentivized contract"""

    participant: str = betterproto.string_field(2)
    """participant address that interacts with the incentive"""

    cumulative_gas: int = betterproto.uint64_field(3)
    """cumulative gas spent during the epoch"""


@dataclass(eq=False, repr=False)
class RegisterIncentiveProposal(betterproto.Message):
    """
    RegisterIncentiveProposal is a gov Content type to register an incentive
    """

    title: str = betterproto.string_field(1)
    """title of the proposal"""

    description: str = betterproto.string_field(2)
    """proposal description"""

    contract: str = betterproto.string_field(3)
    """contract address"""

    allocations: List['___cosmos_base_v1_beta1__.DecCoin'] = betterproto.message_field(
        4
    )
    """denoms and percentage of rewards to be allocated"""

    epochs: int = betterproto.uint32_field(5)
    """number of remaining epochs"""


@dataclass(eq=False, repr=False)
class CancelIncentiveProposal(betterproto.Message):
    """CancelIncentiveProposal is a gov Content type to cancel an incentive"""

    title: str = betterproto.string_field(1)
    """title of the proposal"""

    description: str = betterproto.string_field(2)
    """proposal description"""

    contract: str = betterproto.string_field(3)
    """contract address"""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the module's genesis state."""

    params: 'Params' = betterproto.message_field(1)
    """module parameters"""

    incentives: List['Incentive'] = betterproto.message_field(2)
    """active incentives"""

    gas_meters: List['GasMeter'] = betterproto.message_field(3)
    """active Gasmeters"""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the incentives module params"""

    enable_incentives: bool = betterproto.bool_field(1)
    """parameter to enable incentives"""

    allocation_limit: str = betterproto.string_field(2)
    """maximum percentage an incentive can allocate per denomination"""

    incentives_epoch_identifier: str = betterproto.string_field(3)
    """identifier for the epochs module hooks"""

    reward_scaler: str = betterproto.string_field(4)
    """scaling factor for capping rewards"""


@dataclass(eq=False, repr=False)
class QueryIncentivesRequest(betterproto.Message):
    """
    QueryIncentivesRequest is the request type for the Query/Incentives RPC
    method.
    """

    pagination: '___cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(1)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryIncentivesResponse(betterproto.Message):
    """
    QueryIncentivesResponse is the response type for the Query/Incentives RPC
    method.
    """

    incentives: List['Incentive'] = betterproto.message_field(1)
    pagination: '___cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryIncentiveRequest(betterproto.Message):
    """
    QueryIncentiveRequest is the request type for the Query/Incentive RPC method.
    """

    contract: str = betterproto.string_field(1)
    """contract identifier is the hex contract address of a contract"""


@dataclass(eq=False, repr=False)
class QueryIncentiveResponse(betterproto.Message):
    """
    QueryIncentiveResponse is the response type for the Query/Incentive RPC
    method.
    """

    incentive: 'Incentive' = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryGasMetersRequest(betterproto.Message):
    """
    QueryGasMetersRequest is the request type for the Query/Incentives RPC
    method.
    """

    contract: str = betterproto.string_field(1)
    """
    contract is the hex contract address of a incentivized smart contract
    """

    pagination: '___cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(2)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryGasMetersResponse(betterproto.Message):
    """
    QueryGasMetersResponse is the response type for the Query/Incentives RPC
    method.
    """

    gas_meters: List['GasMeter'] = betterproto.message_field(1)
    pagination: '___cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryGasMeterRequest(betterproto.Message):
    """
    QueryGasMeterRequest is the request type for the Query/Incentive RPC method.
    """

    contract: str = betterproto.string_field(1)
    """contract identifier is the hex contract address of a contract"""

    participant: str = betterproto.string_field(2)
    """participant identifier is the hex address of a user"""


@dataclass(eq=False, repr=False)
class QueryGasMeterResponse(betterproto.Message):
    """
    QueryGasMeterResponse is the response type for the Query/Incentive RPC
    method.
    """

    gas_meter: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QueryAllocationMetersRequest(betterproto.Message):
    """
    QueryAllocationMetersRequest is the request type for the
    Query/AllocationMeters RPC method.
    """

    pagination: '___cosmos_base_query_v1_beta1__.PageRequest' = (
        betterproto.message_field(1)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryAllocationMetersResponse(betterproto.Message):
    """
    QueryAllocationMetersResponse is the response type for the
    Query/AllocationMeters RPC method.
    """

    allocation_meters: List[
        '___cosmos_base_v1_beta1__.DecCoin'
    ] = betterproto.message_field(1)
    pagination: '___cosmos_base_query_v1_beta1__.PageResponse' = (
        betterproto.message_field(2)
    )
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryAllocationMeterRequest(betterproto.Message):
    """
    QueryAllocationMeterRequest is the request type for the Query/AllocationMeter
    RPC method.
    """

    denom: str = betterproto.string_field(1)
    """denom is the coin denom to query an allocation meter for."""


@dataclass(eq=False, repr=False)
class QueryAllocationMeterResponse(betterproto.Message):
    """
    QueryAllocationMeterResponse is the response type for the
    Query/AllocationMeter RPC method.
    """

    allocation_meter: '___cosmos_base_v1_beta1__.DecCoin' = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC
    method.
    """

    params: 'Params' = betterproto.message_field(1)


class QueryStub(betterproto.ServiceStub):
    async def incentives(
        self,
        query_incentives_request: 'QueryIncentivesRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryIncentivesResponse':
        return await self._unary_unary(
            '/evmos.incentives.v1.Query/Incentives',
            query_incentives_request,
            QueryIncentivesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def incentive(
        self,
        query_incentive_request: 'QueryIncentiveRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryIncentiveResponse':
        return await self._unary_unary(
            '/evmos.incentives.v1.Query/Incentive',
            query_incentive_request,
            QueryIncentiveResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def gas_meters(
        self,
        query_gas_meters_request: 'QueryGasMetersRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryGasMetersResponse':
        return await self._unary_unary(
            '/evmos.incentives.v1.Query/GasMeters',
            query_gas_meters_request,
            QueryGasMetersResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def gas_meter(
        self,
        query_gas_meter_request: 'QueryGasMeterRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryGasMeterResponse':
        return await self._unary_unary(
            '/evmos.incentives.v1.Query/GasMeter',
            query_gas_meter_request,
            QueryGasMeterResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def allocation_meters(
        self,
        query_allocation_meters_request: 'QueryAllocationMetersRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryAllocationMetersResponse':
        return await self._unary_unary(
            '/evmos.incentives.v1.Query/AllocationMeters',
            query_allocation_meters_request,
            QueryAllocationMetersResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def allocation_meter(
        self,
        query_allocation_meter_request: 'QueryAllocationMeterRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryAllocationMeterResponse':
        return await self._unary_unary(
            '/evmos.incentives.v1.Query/AllocationMeter',
            query_allocation_meter_request,
            QueryAllocationMeterResponse,
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
            '/evmos.incentives.v1.Query/Params',
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def incentives(
        self, query_incentives_request: 'QueryIncentivesRequest'
    ) -> 'QueryIncentivesResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def incentive(
        self, query_incentive_request: 'QueryIncentiveRequest'
    ) -> 'QueryIncentiveResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def gas_meters(
        self, query_gas_meters_request: 'QueryGasMetersRequest'
    ) -> 'QueryGasMetersResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def gas_meter(
        self, query_gas_meter_request: 'QueryGasMeterRequest'
    ) -> 'QueryGasMeterResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def allocation_meters(
        self, query_allocation_meters_request: 'QueryAllocationMetersRequest'
    ) -> 'QueryAllocationMetersResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def allocation_meter(
        self, query_allocation_meter_request: 'QueryAllocationMeterRequest'
    ) -> 'QueryAllocationMeterResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(
        self, query_params_request: 'QueryParamsRequest'
    ) -> 'QueryParamsResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_incentives(
        self,
        stream: 'grpclib.server.Stream[QueryIncentivesRequest, QueryIncentivesResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.incentives(request)
        await stream.send_message(response)

    async def __rpc_incentive(
        self,
        stream: 'grpclib.server.Stream[QueryIncentiveRequest, QueryIncentiveResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.incentive(request)
        await stream.send_message(response)

    async def __rpc_gas_meters(
        self,
        stream: 'grpclib.server.Stream[QueryGasMetersRequest, QueryGasMetersResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.gas_meters(request)
        await stream.send_message(response)

    async def __rpc_gas_meter(
        self,
        stream: 'grpclib.server.Stream[QueryGasMeterRequest, QueryGasMeterResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.gas_meter(request)
        await stream.send_message(response)

    async def __rpc_allocation_meters(
        self,
        stream: 'grpclib.server.Stream[QueryAllocationMetersRequest, QueryAllocationMetersResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.allocation_meters(request)
        await stream.send_message(response)

    async def __rpc_allocation_meter(
        self,
        stream: 'grpclib.server.Stream[QueryAllocationMeterRequest, QueryAllocationMeterResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.allocation_meter(request)
        await stream.send_message(response)

    async def __rpc_params(
        self, stream: 'grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/evmos.incentives.v1.Query/Incentives': grpclib.const.Handler(
                self.__rpc_incentives,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryIncentivesRequest,
                QueryIncentivesResponse,
            ),
            '/evmos.incentives.v1.Query/Incentive': grpclib.const.Handler(
                self.__rpc_incentive,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryIncentiveRequest,
                QueryIncentiveResponse,
            ),
            '/evmos.incentives.v1.Query/GasMeters': grpclib.const.Handler(
                self.__rpc_gas_meters,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryGasMetersRequest,
                QueryGasMetersResponse,
            ),
            '/evmos.incentives.v1.Query/GasMeter': grpclib.const.Handler(
                self.__rpc_gas_meter,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryGasMeterRequest,
                QueryGasMeterResponse,
            ),
            '/evmos.incentives.v1.Query/AllocationMeters': grpclib.const.Handler(
                self.__rpc_allocation_meters,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllocationMetersRequest,
                QueryAllocationMetersResponse,
            ),
            '/evmos.incentives.v1.Query/AllocationMeter': grpclib.const.Handler(
                self.__rpc_allocation_meter,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllocationMeterRequest,
                QueryAllocationMeterResponse,
            ),
            '/evmos.incentives.v1.Query/Params': grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }
