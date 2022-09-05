from __future__ import annotations

from typing import Any, Mapping, Sequence

from evmos.eip712 import (
    MSG_CANCEL_FEE_SPLIT_TYPES,
    MSG_REGISTER_FEE_SPLIT_TYPES,
    MSG_UPDATE_FEE_SPLIT_TYPES,
    create_msg_cancel_fee_split,
    create_msg_register_fee_split,
    create_msg_update_fee_split,
)
from evmos.proto import (
    MessageGenerated,
    MsgCancelFeeSplit,
    MsgRegisterFeeSplit,
    MsgUpdateFeeSplit,
)
from evmos.proto import create_msg_cancel_fee_split as proto_msg_cancel_fee_split
from evmos.proto import create_msg_register_fee_split as proto_msg_register_fee_split
from evmos.proto import create_msg_update_fee_split as proto_msg_update_fee_split
from evmos.transactions.common import to_generated

# msgCancelFeeSplit.ts


@to_generated(MSG_CANCEL_FEE_SPLIT_TYPES)
def create_tx_msg_cancel_fee_split(
    contract_address: str,
    deployer_address: str,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgCancelFeeSplit]]:
    """Create transaction with message for fee split cancellation."""
    # EIP712
    msg = create_msg_cancel_fee_split(
        contract_address,
        deployer_address,
    )

    # Cosmos
    msg_cosmos = proto_msg_cancel_fee_split(
        contract_address,
        deployer_address,
    )

    return msg, msg_cosmos


# msgRegisterFeeSplit.ts


@to_generated(MSG_REGISTER_FEE_SPLIT_TYPES)
def create_tx_msg_register_fee_split(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> tuple[Mapping[str, Any], MessageGenerated[MsgRegisterFeeSplit]]:
    """Create transaction with message for fee split registration."""
    # EIP712
    msg = create_msg_register_fee_split(
        contract_address,
        deployer_address,
        withdrawer_address,
        nonces,
    )

    # Cosmos
    msg_cosmos = proto_msg_register_fee_split(
        contract_address,
        deployer_address,
        withdrawer_address,
        nonces,
    )
    return msg, msg_cosmos


# msgUpdateFeeSplit.ts


@to_generated(MSG_UPDATE_FEE_SPLIT_TYPES)
def create_tx_msg_update_fee_split(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> tuple[Mapping[str, Any], MessageGenerated[MsgUpdateFeeSplit]]:
    """Create transaction with message for fee split update."""
    # EIP712
    msg = create_msg_update_fee_split(
        contract_address,
        deployer_address,
        withdrawer_address,
    )

    # Cosmos
    msg_cosmos = proto_msg_update_fee_split(
        contract_address,
        deployer_address,
        withdrawer_address,
    )

    return msg, msg_cosmos
