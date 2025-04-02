from __future__ import annotations

from evmos.proto.autogen.py.cosmos.base.v1beta1 import Coin
from evmos.proto.autogen.py.evmos.erc20.v1 import MsgConvertCoin, MsgConvertErc20
from evmos.proto.utils import MessageGenerated

# messageConvertCoin.ts


def create_msg_convert_coin(
    denom: str,
    amount: str,
    receiver: str,
    sender: str,
) -> MessageGenerated[MsgConvertCoin]:
    """Create message for coin conversion."""
    msg = MsgConvertCoin(
        coin=Coin(denom=denom, amount=amount),
        receiver=receiver,
        sender=sender,
    )
    return MessageGenerated(
        message=msg,
        path="evmos.erc20.v1.MsgConvertCoin",
    )


# messageConvertERC20.ts


def create_msg_convert_erc20(
    contract_address: str,
    amount: str,
    receiver: str,
    sender: str,
) -> MessageGenerated[MsgConvertErc20]:
    """Create message for ERC20 conversion."""
    msg = MsgConvertErc20(
        contract_address=contract_address,
        amount=amount,
        receiver=receiver,
        sender=sender,
    )
    return MessageGenerated(
        message=msg,
        path="evmos.erc20.v1.MsgConvertERC20",
    )
