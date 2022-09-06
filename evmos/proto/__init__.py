from __future__ import annotations

from typing import Sequence

from evmos.proto.authz import (
    MsgGrant,
    MsgRevoke,
    RevokeMessages,
    StakeAuthTypes,
    create_msg_grant,
    create_msg_revoke,
    create_stake_authorization,
)
from evmos.proto.autogen.py.cosmos.bank.v1beta1 import MsgSend
from evmos.proto.autogen.py.cosmos.base.v1beta1 import Coin
from evmos.proto.autogen.py.cosmos.gov.v1beta1 import MsgVote, VoteOption
from evmos.proto.autogen.py.cosmos.tx.v1beta1 import AuthInfo, TxBody, TxRaw
from evmos.proto.autogen.py.ethermint.evm import v1 as ethermint
from evmos.proto.autogen.py.ethermint.types.v1 import ExtensionOptionsWeb3Tx
from evmos.proto.autogen.py.ibc.applications.transfer.v1 import MsgTransfer
from evmos.proto.autogen.py.ibc.core.client.v1 import Height
from evmos.proto.erc20 import (
    MsgConvertCoin,
    MsgConvertErc20,
    create_msg_convert_coin,
    create_msg_convert_erc20,
)
from evmos.proto.feesplit import (
    MsgCancelFeeSplit,
    MsgRegisterFeeSplit,
    MsgUpdateFeeSplit,
    create_msg_cancel_fee_split,
    create_msg_register_fee_split,
    create_msg_update_fee_split,
)
from evmos.proto.staking import (
    MsgBeginRedelegate,
    MsgDelegate,
    MsgUndelegate,
    MsgWithdrawDelegatorReward,
    MsgWithdrawValidatorCommission,
    create_msg_begin_redelegate,
    create_msg_delegate,
    create_msg_undelegate,
    create_msg_withdraw_delegator_reward,
    create_msg_withdraw_validator_commission,
)
from evmos.proto.transactions import (
    create_auth_info,
    create_body,
    create_body_with_multiple_messages,
    create_fee,
    create_sig_doc,
    create_signer_info,
    create_transaction,
    create_transaction_with_multiple_messages,
)
from evmos.proto.utils import MessageGenerated, create_any_message
from evmos.proto.validator import MsgEditValidator, create_msg_edit_validator

__all__ = [
    'create_msg_grant',
    'create_msg_revoke',
    'create_stake_authorization',
    'StakeAuthTypes',
    'RevokeMessages',
    'MsgConvertCoin',
    'MsgConvertErc20',
    'MsgGrant',
    'MsgRevoke',
    'MsgCancelFeeSplit',
    'MsgUpdateFeeSplit',
    'MsgRegisterFeeSplit',
    'MsgWithdrawDelegatorReward',
    'MsgWithdrawValidatorCommission',
    'MsgDelegate',
    'MsgBeginRedelegate',
    'MsgUndelegate',
    'MsgEditValidator',
    'TxRaw',
    'AuthInfo',
    'TxBody',
    'create_msg_convert_coin',
    'create_msg_convert_erc20',
    'create_msg_cancel_fee_split',
    'create_msg_register_fee_split',
    'create_msg_update_fee_split',
    'create_msg_delegate',
    'create_msg_begin_redelegate',
    'create_msg_undelegate',
    'create_msg_withdraw_delegator_reward',
    'create_msg_withdraw_validator_commission',
    'create_body_with_multiple_messages',
    'create_body',
    'create_fee',
    'create_signer_info',
    'create_auth_info',
    'create_sig_doc',
    'create_transaction_with_multiple_messages',
    'create_transaction',
    'MessageGenerated',
    'create_any_message',
    'create_msg_edit_validator',
    'create_msg_send',
    'create_ibc_msg_transfer',
    'bytes_to_msg_ethereum_tx',
    'bytes_to_legacy_tx',
    'bytes_to_access_list_tx',
    'bytes_to_dynamic_fee_tx',
    'bytes_to_tx_raw',
    'bytes_to_tx_body',
    'bytes_to_auth_info',
    'create_tx_raw',
    'create_msg_vote',
    'create_web3_extension',
]


# msgSend.ts


def create_msg_send(
    from_address: str,
    to_address: str,
    amount: str,
    denom: str,
) -> MessageGenerated[MsgSend]:
    """Create :class:`~evmos.proto.utils.MessageGenerated` for given args."""
    value = Coin(denom=denom, amount=amount)

    message = MsgSend(
        from_address=from_address,
        to_address=to_address,
        amount=[value],
    )
    return MessageGenerated(
        message=message,
        path='cosmos.bank.v1beta1.MsgSend',
    )


