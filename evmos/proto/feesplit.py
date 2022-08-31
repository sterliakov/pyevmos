from __future__ import annotations

from typing import Sequence

from evmos.proto.autogen.py.evmos.feesplit import v1 as feesplit
from evmos.proto.utils import MessageGenerated

# msgCancelFeeSplit.ts


def create_msg_cancel_fee_split(
    contract_address: str,
    deployer_address: str,
) -> MessageGenerated[feesplit.MsgCancelFeeSplit]:
    """Create a message for fee split cancellation."""
    msg = feesplit.MsgCancelFeeSplit(
        contract_address=contract_address,
        deployer_address=deployer_address,
    )
    return MessageGenerated(
        message=msg,
        path='evmos.feesplit.v1.MsgCancelFeeSplit',
    )


# msgRegisterFeeSplit.ts


def create_msg_register_fee_split(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
    nonces: Sequence[int],
) -> MessageGenerated[feesplit.MsgRegisterFeeSplit]:
    """Create a message for fee split registration."""
    msg = feesplit.MsgRegisterFeeSplit(
        contract_address=contract_address,
        deployer_address=deployer_address,
        withdrawer_address=withdrawer_address,
        nonces=list(nonces),
    )
    return MessageGenerated(
        message=msg,
        path='evmos.feesplit.v1.MsgRegisterFeeSplit',
    )


# msgUpdateFeeSplit.ts


def create_msg_update_fee_split(
    contract_address: str,
    deployer_address: str,
    withdrawer_address: str,
) -> MessageGenerated[feesplit.MsgUpdateFeeSplit]:
    """Create a message for fee split update."""
    msg = feesplit.MsgUpdateFeeSplit(
        contract_address=contract_address,
        deployer_address=deployer_address,
        withdrawer_address=withdrawer_address,
    )
    return MessageGenerated(
        message=msg,
        path='evmos.feesplit.v1.MsgUpdateFeeSplit',
    )
