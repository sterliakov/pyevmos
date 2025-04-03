from __future__ import annotations

from typing import Final

from evmos.eip712.base import MsgInterface

MSG_CONVERT_COIN_TYPES: Final = {
    "MsgValue": [
        {"name": "coin", "type": "TypeCoin"},
        {"name": "receiver", "type": "string"},
        {"name": "sender", "type": "string"},
    ],
    "TypeCoin": [
        {"name": "denom", "type": "string"},
        {"name": "amount", "type": "string"},
    ],
}
"""Types for message for coin types conversion."""


def create_msg_convert_coin(
    denom: str | int,
    amount: str | int,
    receiver: str,
    sender: str,
) -> MsgInterface:
    """Create message for coin types conversion."""
    return {
        "type": "evmos/MsgConvertCoin",
        "value": {
            "coin": {
                "denom": str(denom),
                "amount": str(amount),
            },
            "receiver": receiver,
            "sender": sender,
        },
    }


MSG_CONVERT_ERC20_TYPES: Final = {
    "MsgValue": [
        {"name": "contract_address", "type": "string"},
        {"name": "amount", "type": "string"},
        {"name": "receiver", "type": "string"},
        {"name": "sender", "type": "string"},
    ],
}
"""Types for message for ERC20 types conversion."""


def create_msg_convert_erc20(
    contract_address: str,
    amount: str,
    receiver: str,
    sender: str,
) -> MsgInterface:
    """Create message for ERC20 types conversion."""
    return {
        "type": "evmos/MsgConvertERC20",
        "value": {
            "contract_address": contract_address,
            "amount": amount,
            "receiver": receiver,
            "sender": sender,
        },
    }
