from __future__ import annotations

from betterproto import casing

from evmos.proto import create_msg_send


def test_create_message_send():
    message = create_msg_send(
        "evmos18lw704zeyg5zs098lq7x6ypfkfjqlzzln5qh89",
        "evmos1ndfagggdkgv9vc7wha5gj2zzrnyqd3r704lr4q",
        "69420",
        "aphoton",
    )
    assert message.message.to_pydict(casing=casing.snake_case) == {
        "from_address": "evmos18lw704zeyg5zs098lq7x6ypfkfjqlzzln5qh89",
        "to_address": "evmos1ndfagggdkgv9vc7wha5gj2zzrnyqd3r704lr4q",
        "amount": [{"denom": "aphoton", "amount": "69420"}],
    }

    assert message.path == "cosmos.bank.v1beta1.MsgSend"
