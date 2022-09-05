from __future__ import annotations

from typing import Any, Mapping

from betterproto import Message

from evmos.eip712 import (
    IBC_MSG_TRANSFER_TYPES,
    MSG_SEND_TYPES,
    MSG_VOTE_TYPES,
    create_ibc_msg_transfer,
    create_msg_send,
    create_msg_vote,
)
from evmos.proto import (
    AuthInfo,
    MessageGenerated,
    MsgSend,
    MsgTransfer,
    MsgVote,
    TxBody,
    TxRaw,
    create_any_message,
)
from evmos.proto import create_ibc_msg_transfer as proto_create_ibc_msg_transfer
from evmos.proto import create_msg_send as proto_msg_send
from evmos.proto import create_msg_vote as proto_create_msg_vote
from evmos.proto import create_tx_raw, create_web3_extension
from evmos.proto.autogen.py.ethermint.types.v1 import ExtensionOptionsWeb3Tx
from evmos.transactions.authz import (
    create_tx_msg_stake_authorization,
    create_tx_msg_stake_revoke_authorization,
)
from evmos.transactions.common import (
    Chain,
    Fee,
    Sender,
    TxGenerated,
    TxGeneratedBase,
    to_generated,
)
from evmos.transactions.erc20 import (
    create_tx_msg_convert_coin,
    create_tx_msg_convert_erc20,
)
from evmos.transactions.feesplit import (
    create_tx_msg_cancel_fee_split,
    create_tx_msg_register_fee_split,
    create_tx_msg_update_fee_split,
)
from evmos.transactions.staking import (
    create_tx_msg_begin_redelegate,
    create_tx_msg_delegate,
    create_tx_msg_multiple_withdraw_delegator_reward,
    create_tx_msg_undelegate,
    create_tx_msg_withdraw_delegator_reward,
    create_tx_msg_withdraw_validator_commission,
)
from evmos.transactions.validator import create_tx_msg_edit_validator

__all__ = [
    'create_tx_msg_vote',
    'create_tx_ibc_msg_transfer',
    'create_message_send',
    'create_tx_raw_eip712',
    'signature_to_web3_extension',
    'Chain',
    'Fee',
    'Sender',
    'TxGeneratedBase',
    'TxGenerated',
    'create_tx_msg_stake_authorization',
    'create_tx_msg_stake_revoke_authorization',
    'create_tx_msg_convert_coin',
    'create_tx_msg_convert_erc20',
    'create_tx_msg_cancel_fee_split',
    'create_tx_msg_register_fee_split',
    'create_tx_msg_update_fee_split',
    'create_tx_msg_delegate',
    'create_tx_msg_begin_redelegate',
    'create_tx_msg_undelegate',
    'create_tx_msg_withdraw_delegator_reward',
    'create_tx_msg_multiple_withdraw_delegator_reward',
    'create_tx_msg_withdraw_validator_commission',
    'create_tx_msg_edit_validator',
]


# gov.ts


@to_generated(MSG_VOTE_TYPES, proto=True)
def create_tx_msg_vote(
    account_address: str,
    proposal_id: int,
    option: int,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgVote]]:
    """Create transaction with voting message."""
    # EIP712
    msg = create_msg_vote(
        proposal_id,
        option,
        account_address,
    )

    # Cosmos
    msg_cosmos = proto_create_msg_vote(
        proposal_id,
        option,
        account_address,
    )
    return msg, msg_cosmos


# ibcMessageTransfer.ts


@to_generated(IBC_MSG_TRANSFER_TYPES, proto=True)
def create_tx_ibc_msg_transfer(
    account_address: str,
    # Channel
    source_port: str,
    source_channel: str,
    # Token
    amount: str,
    denom: str,
    # Addresses
    receiver: str,
    # Timeout
    revision_number: int,
    revision_height: int,
    timeout_timestamp: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgTransfer]]:
    """Create transaction with IBC transfer message."""
    # EIP712

    msg = create_ibc_msg_transfer(
        receiver,
        account_address,
        source_channel,
        source_port,
        revision_height,
        revision_number,
        timeout_timestamp,
        amount,
        denom,
    )

    # Cosmos
    msg_cosmos = proto_create_ibc_msg_transfer(
        source_port,
        source_channel,
        amount,
        denom,
        account_address,
        receiver,
        revision_number,
        revision_height,
        timeout_timestamp,
    )
    return msg, msg_cosmos


# msgSend.ts


@to_generated(MSG_SEND_TYPES, proto=True)
def create_message_send(
    account_address: str,
    destination_address: str,
    amount: str,
    denom: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgSend]]:
    """Create transaction with message send."""
    # EIP712
    msg = create_msg_send(
        amount,
        denom,
        account_address,
        destination_address,
    )

    # Cosmos
    msg_send = proto_msg_send(
        account_address,
        destination_address,
        amount,
        denom,
    )
    return msg, msg_send


# txRaw.ts


def create_tx_raw_eip712(
    body: TxBody,
    auth_info: AuthInfo,
    extension: MessageGenerated[Message],
) -> MessageGenerated[TxRaw]:
    """Create a message with raw EIP712 transaction."""
    body.extension_options.append(create_any_message(extension))

    return create_tx_raw(bytes(body), bytes(auth_info), [b''])


# web3Extension.ts


def signature_to_web3_extension(
    chain: Chain,
    sender: Sender,
    signature: bytes,
) -> MessageGenerated[ExtensionOptionsWeb3Tx]:
    """Create a message with web3 extension from signature."""
    return create_web3_extension(
        chain.chain_id,
        sender.account_address,
        signature,
    )
