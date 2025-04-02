from __future__ import annotations

import json
from dataclasses import asdict

import pytest

from evmos.eip712 import MSG_DELEGATE_TYPES, MSG_SEND_TYPES, MSG_VOTE_TYPES
from evmos.eip712.base import generate_types
from evmos.eip712.encoding.decode_amino import decode_amino_sign_doc

eip712_domain = {
    'name': None,
    'version': None,
    'chainId': 9000,
    'verifyingContract': None,
    'salt': None,
}
eip712_primary_type = 'Tx'


def test_decodes_msg_send_payloads():
    orig = {
        'account_number': '0',
        'chain_id': 'evmos_9000-1',
        'fee': {'amount': [{'amount': '200', 'denom': 'aevmos'}], 'gas': '200000'},
        'memo': '',
        'msgs': [
            {
                'type': 'cosmos-sdk/MsgSend',
                'value': {
                    'amount': [{'amount': '100000000000000000', 'denom': 'aevmos'}],
                    'from_address': 'evmos1wsaurpy7uxm2n8vfggc9ehpjlzmfssx305awxx',
                    'to_address': 'evmos1hnmrdr0jc2ve3ycxft0gcjjtrdkncpmmkeamf9',
                },
            }
        ],
        'sequence': '1',
    }
    encoded = json.dumps(orig).encode()
    eip712 = decode_amino_sign_doc(encoded)

    assert asdict(eip712.domain) == eip712_domain
    assert eip712.primaryType == eip712_primary_type
    assert eip712.types.pop('EIP712Domain') == eip712.domain.pick_types()
    assert eip712.types == generate_types(MSG_SEND_TYPES)
    assert eip712.message == {
        'account_number': '0',
        'chain_id': 'evmos_9000-1',
        'fee': {
            'amount': [
                {
                    'amount': '200',
                    'denom': 'aevmos',
                },
            ],
            'gas': '200000',
            'feePayer': 'evmos1wsaurpy7uxm2n8vfggc9ehpjlzmfssx305awxx',
        },
        'memo': '',
        'msgs': [
            {
                'type': 'cosmos-sdk/MsgSend',
                'value': {
                    'from_address': 'evmos1wsaurpy7uxm2n8vfggc9ehpjlzmfssx305awxx',
                    'to_address': 'evmos1hnmrdr0jc2ve3ycxft0gcjjtrdkncpmmkeamf9',
                    'amount': [{'amount': '100000000000000000', 'denom': 'aevmos'}],
                },
            },
        ],
        'sequence': '1',
    }


def test_decodes_msg_vote_payloads():
    orig = {
        'account_number': '0',
        'chain_id': 'evmos_9000-1',
        'fee': {'amount': [{'amount': '2000', 'denom': 'aevmos'}], 'gas': '200000'},
        'memo': '',
        'msgs': [
            {
                'type': 'cosmos-sdk/MsgVote',
                'value': {
                    'option': 1,
                    'proposal_id': '1',
                    'voter': 'evmos1ygxq25vlp3u4lqyys6vrsdaz9ww9kgrx7xlhty',
                },
            }
        ],
        'sequence': '1',
    }
    encoded = json.dumps(orig).encode()
    eip712 = decode_amino_sign_doc(encoded)

    assert asdict(eip712.domain) == eip712_domain
    assert eip712.primaryType == eip712_primary_type
    assert eip712.types.pop('EIP712Domain') == eip712.domain.pick_types()
    assert eip712.types == generate_types(MSG_VOTE_TYPES)
    assert eip712.message == {
        'account_number': '0',
        'chain_id': 'evmos_9000-1',
        'fee': {
            'amount': [{'amount': '2000', 'denom': 'aevmos'}],
            'gas': '200000',
            'feePayer': 'evmos1ygxq25vlp3u4lqyys6vrsdaz9ww9kgrx7xlhty',
        },
        'memo': '',
        'msgs': [
            {
                'type': 'cosmos-sdk/MsgVote',
                'value': {
                    'option': 1,
                    'proposal_id': '1',
                    'voter': 'evmos1ygxq25vlp3u4lqyys6vrsdaz9ww9kgrx7xlhty',
                },
            },
        ],
        'sequence': '1',
    }


