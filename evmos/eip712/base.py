from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Optional, Sequence, TypedDict, Union

from eth_typing import ChecksumAddress, HexAddress

from evmos.utils.eip_712_hash import _FieldT


class WithValidator(TypedDict):
    """:class:`~typing.TypedDict` with string ``validator_address`` field."""

    validator_address: str
    """Validator address."""


class MsgWithValidatorInterface(TypedDict):
    """Validator editing message."""

    type: str  # noqa: A003
    """Type for ABI encoding."""
    value: WithValidator
    """Message itself."""


class MsgInterface(TypedDict):
    """Validator editing message."""

    type: str  # noqa: A003
    """Type for ABI encoding."""
    value: Any
    """Message itself."""


@dataclass
class Domain:
    """This describes ``domain`` field of :class:`EIPToSign`."""

    name: str | None = None
    """Domain name."""
    version: str | None = None
    """Version (usually ``1.0.0``)."""
    chainId: int | None = None  # noqa: N815
    """Chain ID."""
    verifyingContract: HexAddress | ChecksumAddress | None = None  # noqa: N815
    """Verifying contract address."""
    salt: str | None = None
    """Used salt (usually ``'0'``)."""

    def pick_types(self) -> list[_FieldT]:
        known_fields: list[_FieldT] = [
            {'name': 'name', 'type': 'string'},
            {'name': 'version', 'type': 'string'},
            {'name': 'chainId', 'type': 'uint256'},
            {'name': 'verifyingContract', 'type': 'address'},
            {'name': 'salt', 'type': 'bytes32'},
        ]
        return [f for f in known_fields if getattr(self, f['name']) is not None]


@dataclass
class EIPToSign:
    """EIP message to sign."""

    types: dict[str, list[_FieldT]]
    """Message types for ABI encoding, mapping name to type."""
    primaryType: str  # noqa: N815
    """Type name of ``message`` attribute."""
    domain: Domain
    """Domain."""
    message: dict[str, Any]
    """Message to sign itself, mapping."""


def create_eip712(
    types: dict[str, Any], chain_id: int, message: dict[str, Any]
) -> EIPToSign:
    """Create `EIP712 <https://eips.ethereum.org/EIPS/eip-712>`_ data."""
    domain = Domain(chainId=chain_id)
    return EIPToSign(
        types=types | {'EIP712Domain': domain.pick_types()},
        primaryType='Tx',
        domain=domain,
        message=message,
    )


def generate_message_with_multiple_transactions(
    account_number: str,
    sequence: str,
    chain_cosmos_id: str,
    memo: str,
    fee: dict[str, Any],
    msgs: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Create a message with multiple transactions included."""
    return {
        'account_number': account_number,
        'chain_id': chain_cosmos_id,
        'fee': fee,
        'memo': memo,
        'msgs': msgs,
        'sequence': sequence,
    }


def generate_message(
    account_number: str,
    sequence: str,
    chain_cosmos_id: str,
    memo: str,
    fee: dict[str, Any],
    msg: Mapping[str, Any],
) -> dict[str, Any]:
    """Create a message with one transaction included."""
    return generate_message_with_multiple_transactions(
        account_number,
        sequence,
        chain_cosmos_id,
        memo,
        fee,
        [msg],
    )


def generate_types(msg_values: dict[str, Any]) -> dict[str, Any]:
    """Generate EIP-712 types."""
    types = {
        'Tx': [
            {'name': 'account_number', 'type': 'string'},
            {'name': 'chain_id', 'type': 'string'},
            {'name': 'fee', 'type': 'Fee'},
            {'name': 'memo', 'type': 'string'},
            {'name': 'msgs', 'type': 'Msg[]'},
            {'name': 'sequence', 'type': 'string'},
        ],
        'Fee': [
            {'name': 'feePayer', 'type': 'string'},
            {'name': 'amount', 'type': 'Coin[]'},
            {'name': 'gas', 'type': 'string'},
        ],
        'Coin': [
            {'name': 'denom', 'type': 'string'},
            {'name': 'amount', 'type': 'string'},
        ],
        'Msg': [
            {'name': 'type', 'type': 'string'},
            {'name': 'value', 'type': 'MsgValue'},
        ],
    }
    types.update(msg_values)
    return types


def generate_fee(amount: str, denom: str, gas: str, fee_payer: str) -> dict[str, Any]:
    """Generate fee definition structure."""
    return {
        'amount': [{'amount': amount, 'denom': denom}],
        'gas': gas,
        'feePayer': fee_payer,
    }
