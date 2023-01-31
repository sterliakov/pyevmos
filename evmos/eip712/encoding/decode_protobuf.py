from __future__ import annotations

from enum import Enum, unique
from typing import Any

from betterproto import Casing, Message

from evmos.eip712.base import EIPToSign, create_eip712, generate_fee, generate_message
from evmos.eip712.encoding.decode_amino import (
    MsgTypes,
    eip712_message_type,
    get_fee_payer_from_msg,
)
from evmos.eip712.encoding.registry import Registry
from evmos.eip712.encoding.utils import parse_chain_id
from evmos.proto.autogen.py.cosmos.gov.v1beta1 import MsgVote
from evmos.proto.autogen.py.cosmos.staking.v1beta1 import MsgDelegate
from evmos.proto.autogen.py.cosmos.tx.v1beta1 import AuthInfo, SignDoc, TxBody


@unique
class ProtoMsgTypes(str, Enum):
    """Type URLs for supported proto messages."""

    MSG_SEND = '/cosmos.bank.v1beta1.MsgSend'
    MSG_VOTE = '/cosmos.gov.v1beta1.MsgVote'
    MSG_DELEGATE = '/cosmos.staking.v1beta1.MsgDelegate'


def _protobuf_type_url_to_amino_type(type_url: str) -> MsgTypes:
    mapping: dict[ProtoMsgTypes, MsgTypes] = {
        ProtoMsgTypes.MSG_SEND: MsgTypes.MSG_SEND,
        ProtoMsgTypes.MSG_VOTE: MsgTypes.MSG_VOTE,
        ProtoMsgTypes.MSG_DELEGATE: MsgTypes.MSG_DELEGATE,
    }
    try:
        return mapping[ProtoMsgTypes(type_url)]
    except KeyError:
        raise NotImplementedError('Invalid Protobuf message type url received')


def _convert_protobuf_msg_to_amino_msg(obj: Message) -> dict[str, Any]:
    """Convert a Protobuf Message to its corresponding Amino representation.

    Necessary, since EIP-712 types require messages to be in Amino form.
    """
    assert isinstance(obj, Message)
    return obj.to_pydict(casing=Casing.SNAKE)


def _make_eip712_protobuf_registry() -> Registry:
    """Generate Protobuf registry."""
    registry = Registry()
    # Registry includes MSG_SEND by default
    registry.register(ProtoMsgTypes.MSG_VOTE, MsgVote)
    registry.register(ProtoMsgTypes.MSG_DELEGATE, MsgDelegate)
    return registry


def decode_protobuf_sign_doc(bytes_src: bytes) -> EIPToSign:
    """Decode the ProtobufSignDoc to EIP712."""
    # Decode Protobuf tx
    registry = _make_eip712_protobuf_registry()

    sign_doc = SignDoc().parse(bytes_src)
    tx_body = TxBody().parse(sign_doc.body_bytes)
    auth_info = AuthInfo().parse(sign_doc.auth_info_bytes)

    if not tx_body.messages:
        raise ValueError('Expected a message in Protobuf SignDoc but received empty.')
    elif len(tx_body.messages) > 1:
        # Enforce single message for now
        raise NotImplementedError(
            'Expected single message in Protobuf SignDoc '
            f'but received {len(tx_body.messages)}.'
        )

    first_msg = tx_body.messages[0]

    # Enforce single signer for now
    if len(auth_info.signer_infos) != 1:
        raise NotImplementedError(
            'Expected single signer in Protobuf SignDoc '
            f'but received {len(auth_info.signer_infos)}.'
        )

    signer = auth_info.signer_infos[0]

    # Enforce presence of fee
    if not auth_info.fee:
        raise ValueError(
            'Expected fee object to be included in payload, got undefined',
        )

    # Enforce single fee
    if len(auth_info.fee.amount) != 1:
        raise ValueError(
            'Expected single fee in Protobuf SignDoc '
            f'but received {len(auth_info.fee.amount)}'
        )
    amount = auth_info.fee.amount[0]

    # Parse SignDoc fields
    account_number = str(sign_doc.account_number)
    sequence = str(signer.sequence)
    chain_id = sign_doc.chain_id
    memo = tx_body.memo

    # Decode message using registry
    proto_msg = registry.decode(first_msg.type_url, first_msg.value)

    # Convert Protobuf message to expected Amino type
    amino_msg = {
        'type': _protobuf_type_url_to_amino_type(first_msg.type_url),
        'value': _convert_protobuf_msg_to_amino_msg(proto_msg),
    }

    # Use the feePayer from the message if unset in body
    fee_payer = auth_info.fee.payer
    if not fee_payer:
        fee_payer = get_fee_payer_from_msg(amino_msg)

    gas_limit = str(auth_info.fee.gas_limit)
    fee = generate_fee(amount.amount, amount.denom, gas_limit, fee_payer)
    type_ = eip712_message_type(amino_msg)

    eip712_tx = generate_message(
        account_number,
        sequence,
        chain_id,
        memo,
        fee,
        amino_msg,
    )

    return create_eip712(type_, parse_chain_id(chain_id), eip712_tx)
