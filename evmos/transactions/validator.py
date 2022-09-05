from __future__ import annotations

from typing import Any, Mapping

from evmos.eip712 import MSG_EDIT_VALIDATOR_TYPES, create_msg_edit_validator
from evmos.proto import MessageGenerated, MsgEditValidator
from evmos.proto import create_msg_edit_validator as proto_msg_edit_validator
from evmos.transactions.common import to_generated


@to_generated(MSG_EDIT_VALIDATOR_TYPES)
def create_tx_msg_edit_validator(
    *,
    validator_address: str,  # FIXME: was str|None, but not allowed deeper
    moniker: str | None = None,
    identity: str | None = None,
    website: str | None = None,
    security_contact: str | None = None,
    details: str | None = None,
    commission_rate: str | None = None,
    min_self_delegation: str | None = None,
) -> tuple[Mapping[str, Any], MessageGenerated[MsgEditValidator]]:
    """Create a transaction with validator editing message."""
    # EIP712
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

    # Cosmos
    msg_cosmos = proto_msg_edit_validator(
        moniker=moniker,
        identity=identity,
        website=website,
        security_contact=security_contact,
        details=details,
        validator_address=validator_address,
        commission_rate=commission_rate,
        min_self_delegation=min_self_delegation,
    )

    return msg, msg_cosmos
