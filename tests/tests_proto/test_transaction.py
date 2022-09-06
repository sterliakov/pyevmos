from __future__ import annotations

import base64

from betterproto import casing

from evmos.proto import create_msg_send
from evmos.proto.transactions import (
    SIGN_DIRECT,
    create_auth_info,
    create_body,
    create_fee,
    create_sig_doc,
    create_signer_info,
    create_transaction,
)


def test_create_body():
    msg_send = create_msg_send(
        'evmos18lw704zeyg5zs098lq7x6ypfkfjqlzzln5qh89',
        'evmos1ndfagggdkgv9vc7wha5gj2zzrnyqd3r704lr4q',
        '69420',
        'aphoton',
    )
    res = create_body(msg_send, 'this is a test')
    assert res.to_pydict(casing=casing.snake_case) == {
        'messages': [
            {
                'type_url': '/cosmos.bank.v1beta1.MsgSend',
                # fmt: off
                'value': bytes(
                    [
                        10, 44, 101, 118, 109, 111, 115, 49, 56, 108, 119, 55, 48, 52,
                        122, 101, 121, 103, 53, 122, 115, 48, 57, 56, 108,
                        113, 55, 120, 54, 121, 112, 102, 107, 102, 106, 113, 108, 122,
                        122, 108, 110, 53, 113, 104, 56, 57, 18, 44, 101, 118,
                        109, 111, 115, 49, 110, 100, 102, 97, 103, 103, 103, 100,
                        107, 103, 118, 57, 118, 99, 55, 119, 104, 97, 53, 103, 106,
                        50, 122, 122, 114, 110, 121, 113, 100, 51, 114, 55, 48, 52,
                        108, 114, 52, 113, 26, 16, 10, 7, 97, 112, 104,
                        111, 116, 111, 110, 18, 5, 54, 57, 52, 50, 48,
                    ]
                ),
                # fmt: on
            },
        ],
        'memo': 'this is a test',
        # 'extension_options': [],  # default
        # 'non_critical_extension_options': [],  # default
    }


def test_create_fee():
    value = '20'
    denom = 'aphoton'
    gas = 20000
    fee = create_fee(value, denom, gas)
    assert fee.to_pydict(casing=casing.snake_case) == {
        'amount': [{'amount': value, 'denom': denom}],
        'gas_limit': gas,
    }


def test_create_signer_info():
    # fmt: off
    pubkey = bytes(
        [
            10, 33, 2, 136, 177, 245, 49, 184, 120, 113, 219,
            192, 55, 41, 81, 135, 37, 92, 174, 75, 160,
            196, 188, 55, 202, 114, 97, 5, 178, 20, 10, 253, 14, 105, 23,
        ]
    )
    # fmt: on
    sequence = 0
    info = create_signer_info('ethsecp256k1', pubkey, sequence, SIGN_DIRECT)
    assert info.to_pydict(casing=casing.snake_case) == {
        'public_key': {
            'type_url': '/ethermint.crypto.v1.ethsecp256k1.PubKey',
            # value: 'CiMKIQKIsfUxuHhx28A3KVGHJVyuS6DEvDfKcmEFshQK/Q5pFw=='
            # fmt: off
            'value': bytes(
                [
                    10, 35, 10, 33, 2, 136, 177, 245, 49, 184, 120, 113, 219, 192,
                    55, 41, 81, 135, 37, 92, 174, 75, 160, 196, 188, 55, 202, 114,
                    97, 5, 178, 20, 10, 253, 14, 105, 23,
                ]
            ),
            # fmt: on
        },
        'mode_info': {'single': {'mode': 1}},
        # 'sequence': 0,  # default
    }


