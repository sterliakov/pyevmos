from __future__ import annotations

from typing import Sequence

from evmos.proto.autogen.py.evmos.revenue.v1 import (
    MsgCancelRevenue,
    MsgRegisterRevenue,
    MsgUpdateRevenue,
)
from evmos.proto.utils import MessageGenerated

# msgCancelRevenue.ts


def create_msg_cancel_revenue(
    contract_address: str,
    deployer_address: str,
) -> MessageGenerated[MsgCancelRevenue]:
    """Create a message for revenue cancellation."""
    msg = MsgCancelRevenue(
        contract_address=contract_address,
        deployer_address=deployer_address,
    )
    return MessageGenerated(
        message=msg,
        path='evmos.revenue.v1.MsgCancelRevenue',
    )


# msgRegisterRevenue.ts


def create_msg_register_revenue(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> MessageGenerated[MsgRegisterRevenue]:
    """Create a message for revenue registration."""
    msg = MsgRegisterRevenue(
        contract_address=contract_address,
        deployer_address=deployer_address,
        withdrawer_address=withdrawer_address,
        nonces=list(nonces),
    )
    return MessageGenerated(
        message=msg,
        path='evmos.revenue.v1.MsgRegisterRevenue',
    )


# msgUpdateRevenue.ts


def create_msg_update_revenue(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
) -> MessageGenerated[MsgUpdateRevenue]:
    """Create a message for revenue update."""
    msg = MsgUpdateRevenue(
        contract_address=contract_address,
        deployer_address=deployer_address,
        withdrawer_address=withdrawer_address,
    )
    return MessageGenerated(
        message=msg,
        path='evmos.revenue.v1.MsgUpdateRevenue',
    )
