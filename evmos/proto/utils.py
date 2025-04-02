from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

from betterproto import Message
from betterproto.lib.google.protobuf import Any as GoogleAny

_M = TypeVar('_M', bound=Message, covariant=True)


@dataclass
class MessageGenerated(Generic[_M]):
    """Structure of message generated by our library."""

    message: _M
    """Actual message instance."""
    path: str
    """Path where this was generated inside the library."""


def create_any_message(msg: MessageGenerated[Message]) -> GoogleAny:
    """Wrap message (coerced to binary) with convenience wrapper.

    Returns:
        :class:`~betterproto.lib.google.protobuf.Any`
    """
    return GoogleAny(
        type_url=f'/{msg.path}',
        value=bytes(msg.message),
    )
