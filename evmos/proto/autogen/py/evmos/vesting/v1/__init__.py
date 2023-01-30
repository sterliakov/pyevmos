# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: evmos/vesting/v1/query.proto, evmos/vesting/v1/tx.proto, evmos/vesting/v1/vesting.proto
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
from ....cosmos.vesting import v1beta1 as ___cosmos_vesting_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class QueryBalancesRequest(betterproto.Message):
    """QueryBalancesRequest is the request type for the Query/Balances RPC method."""

    address: str = betterproto.string_field(1)
    """address of the clawback vesting account"""


@dataclass(eq=False, repr=False)
class QueryBalancesResponse(betterproto.Message):
    """
    QueryBalancesResponse is the response type for the Query/Balances RPC
    method.
    """

    locked: List['___cosmos_base_v1_beta1__.Coin'] = betterproto.message_field(1)
    """current amount of locked tokens"""

    unvested: List['___cosmos_base_v1_beta1__.Coin'] = betterproto.message_field(2)
    """current amount of unvested tokens"""

    vested: List['___cosmos_base_v1_beta1__.Coin'] = betterproto.message_field(3)
    """current amount of vested tokens"""


@dataclass(eq=False, repr=False)
class ClawbackVestingAccount(betterproto.Message):
    """
    ClawbackVestingAccount implements the VestingAccount interface. It provides
    an account that can hold contributions subject to "lockup" (like a
    PeriodicVestingAccount), or vesting which is subject to clawback
    of unvested tokens, or a combination (tokens vest, but are still locked).
    """

    base_vesting_account: '___cosmos_vesting_v1_beta1__.BaseVestingAccount' = (
        betterproto.message_field(1)
    )
    """
    base_vesting_account implements the VestingAccount interface. It contains
    all the necessary fields needed for any vesting account implementation
    """

    funder_address: str = betterproto.string_field(2)
    """funder_address specifies the account which can perform clawback"""

    start_time: datetime = betterproto.message_field(3)
    """start_time defines the time at which the vesting period begins"""

    lockup_periods: List[
        '___cosmos_vesting_v1_beta1__.Period'
    ] = betterproto.message_field(4)
    """lockup_periods defines the unlocking schedule relative to the start_time"""

    vesting_periods: List[
        '___cosmos_vesting_v1_beta1__.Period'
    ] = betterproto.message_field(5)
    """vesting_periods defines the vesting schedule relative to the start_time"""


@dataclass(eq=False, repr=False)
class MsgCreateClawbackVestingAccount(betterproto.Message):
    """
    MsgCreateClawbackVestingAccount defines a message that enables creating a
    ClawbackVestingAccount.
    """

    from_address: str = betterproto.string_field(1)
    """
    from_address specifies the account to provide the funds and sign the
    clawback request
    """

    to_address: str = betterproto.string_field(2)
    """to_address specifies the account to receive the funds"""

    start_time: datetime = betterproto.message_field(3)
    """start_time defines the time at which the vesting period begins"""

    lockup_periods: List[
        '___cosmos_vesting_v1_beta1__.Period'
    ] = betterproto.message_field(4)
    """lockup_periods defines the unlocking schedule relative to the start_time"""

    vesting_periods: List[
        '___cosmos_vesting_v1_beta1__.Period'
    ] = betterproto.message_field(5)
    """vesting_periods defines thevesting schedule relative to the start_time"""

    merge: bool = betterproto.bool_field(6)
    """
    merge specifies a the creation mechanism for existing
    ClawbackVestingAccounts. If true, merge this new grant into an existing
    ClawbackVestingAccount, or create it if it does not exist. If false,
    creates a new account. New grants to an existing account must be from the
    same from_address.
    """


@dataclass(eq=False, repr=False)
class MsgCreateClawbackVestingAccountResponse(betterproto.Message):
    """
    MsgCreateClawbackVestingAccountResponse defines the
    MsgCreateClawbackVestingAccount response type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgClawback(betterproto.Message):
    """
    MsgClawback defines a message that removes unvested tokens from a
    ClawbackVestingAccount.
    """

    funder_address: str = betterproto.string_field(1)
    """funder_address is the address which funded the account"""

    account_address: str = betterproto.string_field(2)
    """
    account_address is the address of the ClawbackVestingAccount to claw back
    from.
    """

    dest_address: str = betterproto.string_field(3)
    """
    dest_address specifies where the clawed-back tokens should be transferred
    to. If empty, the tokens will be transferred back to the original funder of
    the account.
    """


@dataclass(eq=False, repr=False)
class MsgClawbackResponse(betterproto.Message):
    """MsgClawbackResponse defines the MsgClawback response type."""

    pass


class QueryStub(betterproto.ServiceStub):
    async def balances(
        self,
        query_balances_request: 'QueryBalancesRequest',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'QueryBalancesResponse':
        return await self._unary_unary(
            '/evmos.vesting.v1.Query/Balances',
            query_balances_request,
            QueryBalancesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def create_clawback_vesting_account(
        self,
        msg_create_clawback_vesting_account: 'MsgCreateClawbackVestingAccount',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgCreateClawbackVestingAccountResponse':
        return await self._unary_unary(
            '/evmos.vesting.v1.Msg/CreateClawbackVestingAccount',
            msg_create_clawback_vesting_account,
            MsgCreateClawbackVestingAccountResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def clawback(
        self,
        msg_clawback: 'MsgClawback',
        *,
        timeout: Optional[float] = None,
        deadline: Optional['Deadline'] = None,
        metadata: Optional['MetadataLike'] = None
    ) -> 'MsgClawbackResponse':
        return await self._unary_unary(
            '/evmos.vesting.v1.Msg/Clawback',
            msg_clawback,
            MsgClawbackResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def balances(
        self, query_balances_request: 'QueryBalancesRequest'
    ) -> 'QueryBalancesResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_balances(
        self,
        stream: 'grpclib.server.Stream[QueryBalancesRequest, QueryBalancesResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.balances(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/evmos.vesting.v1.Query/Balances': grpclib.const.Handler(
                self.__rpc_balances,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryBalancesRequest,
                QueryBalancesResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def create_clawback_vesting_account(
        self, msg_create_clawback_vesting_account: 'MsgCreateClawbackVestingAccount'
    ) -> 'MsgCreateClawbackVestingAccountResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def clawback(self, msg_clawback: 'MsgClawback') -> 'MsgClawbackResponse':
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_create_clawback_vesting_account(
        self,
        stream: 'grpclib.server.Stream[MsgCreateClawbackVestingAccount, MsgCreateClawbackVestingAccountResponse]',
    ) -> None:
        request = await stream.recv_message()
        response = await self.create_clawback_vesting_account(request)
        await stream.send_message(response)

    async def __rpc_clawback(
        self, stream: 'grpclib.server.Stream[MsgClawback, MsgClawbackResponse]'
    ) -> None:
        request = await stream.recv_message()
        response = await self.clawback(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            '/evmos.vesting.v1.Msg/CreateClawbackVestingAccount': grpclib.const.Handler(
                self.__rpc_create_clawback_vesting_account,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgCreateClawbackVestingAccount,
                MsgCreateClawbackVestingAccountResponse,
            ),
            '/evmos.vesting.v1.Msg/Clawback': grpclib.const.Handler(
                self.__rpc_clawback,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgClawback,
                MsgClawbackResponse,
            ),
        }
