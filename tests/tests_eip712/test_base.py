from evmos.eip712.base import (
    create_eip712,
    generate_fee,
    generate_message,
    generate_types,
)


def test_generate_fee():
    assert generate_fee(
        '20',
        'aphoton',
        '20000',
        'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
    ) == {
        'amount': [{'amount': '20', 'denom': 'aphoton'}],
        'gas': '20000',
        'feePayer': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
    }


def test_generate_types():
    assert generate_types(
        {
            'MsgValue': [
                {'name': 'fromAddress', 'type': 'string'},
                {'name': 'toAddress', 'type': 'string'},
                {'name': 'amount', 'type': 'TypeAmount[]'},
            ],
            'TypeAmount': [
                {'name': 'denom', 'type': 'string'},
                {'name': 'amount', 'type': 'string'},
            ],
        }
    ) == {
        'EIP712Domain': [
            {'name': 'name', 'type': 'string'},
            {'name': 'version', 'type': 'string'},
            {'name': 'chainId', 'type': 'uint256'},
            {'name': 'verifyingContract', 'type': 'string'},
            {'name': 'salt', 'type': 'string'},
        ],
        'Tx': [
            {'name': 'accountNumber', 'type': 'string'},
            {'name': 'chainId', 'type': 'string'},
            {'name': 'fee', 'type': 'Fee'},
            {'name': 'memo', 'type': 'string'},
            {'name': 'msgs', 'type': 'Msg[]'},
            {'name': 'sequence', 'type': 'string'},
        ],
        'Fee': [
            {'name': 'feePayer', 'type': 'string'},
            {'name': 'amount', 'type': 'Coin[]'},
            {'name': 'gas', 'type': 'string'},
        ],
        'Coin': [
            {'name': 'denom', 'type': 'string'},
            {'name': 'amount', 'type': 'string'},
        ],
        'Msg': [
            {'name': 'type', 'type': 'string'},
            {'name': 'value', 'type': 'MsgValue'},
        ],
        'MsgValue': [
            {'name': 'fromAddress', 'type': 'string'},
            {'name': 'toAddress', 'type': 'string'},
            {'name': 'amount', 'type': 'TypeAmount[]'},
        ],
        'TypeAmount': [
            {'name': 'denom', 'type': 'string'},
            {'name': 'amount', 'type': 'string'},
        ],
    }


def test_generate_message():
    assert generate_message(
        '8',
        '0',
        'ethermint_9000-1',
        '',
        generate_fee(
            '20',
            'aphoton',
            '20000',
            'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
        ),
        {
            'type': 'cosmos-sdk/MsgSend',
            'value': {
                'amount': [{'amount': '1', 'denom': 'aphoton'}],
                'fromAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
                'toAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
            },
        },
    ) == {
        'accountNumber': '8',
        'chainId': 'ethermint_9000-1',
        'fee': {
            'amount': [{'amount': '20', 'denom': 'aphoton'}],
            'gas': '20000',
            'feePayer': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
        },
        'memo': '',
        'msgs': [
            {
                'type': 'cosmos-sdk/MsgSend',
                'value': {
                    'amount': [{'amount': '1', 'denom': 'aphoton'}],
                    'fromAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
                    'toAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
                },
            },
        ],
        'sequence': '0',
    }


def test_generate_base():
    assert create_eip712(
        generate_types(
            {
                'MsgValue': [
                    {'name': 'fromAddress', 'type': 'string'},
                    {'name': 'toAddress', 'type': 'string'},
                    {'name': 'amount', 'type': 'TypeAmount[]'},
                ],
                'TypeAmount': [
                    {'name': 'denom', 'type': 'string'},
                    {'name': 'amount', 'type': 'string'},
                ],
            }
        ),
        9000,
        generate_message(
            '8',
            '0',
            'ethermint_9000-1',
            '',
            generate_fee(
                '20',
                'aphoton',
                '20000',
                'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
            ),
            {
                'type': 'cosmos-sdk/MsgSend',
                'value': {
                    'amount': [{'amount': '1', 'denom': 'aphoton'}],
                    'fromAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
                    'toAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
                },
            },
        ),
    ) == {
        'types': {
            'EIP712Domain': [
                {'name': 'name', 'type': 'string'},
                {'name': 'version', 'type': 'string'},
                {'name': 'chainId', 'type': 'uint256'},
                {'name': 'verifyingContract', 'type': 'string'},
                {'name': 'salt', 'type': 'string'},
            ],
            'Tx': [
                {'name': 'accountNumber', 'type': 'string'},
                {'name': 'chainId', 'type': 'string'},
                {'name': 'fee', 'type': 'Fee'},
                {'name': 'memo', 'type': 'string'},
                {'name': 'msgs', 'type': 'Msg[]'},
                {'name': 'sequence', 'type': 'string'},
            ],
            'Fee': [
                {'name': 'feePayer', 'type': 'string'},
                {'name': 'amount', 'type': 'Coin[]'},
                {'name': 'gas', 'type': 'string'},
            ],
            'Coin': [
                {'name': 'denom', 'type': 'string'},
                {'name': 'amount', 'type': 'string'},
            ],
            'Msg': [
                {'name': 'type', 'type': 'string'},
                {'name': 'value', 'type': 'MsgValue'},
            ],
            'MsgValue': [
                {'name': 'fromAddress', 'type': 'string'},
                {'name': 'toAddress', 'type': 'string'},
                {'name': 'amount', 'type': 'TypeAmount[]'},
            ],
            'TypeAmount': [
                {'name': 'denom', 'type': 'string'},
                {'name': 'amount', 'type': 'string'},
            ],
        },
        'primaryType': 'Tx',
        'domain': {
            'name': 'Cosmos Web3',
            'version': '1.0.0',
            'chainId': 9000,
            'verifyingContract': 'cosmos',
            'salt': '0',
        },
        'message': {
            'accountNumber': '8',
            'chainId': 'ethermint_9000-1',
            'fee': {
                'amount': [{'amount': '20', 'denom': 'aphoton'}],
                'gas': '20000',
                'feePayer': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
            },
            'memo': '',
            'msgs': [
                {
                    'type': 'cosmos-sdk/MsgSend',
                    'value': {
                        'amount': [{'amount': '1', 'denom': 'aphoton'}],
                        'fromAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
                        'toAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
                    },
                },
            ],
            'sequence': '0',
        },
    }
