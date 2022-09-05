from __future__ import annotations

from typing import Any, Mapping

from eth_typing import HexStr

from evmos.eip712 import (
    MSG_CONVERT_COIN_TYPES,
    MSG_CONVERT_ERC20_TYPES,
    create_msg_convert_coin,
    create_msg_convert_erc20,
)
from evmos.proto import MessageGenerated, MsgConvertCoin, MsgConvertErc20
from evmos.proto import create_msg_convert_coin as proto_msg_convert_coin
from evmos.proto import create_msg_convert_erc20 as proto_msg_convert_erc20
from evmos.transactions.common import to_generated

# msgConvertCoin.ts


@to_generated(MSG_CONVERT_COIN_TYPES)
def create_tx_msg_convert_coin(
    denom: str,
    amount: str,
    receiver_hex_formatted: HexStr,
    sender_evmos_formatted: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgConvertCoin]]:
    """Create transaction with message for coin conversion."""
    # EIP712
    msg = create_msg_convert_coin(
        denom,
        amount,
        receiver_hex_formatted,
        sender_evmos_formatted,
    )

    # Cosmos
    msg_cosmos = proto_msg_convert_coin(
        denom,
        amount,
        receiver_hex_formatted,
        sender_evmos_formatted,
    )

    return msg, msg_cosmos


# msgConvertERC20.ts


@to_generated(MSG_CONVERT_ERC20_TYPES)
def create_tx_msg_convert_erc20(
    contract_address: str,
    amount: str,
    receiver_evmos_formatted: str,
    sender_hex_formatted: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgConvertErc20]]:
    """Create transaction with message for ERC20 conversion."""
    # EIP712
    msg = create_msg_convert_erc20(
        contract_address,
        amount,
        receiver_evmos_formatted,
        sender_hex_formatted,
    )

    # Cosmos
    msg_cosmos = proto_msg_convert_erc20(
        contract_address,
        amount,
        receiver_evmos_formatted,
        sender_hex_formatted,
    )

    return msg, msg_cosmos
