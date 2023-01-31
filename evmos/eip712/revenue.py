from __future__ import annotations

from typing import Final, Sequence

from evmos.eip712.base import MsgInterface

MSG_CANCEL_REVENUE_TYPES: Final = {
    'MsgValue': [
        {'name': 'contract_address', 'type': 'string'},
        {'name': 'deployer_address', 'type': 'string'},
    ],
}
"""Types for message for revenue cancellation."""


def create_msg_cancel_revenue(
    contract_address: str,
    deployer_address: str,
) -> MsgInterface:
    """Create message for revenue cancellation."""
    return {
        'type': 'evmos/MsgCancelRevenue',
        'value': {
            'contract_address': contract_address,
            'deployer_address': deployer_address,
        },
    }


MSG_REGISTER_REVENUE_TYPES: Final = {
    'MsgValue': [
        {'name': 'contract_address', 'type': 'string'},
        {'name': 'deployer_address', 'type': 'string'},
        {'name': 'withdrawer_address', 'type': 'string'},
        {'name': 'nonces', 'type': 'uint64[]'},
    ],
}
"""Types for message for revenue registration."""


def create_msg_register_revenue(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> MsgInterface:
    """Create message for revenue registration."""
    return {
        'type': 'evmos/MsgRegisterRevenue',
        'value': {
            'contract_address': contract_address,
            'deployer_address': deployer_address,
            'withdrawer_address': withdrawer_address,
            'nonces': nonces,
        },
    }


MSG_UPDATE_REVENUE_TYPES: Final = {
    'MsgValue': [
        {'name': 'contract_address', 'type': 'string'},
        {'name': 'deployer_address', 'type': 'string'},
        {'name': 'withdrawer_address', 'type': 'string'},
    ],
}
"""Types for message for revenue update."""


def create_msg_update_revenue(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
) -> MsgInterface:
    """Create message for revenue update."""
    return {
        'type': 'evmos/MsgUpdateRevenue',
        'value': {
            'contract_address': contract_address,
            'deployer_address': deployer_address,
            'withdrawer_address': withdrawer_address,
        },
    }
