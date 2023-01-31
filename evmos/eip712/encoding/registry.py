"""Reduced registry module from cosmjs. Encoding capabilities removed.

https://github.com/cosmos/cosmjs/blob/main/packages/proto-signing/src/registry.ts
"""

from __future__ import annotations

from enum import Enum, unique

from betterproto import Message

from evmos.proto.autogen.py.cosmos.bank.v1beta1 import MsgSend
from evmos.proto.autogen.py.cosmos.base.v1beta1 import Coin
from evmos.proto.autogen.py.cosmos.tx.v1beta1 import TxBody


@unique
class DefaultTypeUrls(str, Enum):
    """Type URLS supported by default."""

    COSMOS_COIN = '/cosmos.base.v1beta1.Coin'
    COSMOS_MSG_SEND = '/cosmos.bank.v1beta1.MsgSend'
    COSMOS_TX_BODY = '/cosmos.tx.v1beta1.TxBody'


class Registry:
    """A mapping from protobuf type identifiers/type URLs to actual implementations.

    We support only betterproto-generated declarations.
    """

    types: dict[str, Message]

    def __init__(self, custom_types: dict[str, Message] | None = None):
        self.types = (
            dict(custom_types)
            if custom_types
            else {
                DefaultTypeUrls.COSMOS_COIN: Coin,
                DefaultTypeUrls.COSMOS_MSG_SEND: MsgSend,
                DefaultTypeUrls.COSMOS_TX_BODY: TxBody,
            }
        )

    def register(self, type_url: str, type_: Message) -> None:
        """Add new type to registry."""
        self.types[type_url] = type_

    def lookup_type(self, type_url: str) -> Message | None:
        """Looks up a type that was previously added to the registry."""
        return self.types.get(type_url)

    def _lookup_type_with_error(self, type_url: str) -> Message:
        type_ = self.lookup_type(type_url)
        if not type_:
            raise KeyError(f'Unregistered type url: {type_url}')
        return type_

    def decode(self, type_url: str, value: bytes) -> Message:
        """Decode binary value to the corresponding betterproto class.

        Unlike original JS implementation, does not convert messages to their types.
        This is omitted for least astonishment purpose: we return a TxBody,
        and it should have only `Any` instances as messages.
        """
        type_ = self._lookup_type_with_error(type_url)
        return type_().parse(value)
