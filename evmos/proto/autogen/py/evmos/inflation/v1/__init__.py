# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: evmos/inflation/v1/genesis.proto, evmos/inflation/v1/inflation.proto, evmos/inflation/v1/query.proto, evmos/inflation/v1/tx.proto
# plugin: python-betterproto
# This file has been @generated
import warnings
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ....cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class InflationDistribution(betterproto.Message):
    """
    InflationDistribution defines the distribution in which inflation is
    allocated through minting on each epoch (staking, incentives, community). It
    excludes the team vesting distribution, as this is minted once at genesis.
    The initial InflationDistribution can be calculated from the Evmos Token
    Model like this:
    mintDistribution1 = distribution1 / (1 - teamVestingDistribution)
    0.5333333         = 40%           / (1 - 25%)
    """

    staking_rewards: str = betterproto.string_field(1)
    """
    staking_rewards defines the proportion of the minted minted_denom that is
    to be allocated as staking rewards
    """

    usage_incentives: str = betterproto.string_field(2)
    """
    Deprecated: usage_incentives defines the proportion of the minted minted_denom that
    is
    to be allocated to the incentives module address
    """

    community_pool: str = betterproto.string_field(3)
    """
    community_pool defines the proportion of the minted minted_denom that is to
    be allocated to the community pool
    """

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.is_set("usage_incentives"):
            warnings.warn(
                "InflationDistribution.usage_incentives is deprecated",
                DeprecationWarning,
            )


@dataclass(eq=False, repr=False)
class ExponentialCalculation(betterproto.Message):
    """
    ExponentialCalculation holds factors to calculate exponential inflation on
    each period. Calculation reference:
    periodProvision = exponentialDecay       *  bondingIncentive
    f(x)            = (a * (1 - r) ^ x + c)  *  (1 + max_variance - bondedRatio *
    (max_variance / bonding_target))
    """

    a: str = betterproto.string_field(1)
    """a defines the initial value"""

    r: str = betterproto.string_field(2)
    """r defines the reduction factor"""

    c: str = betterproto.string_field(3)
    """c defines the parameter for long term inflation"""

    bonding_target: str = betterproto.string_field(4)
    """bonding_target"""

    max_variance: str = betterproto.string_field(5)
    """max_variance"""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the inflation module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    """params defines all the parameters of the module."""

    period: int = betterproto.uint64_field(2)
    """period is the amount of past periods, based on the epochs per period param"""

    epoch_identifier: str = betterproto.string_field(3)
    """epoch_identifier for inflation"""

    epochs_per_period: int = betterproto.int64_field(4)
    """
    epochs_per_period is the number of epochs after which inflation is recalculated
    """

    skipped_epochs: int = betterproto.uint64_field(5)
    """
    skipped_epochs is the number of epochs that have passed while inflation is disabled
    """


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params holds parameters for the inflation module."""

    mint_denom: str = betterproto.string_field(1)
    """mint_denom specifies the type of coin to mint"""

    exponential_calculation: "ExponentialCalculation" = betterproto.message_field(2)
    """
    exponential_calculation takes in the variables to calculate exponential inflation
    """

    inflation_distribution: "InflationDistribution" = betterproto.message_field(3)
    """inflation_distribution of the minted denom"""

    enable_inflation: bool = betterproto.bool_field(4)
    """
    enable_inflation is the parameter that enables inflation and halts increasing the
    skipped_epochs
    """


@dataclass(eq=False, repr=False)
class QueryPeriodRequest(betterproto.Message):
    """QueryPeriodRequest is the request type for the Query/Period RPC method."""

    pass


@dataclass(eq=False, repr=False)
class QueryPeriodResponse(betterproto.Message):
    """QueryPeriodResponse is the response type for the Query/Period RPC method."""

    period: int = betterproto.uint64_field(1)
    """period is the current minting per epoch provision value."""


@dataclass(eq=False, repr=False)
class QueryEpochMintProvisionRequest(betterproto.Message):
    """
    QueryEpochMintProvisionRequest is the request type for the
    Query/EpochMintProvision RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryEpochMintProvisionResponse(betterproto.Message):
    """
    QueryEpochMintProvisionResponse is the response type for the
    Query/EpochMintProvision RPC method.
    """

    epoch_mint_provision: "___cosmos_base_v1_beta1__.DecCoin" = (
        betterproto.message_field(1)
    )
    """epoch_mint_provision is the current minting per epoch provision value."""


