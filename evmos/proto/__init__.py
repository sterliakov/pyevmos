from __future__ import annotations

from typing import Sequence

from evmos.proto.autogen.py.cosmos.bank.v1beta1 import MsgSend
from evmos.proto.autogen.py.cosmos.base.v1beta1 import Coin
from evmos.proto.autogen.py.cosmos.gov.v1beta1 import MsgVote, VoteOption
from evmos.proto.autogen.py.cosmos.tx import v1beta1 as tx
from evmos.proto.autogen.py.ethermint.evm import v1 as ethermint
from evmos.proto.autogen.py.ethermint.types.v1 import ExtensionOptionsWeb3Tx
from evmos.proto.autogen.py.ibc.applications.transfer.v1 import MsgTransfer
from evmos.proto.autogen.py.ibc.core.client.v1 import Height
from evmos.proto.utils import MessageGenerated

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
    """Deserialize :class:`evmos.proto.autogen.py.ethermint.evm.v1.NsgEthereumTx`."""
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


def bytes_to_tx_raw(binary_data: bytes) -> tx.TxRaw:
    """Deserialize :class:`evmos.proto.autogen.py.cosmos.tx.v1beta1.TxRaw`."""
    return tx.TxRaw().parse(binary_data)


def bytes_to_tx_body(binary_data: bytes) -> tx.TxBody:
    """Deserialize :class:`evmos.proto.autogen.py.cosmos.tx.v1beta1.TxBody`."""
    return tx.TxBody().parse(binary_data)


def bytes_to_auth_info(binary_data: bytes) -> tx.AuthInfo:
    """Deserialize :class:`evmos.proto.autogen.py.cosmos.tx.v1beta1.AuthInfo`."""
    return tx.AuthInfo().parse(binary_data)


def create_tx_raw(
    body_bytes: bytes,
    auth_info_bytes: bytes,
    signatures: Sequence[bytes],
) -> MessageGenerated[tx.TxRaw]:
    """Create message with raw transaction."""
    message = tx.TxRaw(
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
