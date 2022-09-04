from __future__ import annotations

from typing import Sequence

from evmos.eip712 import (
    MSG_CANCEL_FEE_SPLIT_TYPES,
    MSG_REGISTER_FEE_SPLIT_TYPES,
    MSG_UPDATE_FEE_SPLIT_TYPES,
    create_eip712,
    create_msg_cancel_fee_split,
    create_msg_register_fee_split,
    create_msg_update_fee_split,
    generate_fee,
    generate_message,
    generate_types,
)
from evmos.proto import create_msg_cancel_fee_split as proto_msg_cancel_fee_split
from evmos.proto import create_msg_register_fee_split as proto_msg_register_fee_split
from evmos.proto import create_msg_update_fee_split as proto_msg_update_fee_split
from evmos.proto import create_transaction
from evmos.transactions.common import Chain, Fee, Sender, TxGenerated

# msgCancelFeeSplit.ts


def create_tx_msg_cancel_fee_split(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    contract_address: str,
    deployer_address: str,
) -> TxGenerated:
    """Create transaction with message for fee split cancellation."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_CANCEL_FEE_SPLIT_TYPES)

    msg = create_msg_cancel_fee_split(
        contract_address,
        deployer_address,
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
    msg_cosmos = proto_msg_cancel_fee_split(
        contract_address,
        deployer_address,
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


# msgRegisterFeeSplit.ts


def create_tx_msg_register_fee_split(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> TxGenerated:
    """Create transaction with message for fee split registration."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_REGISTER_FEE_SPLIT_TYPES)

    msg = create_msg_register_fee_split(
        contract_address,
        deployer_address,
        withdrawer_address,
        nonces,
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
    msg_cosmos = proto_msg_register_fee_split(
        contract_address,
        deployer_address,
        withdrawer_address,
        nonces,
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


# msgUpdateFeeSplit.ts


def create_tx_msg_update_fee_split(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> TxGenerated:
    """Create transaction with message for fee split update."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_UPDATE_FEE_SPLIT_TYPES)

    msg = create_msg_update_fee_split(
        contract_address,
        deployer_address,
        withdrawer_address,
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
    msg_cosmos = proto_msg_update_fee_split(
        contract_address,
        deployer_address,
        withdrawer_address,
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
