from __future__ import annotations

from eth_typing import HexStr

from evmos.eip712 import (
    MSG_CONVERT_COIN_TYPES,
    MSG_CONVERT_ERC20_TYPES,
    create_eip712,
    create_msg_convert_coin,
    create_msg_convert_erc20,
    generate_fee,
    generate_message,
    generate_types,
)
from evmos.proto import create_msg_convert_coin as proto_msg_convert_coin
from evmos.proto import create_msg_convert_erc20 as proto_msg_convert_erc20
from evmos.proto import create_transaction
from evmos.transactions.common import Chain, Fee, Sender, TxGenerated

# msgConvertCoin.ts


def create_tx_msg_convert_coin(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    denom: str,
    amount: str,
    receiver_hex_formatted: HexStr,
    sender_evmos_formatted: str,
) -> TxGenerated:
    """Create transaction with message for coin conversion."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_CONVERT_COIN_TYPES)

    msg = create_msg_convert_coin(
        denom,
        amount,
        receiver_hex_formatted,
        sender_evmos_formatted,
    )
    messages = generate_message(
        str(sender.account_number),
        str(sender.sequence),
        chain.cosmos_chain_id,
        memo,
        fee_object,
        msg,
    )
    eip_to_sign = create_eip712(types, chain.chain_id, messages)

    # Cosmos
    msg_cosmos = proto_msg_convert_coin(
        denom,
        amount,
        receiver_hex_formatted,
        sender_evmos_formatted,
    )
    tx = create_transaction(
        msg_cosmos,
        memo,
        fee.amount,
        fee.denom,
        int(fee.gas),
        'ethsecp256',
        sender.pubkey,
        sender.sequence,
        sender.account_number,
        chain.cosmos_chain_id,
    )

    return TxGenerated(
        sign_direct=tx.sign_direct,
        legacy_amino=tx.legacy_amino,
        eip_to_sign=eip_to_sign,
    )


# msgConvertERC20.ts


def create_tx_msg_convert_erc20(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    contract_address: str,
    amount: str,
    receiver_evmos_formatted: str,
    sender_hex_formatted: str,
) -> TxGenerated:
    """Create transaction with message for ERC20 conversion."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_CONVERT_ERC20_TYPES)

    msg = create_msg_convert_erc20(
        contract_address,
        amount,
        receiver_evmos_formatted,
        sender_hex_formatted,
    )
    messages = generate_message(
        str(sender.account_number),
        str(sender.sequence),
        chain.cosmos_chain_id,
        memo,
        fee_object,
        msg,
    )
    eip_to_sign = create_eip712(types, chain.chain_id, messages)

    # Cosmos
    msg_cosmos = proto_msg_convert_erc20(
        contract_address,
        amount,
        receiver_evmos_formatted,
        sender_hex_formatted,
    )
    tx = create_transaction(
        msg_cosmos,
        memo,
        fee.amount,
        fee.denom,
        int(fee.gas),
        'ethsecp256',
        sender.pubkey,
        sender.sequence,
        sender.account_number,
        chain.cosmos_chain_id,
    )

    return TxGenerated(
        sign_direct=tx.sign_direct,
        legacy_amino=tx.legacy_amino,
        eip_to_sign=eip_to_sign,
    )
