import base64

from betterproto import casing

from evmos.proto import (
    bytes_to_auth_info,
    bytes_to_legacy_tx,
    bytes_to_msg_ethereum_tx,
    bytes_to_tx_body,
    bytes_to_tx_raw,
)

blockchain_tx = (
    'CroICoYICh8vZXRoZXJtaW50LmV2bS52MS5Nc2dFdGhlcmV1bVR4EuIHCpIHChovZXRoZXJtaW50'
    'LmV2bS52MS5MZWdhY3lUeBLzBgiMCBINNTAwMDAwMDAwMDAwMBiAn0kiKjB4NzUyYTIxYUI2M2Zj'
    'MkM3ODg3NzQ3ZTc1NDQwNWQ5NzVDRDM1MUQ1NCoBMDLkBaKr5U4AAAAAAAAAAAAAAAAAAAAAAAAA'
    'AAAAAIuIFFmETVNZmgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbl+kIHZQAAAAAAAAAAAAAAAAAA'
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    'AMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAP5jeVCccTRCn3sK'
    '792m8rdNgra8AAAAAAAAAAAAAAAA4cEQ4bG0od7QyvPkK/vbt7XXzhwAAAAAAAAAAAAAAAAAAAAA'
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACbyAAAAAAAAAAAA'
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAJxAAAAAAAAAAAAAAAADjbNV4hCwlX2oYGChpFhFTFalMQAAA'
    'AAAAAAAAAAAAAMISIyScooOXtLZUHf+uzFOb/wxZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAm8gAAAAAAAAAAAAAAAAAAAAAAAAAA'
    'AAAAAAAAAAAAACcQAAAAAAAAAAAAAAAAGCQUFZw+7xQ1r5G88NEqvL4nekYAAAAAAAAAAAAAAABc'
    'f4pXDVeO2E5j/fp7Huct6uGuIwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJvIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAn'
    'EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//wAHOgFWQiBXQ6FNYBwVz4wVf5KpY7ldwXg3'
    'TnOCeO6xfcuzDA5JIEogNw+TTcQqXv3X+fyanCS4bDl3f3bHL5f7+T9UV9z/wckRAAAAAACIikAa'
    'QjB4ZmQxODk2ZWEwNzQ4MjllODQ1OGRlMjE2NjBkZjdiNTc3OWQzMzQ5Y2Y4YjA3YWU2ZmMxZmNh'
    'OTY3ZGRhNzRjY/o/LgosL2V0aGVybWludC5ldm0udjEuRXh0ZW5zaW9uT3B0aW9uc0V0aGVyZXVt'
    'VHgSJhIkCh4KB2Jhc2Vjcm8SEzYwMDAwMDAwMDAwMDAwMDAwMDAQgJ9J'
)


def test_bytes_to_msg_ethereum_tx_from_raw_tx():
    # Create txRaw
    tx_raw_proto = bytes_to_tx_raw(base64.b64decode(blockchain_tx))

    # Create body
    body_proto = bytes_to_tx_body(tx_raw_proto.body_bytes)

    # Create the authInfo
    auth_info_proto = bytes_to_auth_info(tx_raw_proto.auth_info_bytes)
    assert auth_info_proto.to_pydict(casing=casing.snake_case) == {
        # 'signer_infos': [],  # default
        'fee': {
            'amount': [{'amount': '6000000000000000000', 'denom': 'basecro'}],
            'gas_limit': 1200000,
        },
    }

    # Get the messages
    body_proto_messages = body_proto.messages
    assert body_proto_messages

    # Make sure that the message is MsgEthTx
    assert body_proto_messages[0].type_url == '/ethermint.evm.v1.MsgEthereumTx'

    # Create the MsgEthTx proto
    assert body_proto_messages[0].value
    msg_eth_tx = bytes_to_msg_ethereum_tx(
        body_proto_messages[0].value,
    )
    # msg_eth_tx = msg_eth_tx.toObject()

    # Create the LegacyTx/AccessListTx/DynamicFeeTx depending on the type_url
    assert msg_eth_tx.data.type_url == '/ethermint.evm.v1.LegacyTx'

    # Create the LegacyTX
    # eth_tx = bytes_to_legacy_tx(msg_eth_tx.data?.value as Uint8Array).toObject()
    eth_tx = bytes_to_legacy_tx(msg_eth_tx.data.value)
    assert eth_tx.nonce == 1036
    assert eth_tx.gas_price == '5000000000000'
    assert eth_tx.gas == 1200000
    assert eth_tx.to == '0x752a21aB63fc2C7887747e754405d975CD351D54'

    assert eth_tx.value == '0'
    # fmt: off
    assert eth_tx.data == bytes([
        162, 171, 229, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 139, 136, 20, 89, 132, 77, 83, 89, 154, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 229, 250, 66,
        7, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 254, 99, 121, 80, 156, 113, 52, 66, 159,
        123, 10, 239, 221, 166, 242, 183, 77, 130, 182, 188, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 225, 193, 16, 225, 177, 180, 161, 222, 208, 202, 243,
        228, 43, 251, 219, 183, 181, 215, 206, 28, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 38, 242, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 39, 16, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 227, 108, 213, 120, 132, 44, 37, 95, 106, 24, 24, 40, 105,
        22, 17, 83, 21, 169, 76, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 194,
        18, 35, 36, 156, 162, 131, 151, 180, 182, 84, 29, 255, 174, 204, 83,
        155, 255, 12, 89, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 38, 242, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 39, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 36, 20,
        21, 156, 62, 239, 20, 53, 175, 145, 188, 240, 209, 42, 188, 190, 39,
        122, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 92, 127, 138, 87, 13, 87,
        142, 216, 78, 99, 253, 250, 123, 30, 231, 45, 234, 225, 174, 35, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 38, 242, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 39, 16,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 255, 255, 0, 7,
    ])
    # fmt: on