def test_create_auth_info():
    # fmt: off
    pubkey = bytes(
        [
            10, 33, 2, 136, 177, 245, 49, 184, 120, 113,
            219, 192, 55, 41, 81, 135, 37, 92, 174, 75, 160,
            196, 188, 55, 202, 114, 97, 5, 178, 20, 10, 253, 14, 105, 23,
        ]
    )
    # fmt: on
    sequence = 0
    info = create_signer_info('ethsecp256k1', pubkey, sequence, SIGN_DIRECT)
    value = '20'
    denom = 'aphoton'
    gas = 20000
    fee = create_fee(value, denom, gas)

    msg = create_auth_info(info, fee)
    assert msg.to_pydict(casing=casing.snake_case) == {
        'signer_infos': [
            {
                'public_key': {
                    'type_url': '/ethermint.crypto.v1.ethsecp256k1.PubKey',
                    # value: 'CiMKIQKIsfUxuHhx28A3KVGHJVyuS6DEvDfKcmEFshQK/Q5pFw=='
                    # fmt: off
                    'value': bytes(
                        [
                            10, 35, 10, 33, 2, 136, 177, 245, 49, 184, 120, 113,
                            219, 192, 55, 41, 81, 135, 37, 92, 174, 75, 160, 196,
                            188, 55, 202, 114, 97, 5, 178, 20, 10, 253, 14, 105, 23,
                        ]
                    ),
                    # fmt: on
                },
                'mode_info': {'single': {'mode': SIGN_DIRECT}},
                # 'sequence': sequence,  # default
            },
        ],
        'fee': {
            'amount': [{'amount': value, 'denom': denom}],
            'gas_limit': gas,
        },
    }


def test_create_sig_doc():
    msg_send = create_msg_send(
        'evmos18lw704zeyg5zs098lq7x6ypfkfjqlzzln5qh89',
        'evmos1ndfagggdkgv9vc7wha5gj2zzrnyqd3r704lr4q',
        '69420',
        'aphoton',
    )
    body = create_body(msg_send, 'this is a test')

    # fmt: off
    pubkey = bytes(
        [
            10, 33, 2, 136, 177, 245, 49, 184, 120, 113, 219, 192, 55, 41, 81, 135,
            37, 92, 174, 75, 160, 196, 188, 55, 202, 114, 97, 5, 178, 20, 10, 253, 14,
            105, 23,
        ]
    )
    # fmt: on
    sequence = 0
    info = create_signer_info('ethsecp256k1', pubkey, sequence, SIGN_DIRECT)
    value = '20'
    denom = 'aphoton'
    gas = 20000
    fee = create_fee(value, denom, gas)

    auth_info = create_auth_info(info, fee)

    chain_id = 'evmos-9000_1'

    account_number = 0

    res = create_sig_doc(
        bytes(body),
        bytes(auth_info),
        chain_id,
        account_number,
    )
    # auth_info_bytes are not equal to TS version. I confirmed with google.protobuf
    # that both encoding variants are valid.
    # Bytes from TS implementation are parseable for betterproto.
    assert res.to_pydict(casing=casing.snake_case) == {
        # fmt: off
        'body_bytes': bytes(
            [
                10, 142, 1, 10, 28, 47, 99, 111, 115, 109, 111,
                115, 46, 98, 97, 110, 107, 46, 118, 49, 98, 101,
                116, 97, 49, 46, 77, 115, 103, 83, 101, 110, 100, 18,
                110, 10, 44, 101, 118, 109, 111, 115, 49, 56, 108, 119, 55, 48,
                52, 122, 101, 121, 103, 53, 122, 115, 48, 57, 56, 108,
                113, 55, 120, 54, 121, 112, 102, 107, 102, 106, 113, 108, 122,
                122, 108, 110, 53, 113, 104, 56, 57, 18, 44, 101,
                118, 109, 111, 115, 49, 110, 100, 102, 97, 103, 103,
                103, 100, 107, 103, 118, 57, 118, 99, 55, 119, 104, 97,
                53, 103, 106, 50, 122, 122, 114, 110, 121, 113, 100, 51,
                114, 55, 48, 52, 108, 114, 52, 113, 26, 16, 10, 7, 97, 112,
                104, 111, 116, 111, 110, 18, 5, 54, 57, 52, 50, 48, 18, 14,
                116, 104, 105, 115, 32, 105, 115, 32, 97, 32, 116, 101, 115, 116,
            ]
        ),
        'auth_info_bytes': bytes(
            [
                10,
                89,  # 2 bytes less than TS implementation
                10, 81, 10, 40, 47, 101, 116, 104, 101, 114, 109, 105, 110, 116,
                46, 99, 114, 121, 112, 116, 111, 46, 118, 49, 46, 101, 116, 104, 115,
                101, 99, 112, 50, 53, 54, 107, 49, 46, 80, 117, 98, 75, 101, 121, 18,
                37, 10, 35, 10, 33, 2, 136, 177, 245, 49, 184, 120, 113, 219, 192, 55,
                41, 81, 135, 37, 92, 174, 75, 160, 196, 188, 55, 202, 114, 97, 5, 178,
                20, 10, 253, 14, 105, 23, 18, 4, 10, 2, 8, 1,
                # 24, 0,  # This is sequence (should be 0 for 0, but is ignored here)
                18, 19, 10, 13, 10,
                7, 97, 112, 104, 111, 116, 111, 110, 18, 2, 50, 48, 16, 160, 156, 1,
            ]
        ),
        # fmt: on
        'chain_id': chain_id,
        # 'account_number': account_number,  # default
    }


