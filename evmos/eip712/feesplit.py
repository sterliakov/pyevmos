from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Final

MSG_CANCEL_FEE_SPLIT_TYPES: Final = {
    'MsgValue': [
        {'name': 'contract_address', 'type': 'string'},
        {'name': 'deployer_address', 'type': 'string'},
    ],
}
"""Types for message for fee split cancellation."""


def create_msg_cancel_fee_split(
    contract_address: str,
    deployer_address: str,
) -> dict[str, Any]:
    """Create message for fee split cancellation."""
    return {
        'type': 'evmos/MsgCancelFeeSplit',
        'value': {
            'contract_address': contract_address,
            'deployer_address': deployer_address,
        },
    }


MSG_REGISTER_FEE_SPLIT_TYPES: Final = {
    'MsgValue': [
        {'name': 'contract_address', 'type': 'string'},
        {'name': 'deployer_address', 'type': 'string'},
        {'name': 'withdrawer_address', 'type': 'string'},
        {'name': 'nonces', 'type': 'uint64[]'},
    ],
}
"""Types for message for fee split registration."""


def create_msg_register_fee_split(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> dict[str, Any]:
    """Create message for fee split registration."""
    return {
        'type': 'evmos/MsgRegisterFeeSplit',
        'value': {
            'contract_address': contract_address,
            'deployer_address': deployer_address,
            'withdrawer_address': withdrawer_address,
            'nonces': nonces,
        },
    }


MSG_UPDATE_FEE_SPLIT_TYPES: Final = {
    'MsgValue': [
        {'name': 'contract_address', 'type': 'string'},
        {'name': 'deployer_address', 'type': 'string'},
        {'name': 'withdrawer_address', 'type': 'string'},
    ],
}
"""Types for message for fee split update."""


def create_msg_update_fee_split(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
) -> dict[str, Any]:
    """Create message for fee split update."""
    return {
        'type': 'evmos/MsgUpdateFeeSplit',
        'value': {
            'contract_address': contract_address,
            'deployer_address': deployer_address,
            'withdrawer_address': withdrawer_address,
        },
    }
