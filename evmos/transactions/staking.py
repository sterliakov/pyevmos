from __future__ import annotations

from typing import Any, Mapping, Sequence

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
    generate_message_with_multiple_transactions,
    generate_types,
)

# from evmos.proto import MsgWithdrawDelegatorRewardProtoInterface
from evmos.proto import (
    MessageGenerated,
    MsgBeginRedelegate,
    MsgDelegate,
    MsgUndelegate,
    MsgWithdrawDelegatorReward,
    MsgWithdrawValidatorCommission,
)
from evmos.proto import create_msg_begin_redelegate as proto_msg_begin_redelegate
from evmos.proto import create_msg_delegate as proto_msg_delegate
from evmos.proto import create_msg_undelegate as proto_msg_undelegate
from evmos.proto import (
    create_msg_withdraw_delegator_reward as proto_msg_withdraw_delegator_reward,
)
from evmos.proto import (
    create_msg_withdraw_validator_commission as proto_msg_withdraw_validator_commission,
)
from evmos.proto import create_transaction_with_multiple_messages
from evmos.transactions.common import Chain, Fee, Sender, TxGenerated, to_generated


@to_generated(MSG_DELEGATE_TYPES, proto=True)
def create_tx_msg_delegate(
    account_address: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgDelegate]]:
    """Create a transaction with delegation message."""
    # EIP712
    msg = create_msg_delegate(
        account_address,
        validator_address,
        amount,
        denom,
    )

    # Cosmos
    proto_message = proto_msg_delegate(
        account_address,
        validator_address,
        amount,
        denom,
    )
    return msg, proto_message


@to_generated(MSG_BEGIN_REDELEGATE_TYPES, proto=True)
def create_tx_msg_begin_redelegate(
    account_address: str,
    validator_src_address: str,
    validator_dst_address: str,
    amount: str,
    denom: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgBeginRedelegate]]:
    """Create a transaction with redelegation beginning message."""
    # EIP712
    msg = create_msg_begin_redelegate(
        account_address,
        validator_src_address,
        validator_dst_address,
        amount,
        denom,
    )

    # Cosmos
    proto_message = proto_msg_begin_redelegate(
        account_address,
        validator_src_address,
        validator_dst_address,
        amount,
        denom,
    )
    return msg, proto_message


@to_generated(MSG_UNDELEGATE_TYPES, proto=True)
def create_tx_msg_undelegate(
    account_address: str,
    validator_address: str,
    amount: str,
    denom: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgUndelegate]]:
    """Create a transaction with undelegation message."""
    # EIP712
    msg = create_msg_undelegate(
        account_address,
        validator_address,
        amount,
        denom,
    )

    # Cosmos
    proto_message = proto_msg_undelegate(
        account_address,
        validator_address,
        amount,
        denom,
    )
    return msg, proto_message


@to_generated(MSG_WITHDRAW_DELEGATOR_REWARD_TYPES, proto=True)
def create_tx_msg_withdraw_delegator_reward(
    account_address: str,
    validator_address: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgWithdrawDelegatorReward]]:
    """Create a transaction with message for delegator reward withdrawal."""
    # EIP712
    msg = create_msg_withdraw_delegator_reward(
        account_address,
        validator_address,
    )

    # Cosmos
    proto_message = proto_msg_withdraw_delegator_reward(
        account_address,
        validator_address,
    )
    return msg, proto_message


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


@to_generated(MSG_WITHDRAW_VALIDATOR_COMMISSION_TYPES)
def create_tx_msg_withdraw_validator_commission(
    validator_address: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgWithdrawValidatorCommission]]:
    """Create a transaction with message for validator commission withdrawal."""
    # EIP712
    msg = create_msg_withdraw_validator_commission(validator_address)

    # Cosmos
    proto_message = proto_msg_withdraw_validator_commission(validator_address)
    return msg, proto_message