def test_valid_eip712():
    msg = create_msg_send(
        'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
        'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
        '1',
        'aphoton',
    )
    tx = create_transaction(
        msg,
        '',
        '20',
        'aphoton',
        200000,
        'ethsecp256',
        'AgTw+4v0daIrxsNSW4FcQ+IoingPseFwHO1DnssyoOqZ',
        1,
        9,
        '',
    )
    assert base64.b64encode(bytes(tx.legacy_amino.body)) == (
        b'CogBChwvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dTZW5kEmgKK2V0aG0xdGZlZ'
        b'2Y1MG41eGwwaGQ1Y3hmempjYTN5bHNmcGcwZm5lZDVncW0SK2V0aG0xdGZlZ2Y'
        b'1MG41eGwwaGQ1Y3hmempjYTN5bHNmcGcwZm5lZDVncW0aDAoHYXBob3RvbhIBMQ=='
    )
    assert base64.b64encode(bytes(tx.legacy_amino.auth_info)) == (
        b'ClkKTwooL2V0aGVybWludC5jcnlwdG8udjEuZXRoc2VjcDI1NmsxLlB1YktleRIj'
        b'CiECBPD7i/R1oivGw1JbgVxD4iiKeA+x4XAc7UOeyzKg6pkSBAoCCH8YARITCg0K'
        b'B2FwaG90b24SAjIwEMCaDA=='
    )
    assert base64.b64encode(bytes(tx.sign_direct.body)) == (
        b'CogBChwvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dTZW5kEmgKK2V0aG0xdGZlZ2Y1'
        b'MG41eGwwaGQ1Y3hmempjYTN5bHNmcGcwZm5lZDVncW0SK2V0aG0xdGZlZ2Y1MG41'
        b'eGwwaGQ1Y3hmempjYTN5bHNmcGcwZm5lZDVncW0aDAoHYXBob3RvbhIBMQ=='
    )
    assert base64.b64encode(bytes(tx.sign_direct.auth_info)) == (
        b'ClkKTwooL2V0aGVybWludC5jcnlwdG8udjEuZXRoc2VjcDI1NmsxLlB1YktleRIj'
        b'CiECBPD7i/R1oivGw1JbgVxD4iiKeA+x4XAc7UOeyzKg6pkSBAoCCAEYARITCg0K'
        b'B2FwaG90b24SAjIwEMCaDA=='
    )
