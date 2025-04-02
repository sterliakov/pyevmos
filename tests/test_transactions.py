from __future__ import annotations

import base64
from dataclasses import asdict

from evmos.transactions import (
    Chain,
    Fee,
    Sender,
    create_message_send,
    signature_to_web3_extension,
)

# msgSend.spec.ts


def test_msg_send_valid():
    chain = Chain(chain_id=9000, cosmos_chain_id='evmos_9000-1')

    sender = Sender(
        account_address='ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
        sequence=1,
        account_number=9,
        pubkey='AgTw+4v0daIrxsNSW4FcQ+IoingPseFwHO1DnssyoOqZ',
    )

    fee = Fee(amount='20', denom='aevmos', gas='200000')

    memo = ''

    # FIXME: there should be a way to pass a domain here.
    msg = create_message_send(
        chain,
        sender,
        fee,
        memo,
        destination_address='evmos1pmk2r32ssqwps42y3c9d4clqlca403yd9wymgr',
        amount='1',
        denom='aevmos',
    )

    assert base64.b64encode(bytes(msg.legacy_amino.body)).decode() == (
        'CogBChwvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dTZW5kEmgKK2V0aG0xdGZlZ2Y1MG'
        '41eGwwaGQ1Y3hmempjYTN5bHNmcGcwZm5lZDVncW0SLGV2bW9zMXBtazJyMzJzc3F3'
        'cHM0MnkzYzlkNGNscWxjYTQwM3lkOXd5bWdyGgsKBmFldm1vcxIBMQ=='
    )

    assert base64.b64encode(bytes(msg.legacy_amino.auth_info)).decode() == (
        'ClkKTwooL2V0aGVybWludC5jcnlwdG8udjEuZXRoc2VjcDI1NmsxLlB1YktleRIjCiECBPD7i/'
        'R1oivGw1JbgVxD4iiKeA+x4XAc7UOeyzKg6pkSBAoCCH8YARISCgwKBmFldm1vcxICMjAQwJoM'
    )
    assert msg.legacy_amino.sign_bytes == '2XbbRbgd5cQ05gDxc1xxKAH++HXulj5JSrwLI51R0ss='

    assert base64.b64encode(bytes(msg.sign_direct.body)).decode() == (
        'CogBChwvY29zbW9zLmJhbmsudjFiZXRhMS5Nc2dTZW5kEmgKK2V0aG0xdGZlZ2Y1MG41eGw'
        'waGQ1Y3hmempjYTN5bHNmcGcwZm5lZDVncW0SLGV2bW9zMXBtazJyMzJzc3F3cHM0MnkzYz'
        'lkNGNscWxjYTQwM3lkOXd5bWdyGgsKBmFldm1vcxIBMQ=='
    )
    assert base64.b64encode(bytes(msg.sign_direct.auth_info)).decode() == (
        'ClkKTwooL2V0aGVybWludC5jcnlwdG8udjEuZXRoc2VjcDI1NmsxLlB1YktleRIjCiECBPD7i/'
        'R1oivGw1JbgVxD4iiKeA+x4XAc7UOeyzKg6pkSBAoCCAEYARISCgwKBmFldm1vcxICMjAQwJoM'
    )
    assert msg.sign_direct.sign_bytes == 'gmgo2KWJ6FwXEH69W0xMGtrmjUMU182nxn9B3vUw2iI='

    assert asdict(msg.eip_to_sign) == {
        'domain': {
            'chainId': 9000,
            'name': None,
            'salt': None,
            'verifyingContract': None,
            'version': None,
        },
        'message': {
            'account_number': '9',
            'chain_id': 'evmos_9000-1',
            'fee': {
                'amount': [{'amount': '20', 'denom': 'aevmos'}],
                'feePayer': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
                'gas': '200000',
            },
            'memo': '',
            'msgs': [
                {
                    'type': 'cosmos-sdk/MsgSend',
                    'value': {
                        'amount': [{'amount': '1', 'denom': 'aevmos'}],
                        'from_address': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
                        'to_address': 'evmos1pmk2r32ssqwps42y3c9d4clqlca403yd9wymgr',
                    },
                },
            ],
            'sequence': '1',
        },
        'primaryType': 'Tx',
        'types': {
            'Coin': [
                {'name': 'denom', 'type': 'string'},
                {'name': 'amount', 'type': 'string'},
            ],
            'EIP712Domain': [
                {'name': 'chainId', 'type': 'uint256'},
            ],
            'Fee': [
                {'name': 'feePayer', 'type': 'string'},
                {'name': 'amount', 'type': 'Coin[]'},
                {'name': 'gas', 'type': 'string'},
            ],
            'Msg': [
                {'name': 'type', 'type': 'string'},
                {'name': 'value', 'type': 'MsgValue'},
            ],
            'MsgValue': [
                {'name': 'from_address', 'type': 'string'},
                {'name': 'to_address', 'type': 'string'},
                {'name': 'amount', 'type': 'TypeAmount[]'},
            ],
            'Tx': [
                {'name': 'account_number', 'type': 'string'},
                {'name': 'chain_id', 'type': 'string'},
                {'name': 'fee', 'type': 'Fee'},
                {'name': 'memo', 'type': 'string'},
                {'name': 'msgs', 'type': 'Msg[]'},
                {'name': 'sequence', 'type': 'string'},
            ],
            'TypeAmount': [
                {'name': 'denom', 'type': 'string'},
                {'name': 'amount', 'type': 'string'},
            ],
        },
    }


# web3Extension.spec.ts


def test_web3_extension():
    chain = Chain(
        chain_id=9000,
        cosmos_chain_id='evmos_9000-1',
    )

    sender = Sender(
        account_address='ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
        sequence=1,
        account_number=9,
        pubkey='AgTw+4v0daIrxsNSW4FcQ+IoingPseFwHO1DnssyoOqZ',
    )

    signature = bytes.fromhex(
        'ee543cc5a50d25a5bab4da0609bf63095804282aeb82f3fd16e03784db19723a727f5'
        '15b8d8e7b52c6f059f324ec5a651c92829f15e38e4d0db3788e230318a41c'
    )

    res = signature_to_web3_extension(chain, sender, signature)
    assert res.path == 'ethermint.types.v1.ExtensionOptionsWeb3Tx'
    assert base64.b64encode(bytes(res.message)).decode() == (
        'CKhGEitldGhtMXRmZWdmNTBuNXhsMGhkNWN4ZnpqY2EzeWxzZnBnMGZuZWQ1Z3FtGkHuVDzFpQ0lpb'
        'q02gYJv2MJWAQoKuuC8/0W4DeE2xlyOnJ/UVuNjntSxvBZ8yTsWmUckoKfFeOOTQ2zeI4jAxikHA=='
    )