@dataclass(eq=False, repr=False)
class QuerySkippedEpochsRequest(betterproto.Message):
    """
    QuerySkippedEpochsRequest is the request type for the Query/SkippedEpochs RPC
    method.
    """

    pass


@dataclass(eq=False, repr=False)
class QuerySkippedEpochsResponse(betterproto.Message):
    """
    QuerySkippedEpochsResponse is the response type for the Query/SkippedEpochs
    RPC method.
    """

    skipped_epochs: int = betterproto.uint64_field(1)
    """
    skipped_epochs is the number of epochs that the inflation module has been disabled.
    """


@dataclass(eq=False, repr=False)
class QueryCirculatingSupplyRequest(betterproto.Message):
    """
    QueryCirculatingSupplyRequest is the request type for the
    Query/CirculatingSupply RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryCirculatingSupplyResponse(betterproto.Message):
    """
    QueryCirculatingSupplyResponse is the response type for the
    Query/CirculatingSupply RPC method.
    """

    circulating_supply: "___cosmos_base_v1_beta1__.DecCoin" = betterproto.message_field(
        1
    )
    """circulating_supply is the total amount of coins in circulation"""


@dataclass(eq=False, repr=False)
class QueryInflationRateRequest(betterproto.Message):
    """
    QueryInflationRateRequest is the request type for the Query/InflationRate RPC
    method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryInflationRateResponse(betterproto.Message):
    """
    QueryInflationRateResponse is the response type for the Query/InflationRate
    RPC method.
    """

    inflation_rate: str = betterproto.string_field(1)
    """inflation_rate by which the total supply increases within one period"""


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""

    params: "Params" = betterproto.message_field(1)
    """params defines the parameters of the module."""


@dataclass(eq=False, repr=False)
class MsgUpdateParams(betterproto.Message):
    """MsgUpdateParams defines a Msg for updating the x/inflation module parameters."""

    authority: str = betterproto.string_field(1)
    """authority is the address of the governance account."""

    params: "Params" = betterproto.message_field(2)
    """
    params defines the x/inflation parameters to update.
    NOTE: All parameters must be supplied.
    """


