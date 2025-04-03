from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import asdict, dataclass
from typing import TYPE_CHECKING, Any, TypedDict

from eth_typing import ChecksumAddress, HexAddress
from eth_utils import keccak

from evmos.utils.eip_712_hash import encode_data

if TYPE_CHECKING:
    from evmos.utils.eip_712_hash import _FieldDef


class WithValidator(TypedDict):
    """:class:`~typing.TypedDict` with string ``validator_address`` field."""

    validator_address: str
    """Validator address."""


class MsgWithValidatorInterface(TypedDict):
    """Validator editing message."""

    type: str
    """Type for ABI encoding."""
    value: WithValidator
    """Message itself."""


class MsgInterface(TypedDict):
    """Validator editing message."""

    type: str
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

    def pick_types(self) -> list[_FieldDef]:
        known_fields: list[_FieldDef] = [
            {"name": "name", "type": "string"},
            {"name": "version", "type": "string"},
            {"name": "chainId", "type": "uint256"},
            {"name": "verifyingContract", "type": "address"},
            {"name": "salt", "type": "bytes32"},
        ]
        return [f for f in known_fields if getattr(self, f["name"]) is not None]

    def hash(self) -> bytes:
        return keccak(
            encode_data(
                "EIP712Domain", {"EIP712Domain": self.pick_types()}, asdict(self)
            )
        )


class EIP712Signatures(TypedDict):
    domain: bytes
    message: bytes


@dataclass
class EIPToSign:
    """EIP message to sign."""

    types: dict[str, list[_FieldDef]]
    """Message types for ABI encoding, mapping name to type."""
    primaryType: str  # noqa: N815
    """Type name of ``message`` attribute."""
    domain: Domain
    """Domain."""
    message: dict[str, Any]
    """Message to sign itself, mapping."""

    def hash(self) -> EIP712Signatures:
        """Return the hashed V4 EIP-712 domain and struct objects to be signed.

        Throws on errors.
        """
        try:
            return {
                "domain": self.domain.hash(),
                "message": self.hash_message(),
            }
        except (ValueError, TypeError, KeyError, IndexError) as e:
            raise ValueError("Could not hash EIP-712 object") from e

    def hash_message(self: EIPToSign) -> bytes:
        """Hash message part of a EIP-712 message."""
        return keccak(
            encode_data(
                self.primaryType,
                self.types,
                self.message,
            )
        )


def create_eip712(
    types: dict[str, Any], chain_id: int, message: dict[str, Any]
) -> EIPToSign:
    """Create `EIP712 <https://eips.ethereum.org/EIPS/eip-712>`_ data."""
    domain = Domain(chainId=chain_id)
    return EIPToSign(
        types=types | {"EIP712Domain": domain.pick_types()},
        primaryType="Tx",
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
        "account_number": account_number,
        "chain_id": chain_cosmos_id,
        "fee": fee,
        "memo": memo,
        "msgs": msgs,
        "sequence": sequence,
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
        "Tx": [
            {"name": "account_number", "type": "string"},
            {"name": "chain_id", "type": "string"},
            {"name": "fee", "type": "Fee"},
            {"name": "memo", "type": "string"},
            {"name": "msgs", "type": "Msg[]"},
            {"name": "sequence", "type": "string"},
        ],
        "Fee": [
            {"name": "feePayer", "type": "string"},
            {"name": "amount", "type": "Coin[]"},
            {"name": "gas", "type": "string"},
        ],
        "Coin": [
            {"name": "denom", "type": "string"},
            {"name": "amount", "type": "string"},
        ],
        "Msg": [
            {"name": "type", "type": "string"},
            {"name": "value", "type": "MsgValue"},
        ],
    }
    types.update(msg_values)
    return types


def generate_fee(amount: str, denom: str, gas: str, fee_payer: str) -> dict[str, Any]:
    """Generate fee definition structure."""
    return {
        "amount": [{"amount": amount, "denom": denom}],
        "gas": gas,
        "feePayer": fee_payer,
    }