def test_decodes_msg_delegate_payloads():
    orig = {
        'account_number': '0',
        'chain_id': 'evmos_9000-1',
        'fee': {'amount': [{'amount': '2000', 'denom': 'aevmos'}], 'gas': '200000'},
        'memo': '',
        'msgs': [
            {
                'type': 'cosmos-sdk/MsgDelegate',
                'value': {
                    'amount': {'amount': '1000000000000000000', 'denom': 'aevmos'},
                    'delegator_address': 'evmos1sn65acv26jg8kzahlf8gq7cl8pyz3qcps07eem',
                    'validator_address': (
                        'evmosvaloper1sn65acv26jg8kzahlf8gq7cl8pyz3qcpap3fcx'
                    ),
                },
            }
        ],
        'sequence': '1',
    }
    encoded = json.dumps(orig).encode()
    eip712 = decode_amino_sign_doc(encoded)

    assert asdict(eip712.domain) == eip712_domain
    assert eip712.primaryType == eip712_primary_type
    assert eip712.types.pop('EIP712Domain') == eip712.domain.pick_types()
    assert eip712.types == generate_types(MSG_DELEGATE_TYPES)
    assert eip712.message == {
        'account_number': '0',
        'chain_id': 'evmos_9000-1',
        'fee': {
            'amount': [{'amount': '2000', 'denom': 'aevmos'}],
            'gas': '200000',
            'feePayer': 'evmos1sn65acv26jg8kzahlf8gq7cl8pyz3qcps07eem',
        },
        'memo': '',
        'msgs': [
            {
                'type': 'cosmos-sdk/MsgDelegate',
                'value': {
                    'amount': {'amount': '1000000000000000000', 'denom': 'aevmos'},
                    'delegator_address': (
                        'evmos1sn65acv26jg8kzahlf8gq7cl8pyz3qcps07eem'
                    ),
                    'validator_address': (
                        'evmosvaloper1sn65acv26jg8kzahlf8gq7cl8pyz3qcpap3fcx'
                    ),
                },
            },
        ],
        'sequence': '1',
    }


def test_throws_on_invalid_byte_payload():
    orig = {
        'account_number': '0',
        'chain_id': 'evmos_9000-1',
        'fee': {'amount': [{'amount': '2000', 'denom': 'aevmos'}], 'gas': '200000'},
        'memo': '',
        'msgs': [
            {
                'type': 'cosmos-sdk/MsgDelegate',
                'value': {
                    'amount': {'amount': '1000000000000000000', 'denom': 'aevmos'},
                    'delegator_address': 'evmos1sn65acv26jg8kzahlf8gq7cl8pyz3qcps07eem',
                    'validator_address': (
                        'evmosvaloper1sn65acv26jg8kzahlf8gq7cl8pyz3qcpap3fcx'
                    ),
                },
            }
        ],
        'sequence': '1',
    }
    encoded = json.dumps(orig).encode()[:-1]  # strip one byte

    with pytest.raises(json.JSONDecodeError):
        decode_amino_sign_doc(encoded)


def test_fills_blank_fee_payers():
    sign_doc = {
        'account_number': '0',
        'chain_id': 'evmos_9000-1',
        'fee': {
            'amount': [{'amount': '2000', 'denom': 'aevmos'}],
            'gas': '200000',
            'feePayer': '',
        },
        'memo': '',
        'msgs': [
            {
                'type': 'cosmos-sdk/MsgVote',
                'value': {
                    'option': 1,
                    'proposal_id': '1',
                    'voter': 'evmos1ygxq25vlp3u4lqyys6vrsdaz9ww9kgrx7xlhty',
                },
            },
        ],
        'sequence': '1',
    }

    encoded = json.dumps(sign_doc).encode()
    eip712 = decode_amino_sign_doc(encoded)
    message = eip712.message

    assert message['fee']['feePayer'] == 'evmos1ygxq25vlp3u4lqyys6vrsdaz9ww9kgrx7xlhty'
