from __future__ import annotations

import json
from enum import Enum, unique
from typing import Any

from evmos.eip712 import (
    MSG_DELEGATE_TYPES,
    MSG_SEND_TYPES,
    MSG_VOTE_TYPES,
    create_eip712,
    generate_types,
)
from evmos.eip712.base import EIPToSign
from evmos.eip712.encoding.utils import parse_chain_id


@unique
class MsgTypes(str, Enum):
    """Types for supported messages."""

    MSG_SEND = 'cosmos-sdk/MsgSend'
    MSG_VOTE = 'cosmos-sdk/MsgVote'
    MSG_DELEGATE = 'cosmos-sdk/MsgDelegate'


# TODO: support all other versions
def get_fee_payer_from_msg(msg: dict[str, Any]) -> str:
    """Get the feePayer from the message, using the message structure.

    This is required to provide the feePayer in the EIP712 object, and
    because Amino JS representations are in JSON and have no better interface.
    """
    mapping = {
        MsgTypes.MSG_SEND: 'from_address',
        MsgTypes.MSG_VOTE: 'voter',
        MsgTypes.MSG_DELEGATE: 'delegator_address',
    }
    try:
        target_field = mapping[msg['type']]
    except KeyError:
        raise NotImplementedError('Unsupported message type')

    try:
        return getattr(msg['value'], target_field)
    except AttributeError:
        return msg['value'][target_field]


def format_sign_doc(sign_doc: dict[str, Any]) -> dict[str, Any]:
    """Return the SignDoc after formatting."""
    sign_doc = sign_doc.copy()

    # Fill in the feePayer if the field is blank or unset
    if not sign_doc['fee'].get('feePayer'):
        sign_doc['fee']['feePayer'] = get_fee_payer_from_msg(sign_doc['msgs'][0])

    return sign_doc


def eip712_message_type(msg: dict[str, Any]) -> dict[str, Any]:
    """Generate EIP-712 types for the given message."""
    mapping = {
        MsgTypes.MSG_SEND: MSG_SEND_TYPES,
        MsgTypes.MSG_VOTE: MSG_VOTE_TYPES,
        MsgTypes.MSG_DELEGATE: MSG_DELEGATE_TYPES,
    }
    try:
        target_types = mapping[msg['type']]
    except KeyError:
        raise NotImplementedError('Unsupported message type')

    return generate_types(target_types)


def decode_amino_sign_doc(bytes_src: bytes) -> EIPToSign:
    """Decode the AminoSignDoc to EIP712 types."""
    raw_sign_doc = json.loads(bytes_src)

    # Enforce single-message signing for now
    if len(raw_sign_doc['msgs']) != 1:
        raise NotImplementedError(
            'Expected single message in Amino SignDoc '
            f'but received {len(raw_sign_doc.msgs)}.',
        )

    # Format SignDoc to match EIP-712 types
    sign_doc = format_sign_doc(raw_sign_doc)
    chain_id = sign_doc['chain_id']

    msg = sign_doc['msgs'][0]
    type_ = eip712_message_type(msg)

    return create_eip712(type_, parse_chain_id(chain_id), sign_doc)