@dataclass(eq=False, repr=False)
class MsgUpdateParamsResponse(betterproto.Message):
    """
    MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message.
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def period(
        self,
        query_period_request: "QueryPeriodRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryPeriodResponse":
        return await self._unary_unary(
            "/evmos.inflation.v1.Query/Period",
            query_period_request,
            QueryPeriodResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def epoch_mint_provision(
        self,
        query_epoch_mint_provision_request: "QueryEpochMintProvisionRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryEpochMintProvisionResponse":
        return await self._unary_unary(
            "/evmos.inflation.v1.Query/EpochMintProvision",
            query_epoch_mint_provision_request,
            QueryEpochMintProvisionResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def skipped_epochs(
        self,
        query_skipped_epochs_request: "QuerySkippedEpochsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QuerySkippedEpochsResponse":
        return await self._unary_unary(
            "/evmos.inflation.v1.Query/SkippedEpochs",
            query_skipped_epochs_request,
            QuerySkippedEpochsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def circulating_supply(
        self,
        query_circulating_supply_request: "QueryCirculatingSupplyRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryCirculatingSupplyResponse":
        return await self._unary_unary(
            "/evmos.inflation.v1.Query/CirculatingSupply",
            query_circulating_supply_request,
            QueryCirculatingSupplyResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def inflation_rate(
        self,
        query_inflation_rate_request: "QueryInflationRateRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryInflationRateResponse":
        return await self._unary_unary(
            "/evmos.inflation.v1.Query/InflationRate",
            query_inflation_rate_request,
            QueryInflationRateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/evmos.inflation.v1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def update_params(
        self,
        msg_update_params: "MsgUpdateParams",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "MsgUpdateParamsResponse":
        return await self._unary_unary(
            "/evmos.inflation.v1.Msg/UpdateParams",
            msg_update_params,
            MsgUpdateParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def period(
        self, query_period_request: "QueryPeriodRequest"
    ) -> "QueryPeriodResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def epoch_mint_provision(
        self, query_epoch_mint_provision_request: "QueryEpochMintProvisionRequest"
    ) -> "QueryEpochMintProvisionResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def skipped_epochs(
        self, query_skipped_epochs_request: "QuerySkippedEpochsRequest"
    ) -> "QuerySkippedEpochsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def circulating_supply(
        self, query_circulating_supply_request: "QueryCirculatingSupplyRequest"
    ) -> "QueryCirculatingSupplyResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def inflation_rate(
        self, query_inflation_rate_request: "QueryInflationRateRequest"
    ) -> "QueryInflationRateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(
        self, query_params_request: "QueryParamsRequest"
    ) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_period(
        self, stream: "grpclib.server.Stream[QueryPeriodRequest, QueryPeriodResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.period(request)
        await stream.send_message(response)

    async def __rpc_epoch_mint_provision(
        self,
        stream: "grpclib.server.Stream[QueryEpochMintProvisionRequest, QueryEpochMintProvisionResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.epoch_mint_provision(request)
        await stream.send_message(response)

    async def __rpc_skipped_epochs(
        self,
        stream: "grpclib.server.Stream[QuerySkippedEpochsRequest, QuerySkippedEpochsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.skipped_epochs(request)
        await stream.send_message(response)

    async def __rpc_circulating_supply(
        self,
        stream: "grpclib.server.Stream[QueryCirculatingSupplyRequest, QueryCirculatingSupplyResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.circulating_supply(request)
        await stream.send_message(response)

    async def __rpc_inflation_rate(
        self,
        stream: "grpclib.server.Stream[QueryInflationRateRequest, QueryInflationRateResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.inflation_rate(request)
        await stream.send_message(response)

    async def __rpc_params(
        self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/evmos.inflation.v1.Query/Period": grpclib.const.Handler(
                self.__rpc_period,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryPeriodRequest,
                QueryPeriodResponse,
            ),
            "/evmos.inflation.v1.Query/EpochMintProvision": grpclib.const.Handler(
                self.__rpc_epoch_mint_provision,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryEpochMintProvisionRequest,
                QueryEpochMintProvisionResponse,
            ),
            "/evmos.inflation.v1.Query/SkippedEpochs": grpclib.const.Handler(
                self.__rpc_skipped_epochs,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySkippedEpochsRequest,
                QuerySkippedEpochsResponse,
            ),
            "/evmos.inflation.v1.Query/CirculatingSupply": grpclib.const.Handler(
                self.__rpc_circulating_supply,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryCirculatingSupplyRequest,
                QueryCirculatingSupplyResponse,
            ),
            "/evmos.inflation.v1.Query/InflationRate": grpclib.const.Handler(
                self.__rpc_inflation_rate,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryInflationRateRequest,
                QueryInflationRateResponse,
            ),
            "/evmos.inflation.v1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def update_params(
        self, msg_update_params: "MsgUpdateParams"
    ) -> "MsgUpdateParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_update_params(
        self, stream: "grpclib.server.Stream[MsgUpdateParams, MsgUpdateParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/evmos.inflation.v1.Msg/UpdateParams": grpclib.const.Handler(
                self.__rpc_update_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateParams,
                MsgUpdateParamsResponse,
            ),
        }
