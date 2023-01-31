from __future__ import annotations

from base64 import b64encode
from dataclasses import dataclass

import betterproto
import pytest
from betterproto.lib.google.protobuf import Any

from evmos.eip712.encoding.registry import Registry
from evmos.proto.autogen.py.cosmos.tx.v1beta1 import TxBody


def test_works_with_default_msg():
    registry = Registry()
    Coin = registry.lookup_type('/cosmos.base.v1beta1.Coin')  # noqa: N806
    MsgSend = registry.lookup_type('/cosmos.bank.v1beta1.MsgSend')  # noqa: N806
    assert Coin
    assert MsgSend

    coin = Coin(denom='ucosm', amount='1234567890')
    msg_send = MsgSend(
        from_address='cosmos1pkptre7fdkl6gfrzlesjjvhxhlc3r4gmmk8rs6',
        to_address='cosmos1qypqxpq9qcrsszg2pvxq6rs0zqg3yyc5lzv7xu',
        amount=[coin],
    )
    msg_send_wrapped = Any(
        type_url='/cosmos.bank.v1beta1.MsgSend',
        value=bytes(msg_send),
    )
    tx_body = TxBody(
        messages=[msg_send_wrapped],
        memo='Some memo',
        timeout_height=9999,
        extension_options=[],
    )

    tx_body_decoded = TxBody().parse(bytes(tx_body))
    msg = tx_body_decoded.messages[0]
    assert msg.type_url
    assert msg.value

    decoder = registry.lookup_type(msg.type_url)
    msg_send_decoded = decoder().parse(msg.value)

    assert msg_send_decoded.from_address == msg_send.from_address
    assert msg_send_decoded.to_address == msg_send.to_address
    assert msg_send_decoded.amount == msg_send.amount

    parsed = registry.decode('/cosmos.tx.v1beta1.TxBody', bytes(tx_body))
    assert parsed.messages[0] == msg_send_wrapped


def test_works_with_custom_msg():
    # From https://gist.github.com/fadeev/a4981eff1cf3a805ef10e25313d5f2b7
    type_url = '/blog.MsgCreatePost'

    @dataclass(eq=False, repr=False)
    class MsgCreatePostOriginal(betterproto.Message):
        creator: str = betterproto.string_field(1)
        title: str = betterproto.string_field(2)
        body: str = betterproto.string_field(3)
        attachment: bytes = betterproto.bytes_field(4)

    registry = Registry()
    registry.register(type_url, MsgCreatePostOriginal)
    MsgCreatePost = registry.lookup_type(type_url)  # noqa: N806
    assert MsgCreatePost

    # Usually constructor is better, but here's what is done under the hood:
    msg_demo = MsgCreatePost().from_dict(
        {
            'creator': 'Me',
            'title': 'Something with stars',
            'body': 'la la la',
            'attachment': b64encode(bytes.fromhex('AABBAABB66FE')),
        }
    )
    msg_demo_wrapped = Any(
        type_url=type_url,
        value=bytes(msg_demo),
    )
    # Usually constructor is better, but here's what is done under the hood:
    tx_body = TxBody().from_dict(
        {
            'messages': [msg_demo_wrapped.to_dict()],
            'memo': 'Some memo',
            'timeout_height': 9999,
            'extension_options': [],
        }
    )
    tx_body_decoded = TxBody().parse(bytes(tx_body))
    msg = tx_body_decoded.messages[0]
    assert msg.type_url
    assert msg.value

    decoder = registry.lookup_type(msg.type_url)
    msg_demo_decoded = decoder().parse(msg.value)
    assert msg_demo_decoded.creator == 'Me'
    assert msg_demo_decoded.title == 'Something with stars'
    assert msg_demo_decoded.body == 'la la la'
    assert msg_demo_decoded.attachment == bytes.fromhex('AABBAABB66FE')


def test_fails_with_undeclared_type():
    registry = Registry()
    wrapped = Any(
        type_url='/foobar',
        value=b'1234',
    )
    type_ = registry.lookup_type(wrapped.type_url)
    assert type_ is None
    with pytest.raises(KeyError, match=r'Unregistered type url'):
        registry.decode(wrapped.type_url, wrapped.value)
