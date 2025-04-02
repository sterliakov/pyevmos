from __future__ import annotations

from typing import Final

from evmos.eip712.base import MsgInterface, MsgWithValidatorInterface

MSG_DELEGATE_TYPES: Final = {
    "MsgValue": [
        {"name": "delegator_address", "type": "string"},
        {"name": "validator_address", "type": "string"},
        {"name": "amount", "type": "TypeAmount"},
    ],
    "TypeAmount": [
        {"name": "denom", "type": "string"},
        {"name": "amount", "type": "string"},
    ],
}
"""Types for delegation message."""


def create_msg_delegate(
    delegator_address: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> MsgInterface:
    """Create delegation message."""
    return {
        "type": "cosmos-sdk/MsgDelegate",
        "value": {
            "amount": {"amount": amount, "denom": denom},
            "delegator_address": delegator_address,
            "validator_address": validator_address,
        },
    }


MSG_BEGIN_REDELEGATE_TYPES: Final = {
    "MsgValue": [
        {"name": "delegator_address", "type": "string"},
        {"name": "validator_src_address", "type": "string"},
        {"name": "validator_dst_address", "type": "string"},
        {"name": "amount", "type": "TypeAmount"},
    ],
    "TypeAmount": [
        {"name": "denom", "type": "string"},
        {"name": "amount", "type": "string"},
    ],
}
"""Types for redelegation beginning message."""


def create_msg_begin_redelegate(
    delegator_address: str,
    validator_src_address: str,
    validator_dst_address: str,
    amount: str,
    denom: str,
) -> MsgInterface:
    """Create redelegation beginning message."""
    return {
        "type": "cosmos-sdk/MsgBeginRedelegate",
        "value": {
            "amount": {"amount": amount, "denom": denom},
            "delegator_address": delegator_address,
            "validator_src_address": validator_src_address,
            "validator_dst_address": validator_dst_address,
        },
    }


MSG_UNDELEGATE_TYPES: Final = {
    "MsgValue": [
        {"name": "delegator_address", "type": "string"},
        {"name": "validator_address", "type": "string"},
        {"name": "amount", "type": "TypeAmount"},
    ],
    "TypeAmount": [
        {"name": "denom", "type": "string"},
        {"name": "amount", "type": "string"},
    ],
}
"""Types for delegation cancellation message."""


def create_msg_undelegate(
    delegator_address: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> MsgInterface:
    """Create delegation cancellation message."""
    return {
        "type": "cosmos-sdk/MsgUndelegate",
        "value": {
            "amount": {"amount": amount, "denom": denom},
            "delegator_address": delegator_address,
            "validator_address": validator_address,
        },
    }


MSG_WITHDRAW_DELEGATOR_REWARD_TYPES: Final = {
    "MsgValue": [
        {"name": "delegator_address", "type": "string"},
        {"name": "validator_address", "type": "string"},
    ],
}
"""Types for delegation reward withdrawal message."""


def create_msg_withdraw_delegator_reward(
    delegator_address: str,
    validator_address: str,
) -> MsgInterface:
    """Create delegation reward withdrawal message."""
    return {
        "type": "cosmos-sdk/MsgWithdrawDelegationReward",
        "value": {
            "delegator_address": delegator_address,
            "validator_address": validator_address,
        },
    }


MSG_WITHDRAW_VALIDATOR_COMMISSION_TYPES: Final = {
    "MsgValue": [{"name": "validator_address", "type": "string"}],
}
"""Types for validator commission withdrawal message."""


def create_msg_withdraw_validator_commission(
    validator_address: str,
) -> MsgWithValidatorInterface:
    """Create validator commission withdrawal message."""
    return {
        "type": "cosmos-sdk/MsgWithdrawValidatorCommission",
        "value": {"validator_address": validator_address},
    }


MSG_SET_WITHDRAW_ADDRESS_TYPES: Final = {
    "MsgValue": [
        {"name": "delegator_address", "type": "string"},
        {"name": "withdraw_address", "type": "string"},
    ],
}
"""Types for validator withdrawal address setting message."""


def create_msg_set_withdraw_address(
    delegator_address: str,
    withdraw_address: str,
) -> MsgInterface:
    """Create validator withdrawal address setting message."""
    return {
        "type": "cosmos-sdk/MsgModifyWithdrawAddress",
        "value": {
            "delegator_address": delegator_address,
            "withdraw_address": withdraw_address,
        },
    }
