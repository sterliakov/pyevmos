from __future__ import annotations

from evmos.constants import NOT_MODIFY
from evmos.proto.autogen.py.cosmos.staking.v1beta1 import Description, MsgEditValidator
from evmos.proto.utils import MessageGenerated


def create_msg_edit_validator(
    *,
    moniker: str | None,
    identity: str | None,
    website: str | None,
    security_contact: str | None,
    details: str | None,
    validator_address: str,
    commission_rate: str | None,
    min_self_delegation: str | None,
) -> MessageGenerated[MsgEditValidator]:
    """Create message for validator editing."""
    message = MsgEditValidator(
        description=Description(
            moniker=moniker or NOT_MODIFY,
            identity=identity or NOT_MODIFY,
            website=website or NOT_MODIFY,
            security_contact=security_contact or NOT_MODIFY,
            details=details or NOT_MODIFY,
        ),
        validator_address=validator_address,
        commission_rate=str(commission_rate or "<nil>"),
        min_self_delegation=str(min_self_delegation or "<nil>"),
    )

    return MessageGenerated(
        message=message,
        path="cosmos.staking.v1beta1.MsgEditValidator",
    )
