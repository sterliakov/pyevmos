from __future__ import annotations

from typing import Sequence

# from evmos.eip712 import MsgWithdrawDelegatorRewardInterface
from evmos.eip712 import (
    MSG_BEGIN_REDELEGATE_TYPES,
    MSG_DELEGATE_TYPES,
    MSG_UNDELEGATE_TYPES,
    MSG_WITHDRAW_DELEGATOR_REWARD_TYPES,
    MSG_WITHDRAW_VALIDATOR_COMMISSION_TYPES,
    create_eip712,
    create_msg_begin_redelegate,
    create_msg_delegate,
    create_msg_undelegate,
    create_msg_withdraw_delegator_reward,
    create_msg_withdraw_validator_commission,
    generate_fee,
    generate_message,
    generate_message_with_multiple_transactions,
    generate_types,
)

# from evmos.proto import MsgWithdrawDelegatorRewardProtoInterface
from evmos.proto import create_msg_begin_redelegate as proto_msg_begin_redelegate
from evmos.proto import create_msg_delegate as proto_msg_delegate
from evmos.proto import create_msg_undelegate as proto_msg_undelegate
from evmos.proto import (
    create_msg_withdraw_delegator_reward as proto_msg_withdraw_delegator_reward,
)
from evmos.proto import (
    create_msg_withdraw_validator_commission as proto_msg_withdraw_validator_commission,
)
from evmos.proto import create_transaction, create_transaction_with_multiple_messages
from evmos.transactions.common import Chain, Fee, Sender, TxGenerated


def create_tx_msg_delegate(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> TxGenerated:
    """Create a transaction with delegation message."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_DELEGATE_TYPES)
    msg = create_msg_delegate(
        sender.account_address,
        validator_address,
        amount,
        denom,
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
    proto_message = proto_msg_delegate(
        sender.account_address,
        validator_address,
        amount,
        denom,
    )
    tx = create_transaction(
        proto_message,
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


def create_tx_msg_begin_redelegate(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    validator_src_address: str,
    validator_dst_address: str,
    amount: str,
    denom: str,
) -> TxGenerated:
    """Create a transaction with redelegation beginning message."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_BEGIN_REDELEGATE_TYPES)
    msg = create_msg_begin_redelegate(
        sender.account_address,
        validator_src_address,
        validator_dst_address,
        amount,
        denom,
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
    proto_message = proto_msg_begin_redelegate(
        sender.account_address,
        validator_src_address,
        validator_dst_address,
        amount,
        denom,
    )
    tx = create_transaction(
        proto_message,
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


def create_tx_msg_undelegate(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> TxGenerated:
    """Create a transaction with undelegation message."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_UNDELEGATE_TYPES)
    msg = create_msg_undelegate(
        sender.account_address,
        validator_address,
        amount,
        denom,
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
    proto_message = proto_msg_undelegate(
        sender.account_address,
        validator_address,
        amount,
        denom,
    )
    tx = create_transaction(
        proto_message,
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


def create_tx_msg_withdraw_delegator_reward(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    validator_address: str,
) -> TxGenerated:
    """Create a transaction with message for delegator reward withdrawal."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_WITHDRAW_DELEGATOR_REWARD_TYPES)
    msg = create_msg_withdraw_delegator_reward(
        sender.account_address,
        validator_address,
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
    proto_message = proto_msg_withdraw_delegator_reward(
        sender.account_address,
        validator_address,
    )
    tx = create_transaction(
        proto_message,
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


# Multiple WithdrawRewards
def create_tx_msg_multiple_withdraw_delegator_reward(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    validator_addresses: Sequence[str],
) -> TxGenerated:
    """Create a transaction with message for delegator multiple rewards withdrawal."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_WITHDRAW_DELEGATOR_REWARD_TYPES)
    # EIP712
    # msgs: MsgWithdrawDelegatorRewardInterface[] = []
    msgs = []
    # Cosmos
    # proto_msgs: MsgWithdrawDelegatorRewardProtoInterface[] = []
    msgs = [
        create_msg_withdraw_delegator_reward(sender.account_address, validator)
        for validator in validator_addresses
    ]
    proto_msgs = [
        proto_msg_withdraw_delegator_reward(sender.account_address, validator)
        for validator in validator_addresses
    ]

    messages = generate_message_with_multiple_transactions(
        str(sender.account_number),
        str(sender.sequence),
        chain.cosmos_chain_id,
        memo,
        fee_object,
        msgs,
    )
    eip_to_sign = create_eip712(types, chain.chain_id, messages)

    # Cosmos
    tx = create_transaction_with_multiple_messages(
        proto_msgs,
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


def create_tx_msg_withdraw_validator_commission(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    validator_address: str,
) -> TxGenerated:
    """Create a transaction with message for validator commission withdrawal."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_WITHDRAW_VALIDATOR_COMMISSION_TYPES)
    msg = create_msg_withdraw_validator_commission(validator_address)
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
    proto_message = proto_msg_withdraw_validator_commission(
        validator_address,
    )
    tx = create_transaction(
        proto_message,
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