# ibcMsgTransfer.ts


def create_ibc_msg_transfer(
    # Channel
    source_port: str,
    source_channel: str,
    # Token
    amount: str,
    denom: str,
    # Addresses
    sender: str,
    receiver: str,
    # Timeout
    revision_number: int,
    revision_height: int,
    timeout_timestamp: str,
) -> MessageGenerated[MsgTransfer]:
    """Create message for IBC transfer."""
    token = Coin(denom=denom, amount=amount)

    timeout_height = Height(
        revision_number=revision_number,
        revision_height=revision_height,
    )

    ibc_message = MsgTransfer(
        source_port=source_port,
        source_channel=source_channel,
        token=token,
        sender=sender,
        receiver=receiver,
        timeout_height=timeout_height,
        timeout_timestamp=int(timeout_timestamp),
    )

    return MessageGenerated(
        message=ibc_message,
        path='ibc.applications.transfer.v1.MsgTransfer',
    )


# msgEthereumTx


def bytes_to_msg_ethereum_tx(binary_data: bytes) -> ethermint.MsgEthereumTx:
    """Deserialize :class:`evmos.proto.autogen.py.ethermint.evm.v1.MsgEthereumTx`."""
    return ethermint.MsgEthereumTx().parse(binary_data)


def bytes_to_legacy_tx(binary_data: bytes) -> ethermint.LegacyTx:
    """Deserialize :class:`evmos.proto.autogen.py.ethermint.evm.v1.LegacyTx`."""
    return ethermint.LegacyTx().parse(binary_data)


def bytes_to_access_list_tx(binary_data: bytes) -> ethermint.AccessListTx:
    """Deserialize :class:`evmos.proto.autogen.py.ethermint.evm.v1.AccessListTx`."""
    return ethermint.AccessListTx().parse(binary_data)


def bytes_to_dynamic_fee_tx(binary_data: bytes) -> ethermint.DynamicFeeTx:
    """Deserialize :class:`evmos.proto.autogen.py.ethermint.evm.v1.DynamicFeeTx`."""
    return ethermint.DynamicFeeTx().parse(binary_data)


# txRaw.ts


def bytes_to_tx_raw(binary_data: bytes) -> TxRaw:
    """Deserialize :class:`evmos.proto.autogen.py.cosmos.tx.v1beta1.TxRaw`."""
    return TxRaw().parse(binary_data)


def bytes_to_tx_body(binary_data: bytes) -> TxBody:
    """Deserialize :class:`evmos.proto.autogen.py.cosmos.tx.v1beta1.TxBody`."""
    return TxBody().parse(binary_data)


def bytes_to_auth_info(binary_data: bytes) -> AuthInfo:
    """Deserialize :class:`evmos.proto.autogen.py.cosmos.tx.v1beta1.AuthInfo`."""
    return AuthInfo().parse(binary_data)


def create_tx_raw(
    body_bytes: bytes,
    auth_info_bytes: bytes,
    signatures: Sequence[bytes],
) -> MessageGenerated[TxRaw]:
    """Create message with raw transaction."""
    message = TxRaw(
        body_bytes=body_bytes,
        auth_info_bytes=auth_info_bytes,
        signatures=list(signatures),
    )
    return MessageGenerated(
        message=message,
        path='cosmos.tx.v1beta1.TxRaw',
    )


# vote.ts


def create_msg_vote(
    proposal_id: int,
    option: int | VoteOption,
    sender: str,
) -> MessageGenerated[MsgVote]:
    """Create voting message."""
    vote_message = MsgVote(
        proposal_id=proposal_id,
        voter=sender,
        option=option,  # type: ignore[arg-type]
    )

    return MessageGenerated(
        message=vote_message,
        path='cosmos.gov.v1beta1.MsgVote',
    )


# web3Extension.ts


def create_web3_extension(
    chain_id: int,
    fee_payer: str,
    fee_payer_sig: bytes,
) -> MessageGenerated[ExtensionOptionsWeb3Tx]:
    """Create web3 extension options message."""
    message = ExtensionOptionsWeb3Tx(
        typed_data_chain_id=chain_id,
        fee_payer=fee_payer,
        fee_payer_sig=fee_payer_sig,
    )
    return MessageGenerated(
        message=message,
        path='ethermint.types.v1.ExtensionOptionsWeb3Tx',
    )
