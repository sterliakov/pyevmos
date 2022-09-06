from __future__ import annotations

from typing import Final

from evmos.eip712.base import (
    Domain,
    EIPToSign,
    MsgInterface,
    create_eip712,
    generate_fee,
    generate_message,
    generate_message_with_multiple_transactions,
    generate_types,
)
from evmos.eip712.erc20 import (
    MSG_CONVERT_COIN_TYPES,
    MSG_CONVERT_ERC20_TYPES,
    create_msg_convert_coin,
    create_msg_convert_erc20,
)
from evmos.eip712.feesplit import (
    MSG_CANCEL_FEE_SPLIT_TYPES,
    MSG_REGISTER_FEE_SPLIT_TYPES,
    MSG_UPDATE_FEE_SPLIT_TYPES,
    create_msg_cancel_fee_split,
    create_msg_register_fee_split,
    create_msg_update_fee_split,
)
from evmos.eip712.staking import (
    MSG_BEGIN_REDELEGATE_TYPES,
    MSG_DELEGATE_TYPES,
    MSG_UNDELEGATE_TYPES,
    MSG_WITHDRAW_DELEGATOR_REWARD_TYPES,
    MSG_WITHDRAW_VALIDATOR_COMMISSION_TYPES,
    create_msg_begin_redelegate,
    create_msg_delegate,
    create_msg_undelegate,
    create_msg_withdraw_delegator_reward,
    create_msg_withdraw_validator_commission,
)
from evmos.eip712.validator import MSG_EDIT_VALIDATOR_TYPES, create_msg_edit_validator

__all__ = [
    'create_eip712',
    'create_ibc_msg_transfer',
    'create_msg_begin_redelegate',
    'create_msg_cancel_fee_split',
    'create_msg_convert_coin',
    'create_msg_convert_erc20',
    'MSG_CANCEL_FEE_SPLIT_TYPES',
    'create_msg_delegate',
    'create_msg_edit_validator',
    'MSG_VOTE_TYPES',
    'create_msg_register_fee_split',
    'create_msg_send',
    'create_msg_undelegate',
    'create_msg_update_fee_split',
    'MSG_DELEGATE_TYPES',
    'create_msg_vote',
    'create_msg_withdraw_delegator_reward',
    'create_msg_withdraw_validator_commission',
    'generate_fee',
    'MSG_CONVERT_COIN_TYPES',
    'generate_message',
    'generate_message_with_multiple_transactions',
    'generate_types',
    'IBC_MSG_TRANSFER_TYPES',
    'MSG_BEGIN_REDELEGATE_TYPES',
    'MSG_CONVERT_ERC20_TYPES',
    'MSG_REGISTER_FEE_SPLIT_TYPES',
    'MSG_SEND_TYPES',
    'MSG_UNDELEGATE_TYPES',
    'MSG_UPDATE_FEE_SPLIT_TYPES',
    'MSG_WITHDRAW_DELEGATOR_REWARD_TYPES',
    'MSG_WITHDRAW_VALIDATOR_COMMISSION_TYPES',
    'MSG_EDIT_VALIDATOR_TYPES',
    'EIPToSign',
    'Domain',
]


# gov.ts
MSG_VOTE_TYPES: Final = {
    'MsgValue': [
        {'name': 'proposalId', 'type': 'uint64'},
        {'name': 'voter', 'type': 'string'},
        {'name': 'option', 'type': 'int32'},
    ],
}
"""Types for voting message."""


def create_msg_vote(proposal_id: int, option: int, sender: str) -> MsgInterface:
    """Create voting (governmental) message."""
    return {
        'type': 'cosmos-sdk/MsgVote',
        'value': {
            'proposalId': proposal_id,
            'voter': sender,
            'option': option,
        },
    }


# ibcMsgTransfer.ts
IBC_MSG_TRANSFER_TYPES: Final = {
    'MsgValue': [
        {'name': 'sourcePort', 'type': 'string'},
        {'name': 'sourceChannel', 'type': 'string'},
        {'name': 'token', 'type': 'TypeToken'},
        {'name': 'sender', 'type': 'string'},
        {'name': 'receiver', 'type': 'string'},
        {'name': 'timeoutHeight', 'type': 'TypeTimeoutHeight'},
        {'name': 'timeoutTimestamp', 'type': 'uint64'},
    ],
    'TypeToken': [
        {'name': 'denom', 'type': 'string'},
        {'name': 'amount', 'type': 'string'},
    ],
    'TypeTimeoutHeight': [
        {'name': 'revisionNumber', 'type': 'uint64'},
        {'name': 'revisionHeight', 'type': 'uint64'},
    ],
}
"""Types for IBC message."""


def create_ibc_msg_transfer(
    receiver: str,
    sender: str,
    source_channel: str,
    source_port: str,
    revision_height: int,
    revision_number: int,
    timeout_timestamp: str,
    amount: str,
    denom: str,
) -> MsgInterface:
    """Create IBC (inter-blockchain) message transfer.

    See Also:
        https://tutorials.cosmos.network/academy/4-ibc/what-is-ibc.html
    """
    return {
        'type': 'cosmos-sdk/MsgTransfer',
        'value': {
            'receiver': receiver,
            'sender': sender,
            'sourceChannel': source_channel,
            'sourcePort': source_port,
            'timeoutHeight': {
                'revisionHeight': str(revision_height),
                'revisionNumber': str(revision_number),
            },
            'timeoutTimestamp': timeout_timestamp,
            'token': {'amount': amount, 'denom': denom},
        },
    }


# msgSend.ts
MSG_SEND_TYPES: Final = {
    'MsgValue': [
        {'name': 'from_address', 'type': 'string'},
        {'name': 'to_address', 'type': 'string'},
        {'name': 'amount', 'type': 'TypeAmount[]'},
    ],
    'TypeAmount': [
        {'name': 'denom', 'type': 'string'},
        {'name': 'amount', 'type': 'string'},
    ],
}
"""Types for message sending."""


def create_msg_send(
    amount: str,
    denom: str,
    from_address: str,
    to_address: str,
) -> MsgInterface:
    """Create message for sending."""
    return {
        'type': 'cosmos-sdk/MsgSend',
        'value': {
            'amount': [
                {'amount': amount, 'denom': denom},
            ],
            'from_address': from_address,
            'to_address': to_address,
        },
    }
