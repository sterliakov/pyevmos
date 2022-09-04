from __future__ import annotations

from evmos.eip712 import (
    MSG_EDIT_VALIDATOR_TYPES,
    create_eip712,
    create_msg_edit_validator,
    generate_fee,
    generate_message,
    generate_types,
)
from evmos.proto import create_msg_edit_validator as proto_msg_edit_validator
from evmos.proto import create_transaction
from evmos.transactions.common import Chain, Fee, Sender, TxGenerated


def create_tx_msg_edit_validator(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    *,
    validator_address: str,  # FIXME: was str|None, but not allowed deeper
    moniker: str | None = None,
    identity: str | None = None,
    website: str | None = None,
    security_contact: str | None = None,
    details: str | None = None,
    commission_rate: str | None = None,
    min_self_delegation: str | None = None,
) -> TxGenerated:
    """Create a transaction with validator editing message."""
    # EIP712
    fee_object = generate_fee(
        fee.amount,
        fee.denom,
        fee.gas,
        sender.account_address,
    )
    types = generate_types(MSG_EDIT_VALIDATOR_TYPES)
    msg = create_msg_edit_validator(
        moniker=moniker,
        identity=identity,
        website=website,
        security_contact=security_contact,
        details=details,
        validator_address=validator_address,
        commission_rate=commission_rate,
        min_self_delegation=min_self_delegation,
    )
    messages = generate_message(
        str(sender.account_number),
        str(sender.sequence),
        chain.cosmos_chain_id,
        memo,
        fee_object,
        msg,
    )
    eip_to_sign = create_eip712(types, chain.chain_id, messages)

    # Cosmos
    proto_message = proto_msg_edit_validator(
        moniker=moniker,
        identity=identity,
        website=website,
        security_contact=security_contact,
        details=details,
        validator_address=validator_address,
        commission_rate=commission_rate,
        min_self_delegation=min_self_delegation,
    )
    tx = create_transaction(
        proto_message,
        memo,
        fee.amount,
        fee.denom,
        int(fee.gas),
        'ethsecp256',
        sender.pubkey,
        sender.sequence,
        sender.account_number,
        chain.cosmos_chain_id,
    )

    return TxGenerated(
        sign_direct=tx.sign_direct,
        legacy_amino=tx.legacy_amino,
        eip_to_sign=eip_to_sign,
    )
