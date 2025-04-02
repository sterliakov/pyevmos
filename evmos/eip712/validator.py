from __future__ import annotations

from typing import Final

from evmos.constants import NOT_MODIFY
from evmos.eip712.base import MsgInterface

MSG_EDIT_VALIDATOR_TYPES: Final = {
    "TypeDescription": [
        {"name": "moniker", "type": "string"},
        {"name": "identity", "type": "string"},
        {"name": "website", "type": "string"},
        {"name": "security_contact", "type": "string"},
        {"name": "details", "type": "string"},
    ],
    "MsgValue": [
        {"name": "description", "type": "TypeDescription"},
        {"name": "validator_address", "type": "string"},
        {"name": "commission_rate", "type": "string"},
        {"name": "min_self_delegation", "type": "string"},
    ],
}
"""Types for validator editing message."""


def create_msg_edit_validator(
    *,
    moniker: str | None,
    identity: str | None,
    website: str | None,
    security_contact: str | None,
    details: str | None,
    validator_address: str,
    commission_rate: int | str | None = None,
    min_self_delegation: int | str | None = None,
) -> MsgInterface:
    """Create validator editing message."""
    return {
        "type": "cosmos-sdk/MsgEditValidator",
        "value": {
            "description": {
                "moniker": moniker or NOT_MODIFY,
                "identity": identity or NOT_MODIFY,
                "website": website or NOT_MODIFY,
                "security_contact": security_contact or NOT_MODIFY,
                "details": details or NOT_MODIFY,
            },
            "validator_address": validator_address,
            "commission_rate": str(commission_rate or "<nil>"),
            "min_self_delegation": str(min_self_delegation or "<nil>"),
        },
    }
