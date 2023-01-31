from __future__ import annotations

from typing import Any, Mapping, Sequence

from evmos.eip712 import (
    MSG_CANCEL_REVENUE_TYPES,
    MSG_REGISTER_REVENUE_TYPES,
    MSG_UPDATE_REVENUE_TYPES,
    create_msg_cancel_revenue,
    create_msg_register_revenue,
    create_msg_update_revenue,
)
from evmos.proto import (
    MessageGenerated,
    MsgCancelRevenue,
    MsgRegisterRevenue,
    MsgUpdateRevenue,
)
from evmos.proto import create_msg_cancel_revenue as proto_msg_cancel_revenue
from evmos.proto import create_msg_register_revenue as proto_msg_register_revenue
from evmos.proto import create_msg_update_revenue as proto_msg_update_revenue
from evmos.transactions.common import to_generated

# msgCancelRevenue.ts


@to_generated(MSG_CANCEL_REVENUE_TYPES)
def create_tx_msg_cancel_revenue(
    contract_address: str,
    deployer_address: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgCancelRevenue]]:
    """Create transaction with message for revenue cancellation."""
    msg = create_msg_cancel_revenue(
        contract_address,
        deployer_address,
    )

    msg_cosmos = proto_msg_cancel_revenue(
        contract_address,
        deployer_address,
    )

    return msg, msg_cosmos


# msgRegisterRevenue.ts


@to_generated(MSG_REGISTER_REVENUE_TYPES)
def create_tx_msg_register_revenue(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> tuple[Mapping[str, Any], MessageGenerated[MsgRegisterRevenue]]:
    """Create transaction with message for revenue registration."""
    msg = create_msg_register_revenue(
        contract_address,
        deployer_address,
        withdrawer_address,
        nonces,
    )

    msg_cosmos = proto_msg_register_revenue(
        contract_address,
        deployer_address,
        withdrawer_address,
        nonces,
    )
    return msg, msg_cosmos


# msgUpdateRevenue.ts


@to_generated(MSG_UPDATE_REVENUE_TYPES)
def create_tx_msg_update_revenue(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> tuple[Mapping[str, Any], MessageGenerated[MsgUpdateRevenue]]:
    """Create transaction with message for revenue update."""
    msg = create_msg_update_revenue(
        contract_address,
        deployer_address,
        withdrawer_address,
    )

    msg_cosmos = proto_msg_update_revenue(
        contract_address,
        deployer_address,
        withdrawer_address,
    )

    return msg, msg_cosmos
