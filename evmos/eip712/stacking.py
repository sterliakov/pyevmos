from __future__ import annotations

from typing import Any, Final, TypedDict

from evmos.eip712.base import _WithValidator

MSG_DELEGATE_TYPES: Final = {
    'MsgValue': [
        {'name': 'delegator_address', 'type': 'string'},
        {'name': 'validator_address', 'type': 'string'},
        {'name': 'amount', 'type': 'TypeAmount'},
    ],
    'TypeAmount': [
        {'name': 'denom', 'type': 'string'},
        {'name': 'amount', 'type': 'string'},
    ],
}
"""Types for delegation message."""


def create_msg_delegate(
    delegator_address: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> dict[str, Any]:
    """Create delegation message."""
    return {
        'type': 'cosmos-sdk/MsgDelegate',
        'value': {
            'amount': {'amount': amount, 'denom': denom},
            'delegator_address': delegator_address,
            'validator_address': validator_address,
        },
    }


MSG_BEGIN_REDELEGATE_TYPES: Final = {
    'MsgValue': [
        {'name': 'delegator_address', 'type': 'string'},
        {'name': 'validator_src_address', 'type': 'string'},
        {'name': 'validator_dst_address', 'type': 'string'},
        {'name': 'amount', 'type': 'TypeAmount'},
    ],
    'TypeAmount': [
        {'name': 'denom', 'type': 'string'},
        {'name': 'amount', 'type': 'string'},
    ],
}
"""Types for redelegation beginning message."""


def create_msg_begin_redelegate(
    delegator_address: str,
    validator_src_address: str,
    validator_dst_address: str,
    amount: str,
    denom: str,
) -> dict[str, Any]:
    """Create redelegation beginning message."""
    return {
        'type': 'cosmos-sdk/MsgBeginRedelegate',
        'value': {
            'amount': {'amount': amount, 'denom': denom},
            'delegator_address': delegator_address,
            'validator_src_address': validator_src_address,
            'validator_dst_address': validator_dst_address,
        },
    }


MSG_UNDELEGATE_TYPES: Final = {
    'MsgValue': [
        {'name': 'delegator_address', 'type': 'string'},
        {'name': 'validator_address', 'type': 'string'},
        {'name': 'amount', 'type': 'TypeAmount'},
    ],
    'TypeAmount': [
        {'name': 'denom', 'type': 'string'},
        {'name': 'amount', 'type': 'string'},
    ],
}
"""Types for delegation cancellation message."""


def create_msg_undelegate(
    delegator_address: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> dict[str, Any]:
    """Create delegation cancellation message."""
    return {
        'type': 'cosmos-sdk/MsgUndelegate',
        'value': {
            'amount': {'amount': amount, 'denom': denom},
            'delegator_address': delegator_address,
            'validator_address': validator_address,
        },
    }


MSG_WITHDRAW_DELEGATOR_REWARD_TYPES: Final = {
    'MsgValue': [
        {'name': 'delegator_address', 'type': 'string'},
        {'name': 'validator_address', 'type': 'string'},
    ],
}
"""Types for delegation reward withdrawal message."""


class _MsgValidators(TypedDict):
    delegator_address: str
    validator_address: str


class MsgWithdrawDelegatorRewardInterface(TypedDict):
    """Delegation reward withdrawal message."""

    type: str  # noqa: A003
    value: _MsgValidators


def create_msg_withdraw_delegator_reward(
    delegator_address: str,
    validator_address: str,
) -> MsgWithdrawDelegatorRewardInterface:
    """Create delegation reward withdrawal message."""
    return {
        'type': 'cosmos-sdk/MsgWithdrawDelegationReward',
        'value': {
            'delegator_address': delegator_address,
            'validator_address': validator_address,
        },
    }


MSG_WITHDRAW_VALIDATOR_COMMISSION_TYPES: Final = {
    'MsgValue': [{'name': 'validator_address', 'type': 'string'}],
}
"""Types for validator commission withdrawal message."""


class MsgWithdrawValidatorCommissionInterface(TypedDict):
    """Validator commission withdrawal message."""

    type: str  # noqa: A003
    value: _WithValidator


def create_msg_withdraw_validator_commission(
    validator_address: str,
) -> MsgWithdrawValidatorCommissionInterface:
    """Create validator commission withdrawal message."""
    return {
        'type': 'cosmos-sdk/MsgWithdrawValidatorCommission',
        'value': {'validator_address': validator_address},
    }
