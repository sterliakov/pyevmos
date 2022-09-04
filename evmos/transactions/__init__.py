from __future__ import annotations

from betterproto import Message
from eth_typing import HexStr

from evmos.eip712 import (
    IBC_MSG_TRANSFER_TYPES,
    MSG_SEND_TYPES,
    MSG_VOTE_TYPES,
    create_eip712,
    create_ibc_msg_transfer,
    create_msg_send,
    create_msg_vote,
    generate_fee,
    generate_message,
    generate_types,
)
from evmos.proto import MessageGenerated, create_any_message
from evmos.proto import create_ibc_msg_transfer as proto_create_ibc_msg_transfer
from evmos.proto import create_msg_send as proto_msg_send
from evmos.proto import create_msg_vote as proto_create_msg_vote
from evmos.proto import create_transaction, create_tx_raw, create_web3_extension, tx
from evmos.proto.autogen.py.ethermint.types.v1 import ExtensionOptionsWeb3Tx
from evmos.transactions.authz import (
    create_tx_msg_stake_authorization,
    create_tx_msg_stake_revoke_authorization,
)
from evmos.transactions.common import Chain, Fee, Sender, TxGenerated, TxGeneratedBase
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
from evmos.utils.polyfill import removeprefix

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


def create_tx_msg_vote(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    proposal_id: int,
    option: int,
) -> TxGenerated:
    """Create transaction with voting message."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_VOTE_TYPES)

    msg = create_msg_vote(
        proposal_id,
        option,
        sender.account_address,
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
    msg_cosmos = proto_create_msg_vote(
        proposal_id,
        option,
        sender.account_address,
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


# ibcMessageTransfer.ts


def create_tx_ibc_msg_transfer(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
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
) -> TxGenerated:
    """Create transaction with IBC transfer message."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(IBC_MSG_TRANSFER_TYPES)

    msg = create_ibc_msg_transfer(
        receiver,
        sender.account_address,
        source_channel,
        source_port,
        revision_height,
        revision_number,
        timeout_timestamp,
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
    msg_cosmos = proto_create_ibc_msg_transfer(
        source_port,
        source_channel,
        amount,
        denom,
        sender.account_address,
        receiver,
        revision_number,
        revision_height,
        timeout_timestamp,
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


# msgSend.ts


def create_message_send(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    destination_address: str,
    amount: str,
    denom: str,
) -> TxGenerated:
    """Create transaction with message send."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_SEND_TYPES)
    msg = create_msg_send(
        amount,
        denom,
        sender.account_address,
        destination_address,
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
    msg_send = proto_msg_send(
        sender.account_address,
        destination_address,
        amount,
        denom,
    )
    tx = create_transaction(
        msg_send,
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


# txRaw.ts


def create_tx_raw_eip712(
    body: tx.TxBody,
    auth_info: tx.AuthInfo,
    extension: MessageGenerated[Message],
) -> MessageGenerated[tx.TxRaw]:
    """Create a message with raw EIP712 transaction."""
    body.extension_options.append(create_any_message(extension))

    return create_tx_raw(bytes(body), bytes(auth_info), [b''])


# web3Extension.ts


def signature_to_web3_extension(
    chain: Chain,
    sender: Sender,
    hex_formatted_signature: HexStr,
) -> MessageGenerated[ExtensionOptionsWeb3Tx]:
    """Create a message with web3 extension from signature."""
    signature = removeprefix(hex_formatted_signature, '0x')
    return create_web3_extension(
        chain.chain_id,
        sender.account_address,
        bytes.fromhex(signature),
    )
