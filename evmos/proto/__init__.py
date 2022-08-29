from __future__ import annotations

from evmos.proto.autogen.py.cosmos.bank.v1beta1 import MsgSend
from evmos.proto.autogen.py.cosmos.base.v1beta1 import Coin
from evmos.proto.utils import MessageGenerated

# msgSend.ts


def create_msg_send(
    from_address: str,
    to_address: str,
    amount: str,
    denom: str,
) -> MessageGenerated:
    """Create :class:`~evmos.proto.utils.MessageGenerated` for given args."""
    value = Coin(denom=denom, amount=amount)

    message = MsgSend(
        from_address=from_address,
        to_address=to_address,
        amount=[value],
    )
    return {
        'message': message,
        'path': 'cosmos.bank.v1beta1.MsgSend',
    }
