from __future__ import annotations

import json
from pprint import pprint

import pytest

from evmos.eip712.base import Domain, EIPToSign
from evmos.eip712.encoding.encoding import decode_sign_doc_to_typed_data

eip712_domain = Domain(
    name="Cosmos Web3",
    version="1.0.0",
    chainId=9000,
    verifyingContract=None,
    salt=None,
)
eip712_primary_type = "Tx"


def test_decodes_amino_signdocs():
    orig = {
        "account_number": "0",
        "chain_id": "evmos_9000-1",
        "fee": {"amount": [{"amount": "200", "denom": "aevmos"}], "gas": "200000"},
        "memo": "",
        "msgs": [
            {
                "type": "cosmos-sdk/MsgSend",
                "value": {
                    "amount": [{"amount": "100000000000000000", "denom": "aevmos"}],
                    "from_address": "evmos1wsaurpy7uxm2n8vfggc9ehpjlzmfssx305awxx",
                    "to_address": "evmos1hnmrdr0jc2ve3ycxft0gcjjtrdkncpmmkeamf9",
                },
            }
        ],
        "sequence": "1",
    }
    encoded = json.dumps(orig).encode()
    decoded = decode_sign_doc_to_typed_data(encoded)
    assert decoded
    pprint(decoded)


def test_decodes_protobuf_signdocs():
    # fmt: off
    encoded = bytes([
        10, 157, 1, 10, 154, 1, 10, 28, 47, 99, 111, 115, 109, 111, 115,
        46, 98, 97, 110, 107, 46, 118, 49, 98, 101, 116, 97, 49, 46, 77,
        115, 103, 83, 101, 110, 100, 18, 122, 10, 44, 101, 118, 109, 111, 115,
        49, 116, 121, 118, 112, 113, 53, 55, 51, 54, 108, 122, 106, 50, 121,
        122, 109, 106, 48, 107, 97, 110, 113, 120, 103, 55, 119, 102, 50, 57,
        102, 109, 112, 50, 100, 114, 113, 116, 48, 18, 44, 101, 118, 109, 111,
        115, 49, 104, 110, 109, 114, 100, 114, 48, 106, 99, 50, 118, 101, 51,
        121, 99, 120, 102, 116, 48, 103, 99, 106, 106, 116, 114, 100, 107, 110,
        99, 112, 109, 109, 107, 101, 97, 109, 102, 57, 26, 28, 10, 6, 97,
        101, 118, 109, 111, 115, 18, 18, 49, 48, 48, 48, 48, 48, 48, 48,
        48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 18, 112, 10, 89, 10,
        79, 10, 40, 47, 101, 116, 104, 101, 114, 109, 105, 110, 116, 46, 99,
        114, 121, 112, 116, 111, 46, 118, 49, 46, 101, 116, 104, 115, 101, 99,
        112, 50, 53, 54, 107, 49, 46, 80, 117, 98, 75, 101, 121, 18, 35,
        10, 33, 3, 49, 50, 222, 101, 16, 162, 111, 232, 18, 113, 67, 108,
        229, 229, 56, 46, 213, 147, 92, 122, 233, 142, 164, 59, 1, 106, 220,
        154, 240, 182, 35, 139, 18, 4, 10, 2, 8, 1, 24, 1, 18, 19,
        10, 13, 10, 6, 97, 101, 118, 109, 111, 115, 18, 3, 50, 48, 48,
        16, 192, 154, 12, 26, 12, 101, 118, 109, 111, 115, 95, 57, 48, 48,
        48, 45, 49,
    ])
    # fmt: on

    decoded = decode_sign_doc_to_typed_data(encoded)
    assert decoded
    pprint(decoded)


def test_throws_decoding_invalid_payload():
    orig = {
        "account_number": "0",
        "chain_id": "evmos_9000-1",
        "fee": {"amount": [{"amount": "200", "denom": "aevmos"}], "gas": "200000"},
        "memo": "",
        "msgs": [
            {
                "type": "cosmos-sdk/MsgSend",
                "value": {
                    "amount": [{"amount": "100000000000000000", "denom": "aevmos"}],
                    "from_address": "evmos1wsaurpy7uxm2n8vfggc9ehpjlzmfssx305awxx",
                    "to_address": "evmos1hnmrdr0jc2ve3ycxft0gcjjtrdkncpmmkeamf9",
                },
            }
        ],
        "sequence": "1",
    }
    encoded = json.dumps(orig).encode()[:-1]

    with pytest.raises(
        ValueError, match=r"Could not cast byte_src to either StdSignDoc or SignDoc"
    ):
        decode_sign_doc_to_typed_data(encoded)


def test_hashes_eip712_structs_0():
    # Amino MSG_VOTE
    encoded = json.dumps({
        "account_number": "0",
        "chain_id": "evmos_9000-1",
        "fee": {"amount": [{"amount": "2000", "denom": "aevmos"}], "gas": "200000"},
        "memo": "",
        "msgs": [
            {
                "type": "cosmos-sdk/MsgVote",
                "value": {
                    "option": 1,
                    "proposal_id": 1,
                    "voter": "evmos1ygxq25vlp3u4lqyys6vrsdaz9ww9kgrx7xlhty",
                },
            }
        ],
        "sequence": "1",
    }).encode()
    eip712 = decode_sign_doc_to_typed_data(encoded)
    print(eip712)
    hashed = eip712.hash()
    assert (
        hashed["message"].hex()
        == "ab08501e02408252b4f674263d976f2995feb4bb8127b393baf75c54cfd86d76"
    )


def test_hashes_eip712_structs_1():
    # Protobuf MSG_SEND
    encoded = bytes.fromhex(
        "0a9d010a9a010a1c2f636f736d6f732e62616e6b2e763162657461312e4d736753656e64127a0a2c65766d6f73317479767071353733366c7a6a32797a6d6a306b616e7178673777663239666d70326472717430122c65766d6f7331686e6d726472306a633276653379637866743067636a6a7472646b6e63706d6d6b65616d66391a1c0a066165766d6f73121231303030303030303030303030303030303012700a590a4f0a282f65746865726d696e742e63727970746f2e76312e657468736563703235366b312e5075624b657912230a21033132de6510a26fe81271436ce5e5382ed5935c7ae98ea43b016adc9af0b6238b12040a020801180112130a0d0a066165766d6f73120332303010c09a0c1a0c65766d6f735f393030302d31"
    )
    eip712 = decode_sign_doc_to_typed_data(encoded)
    hashed = eip712.hash()
    assert (
        hashed["message"].hex()
        == "a6a4e73512097abdf92fa255904b317eb37b727de8513d03877df4671e033e88"
    )


def test_throws_hashing_invalid_eip712():
    invalid_eip712 = EIPToSign(
        domain=eip712_domain,
        primaryType=eip712_primary_type,
        types={
            "EIP712Domain": "invalid format",
        },
        message={
            "recipient": "content",
        },
    )

    with pytest.raises(ValueError, match=r"Could not hash EIP-712 object"):
        invalid_eip712.hash()
