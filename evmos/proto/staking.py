from __future__ import annotations

from evmos.proto.autogen.py.cosmos.base.v1beta1 import Coin
from evmos.proto.autogen.py.cosmos.distribution.v1beta1 import (
    MsgSetWithdrawAddress,
    MsgWithdrawDelegatorReward,
    MsgWithdrawValidatorCommission,
)
from evmos.proto.autogen.py.cosmos.staking.v1beta1 import (
    MsgBeginRedelegate,
    MsgDelegate,
    MsgUndelegate,
)
from evmos.proto.utils import MessageGenerated


def create_msg_delegate(
    delegator_address: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> MessageGenerated[MsgDelegate]:
    """Create a message for staking delegation."""
    value = Coin(denom=denom, amount=amount)

    message = MsgDelegate(
        delegator_address=delegator_address,
        validator_address=validator_address,
        amount=value,
    )

    return MessageGenerated(
        message=message,
        path="cosmos.staking.v1beta1.MsgDelegate",
    )


def create_msg_begin_redelegate(
    delegator_address: str,
    validator_src_address: str,
    validator_dst_address: str,
    amount: str,
    denom: str,
) -> MessageGenerated[MsgBeginRedelegate]:
    """Create a message for staking redelegation."""
    value = Coin(denom=denom, amount=amount)

    message = MsgBeginRedelegate(
        delegator_address=delegator_address,
        validator_src_address=validator_src_address,
        validator_dst_address=validator_dst_address,
        amount=value,
    )

    return MessageGenerated(
        message=message,
        path="cosmos.staking.v1beta1.MsgBeginRedelegate",
    )


def create_msg_undelegate(
    delegator_address: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> MessageGenerated[MsgUndelegate]:
    """Create a message for staking undelegation."""
    value = Coin(denom=denom, amount=amount)

    message = MsgUndelegate(
        delegator_address=delegator_address,
        validator_address=validator_address,
        amount=value,
    )

    return MessageGenerated(
        message=message,
        path="cosmos.staking.v1beta1.MsgUndelegate",
    )


def create_msg_withdraw_delegator_reward(
    delegator_address: str,
    validator_address: str,
) -> MessageGenerated[MsgWithdrawDelegatorReward]:
    """Create a message for delegator rewards withdrawal."""
    message = MsgWithdrawDelegatorReward(
        delegator_address=delegator_address,
        validator_address=validator_address,
    )

    return MessageGenerated(
        message=message,
        path="cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward",
    )


def create_msg_withdraw_validator_commission(
    validator_address: str,
) -> MessageGenerated[MsgWithdrawValidatorCommission]:
    """Create a message for validator commission withdrawal."""
    message = MsgWithdrawValidatorCommission(
        validator_address=validator_address,
    )

    return MessageGenerated(
        message=message,
        path="cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission",
    )


def create_msg_set_withdraw_address(
    delegator_address: str,
    withdraw_address: str,
) -> MessageGenerated[MsgSetWithdrawAddress]:
    """Create a message for withdrawal address setting."""
    message = MsgSetWithdrawAddress(
        delegator_address=delegator_address,
        withdraw_address=withdraw_address,
    )

    return MessageGenerated(
        message=message,
        path="cosmos.distribution.v1beta1.MsgSetWithdrawAddress",
    )
