from evmos.eip712 import create_msg_send


def test_create_msg_send():
    assert create_msg_send(
        '1',
        'aphoton',
        'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
        'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
    ) == {
        'type': 'cosmos-sdk/MsgSend',
        'value': {
            'amount': [{'amount': '1', 'denom': 'aphoton'}],
            'fromAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
            'toAddress': 'ethm1tfegf50n5xl0hd5cxfzjca3ylsfpg0fned5gqm',
        },
    }
