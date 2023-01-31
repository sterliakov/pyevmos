from __future__ import annotations

from typing import Any, Mapping, Sequence

from evmos.eip712 import (
    MSG_BEGIN_REDELEGATE_TYPES,
    MSG_DELEGATE_TYPES,
    MSG_SET_WITHDRAW_ADDRESS_TYPES,
    MSG_UNDELEGATE_TYPES,
    MSG_WITHDRAW_DELEGATOR_REWARD_TYPES,
    MSG_WITHDRAW_VALIDATOR_COMMISSION_TYPES,
    create_msg_begin_redelegate,
    create_msg_delegate,
    create_msg_set_withdraw_address,
    create_msg_undelegate,
    create_msg_withdraw_delegator_reward,
    create_msg_withdraw_validator_commission,
)
from evmos.proto import (
    MessageGenerated,
    MsgBeginRedelegate,
    MsgDelegate,
    MsgSetWithdrawAddress,
    MsgUndelegate,
    MsgWithdrawDelegatorReward,
    MsgWithdrawValidatorCommission,
)
from evmos.proto import create_msg_begin_redelegate as proto_msg_begin_redelegate
from evmos.proto import create_msg_delegate as proto_msg_delegate
from evmos.proto import (
    create_msg_set_withdraw_address as proto_msg_set_withdraw_address,
)
from evmos.proto import create_msg_undelegate as proto_msg_undelegate
from evmos.proto import (
    create_msg_withdraw_delegator_reward as proto_msg_withdraw_delegator_reward,
)
from evmos.proto import (
    create_msg_withdraw_validator_commission as proto_msg_withdraw_validator_commission,
)
from evmos.transactions.common import to_generated


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
@to_generated(MSG_WITHDRAW_DELEGATOR_REWARD_TYPES, proto=True, many=True)
def create_tx_msg_multiple_withdraw_delegator_reward(
    account_address: str,
    validator_addresses: Sequence[str],
) -> tuple[
    Sequence[Mapping[str, Any]], Sequence[MessageGenerated[MsgWithdrawDelegatorReward]]
]:
    """Create a transaction with message for delegator multiple rewards withdrawal."""
    msgs = [
        create_msg_withdraw_delegator_reward(account_address, validator)
        for validator in validator_addresses
    ]
    proto_msgs = [
        proto_msg_withdraw_delegator_reward(account_address, validator)
        for validator in validator_addresses
    ]

    return msgs, proto_msgs


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


@to_generated(MSG_SET_WITHDRAW_ADDRESS_TYPES)
def create_tx_msg_set_withdraw_address(
    delegator_address: str,
    withdraw_address: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgSetWithdrawAddress]]:
    """Create a transaction with message for withdrawal address setting."""
    # EIP712
    msg = create_msg_set_withdraw_address(delegator_address, withdraw_address)

    # Cosmos
    proto_message = proto_msg_set_withdraw_address(delegator_address, withdraw_address)
    return msg, proto_message
