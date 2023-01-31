from __future__ import annotations

from dataclasses import asdict
from typing import Any

from eth_account.messages import hash_domain, hash_eip712_message

from evmos.eip712.base import EIPToSign
from evmos.eip712.encoding.decode_amino import decode_amino_sign_doc
from evmos.eip712.encoding.decode_protobuf import decode_protobuf_sign_doc


def decode_sign_doc_to_typed_data(byte_src: bytes) -> EIPToSign:
    """Decode Amino StdSignDoc or Protobuf SignDoc bytes into the EIP-712 TypedData.

    Throws on errors.
    """
    try:
        return decode_amino_sign_doc(byte_src)
    except ValueError as amino_exc:
        try:
            return decode_protobuf_sign_doc(byte_src)
        except ValueError as proto_exc:
            raise ValueError(
                'Could not cast byte_src to either StdSignDoc or SignDoc:\n'
                f'Amino: {amino_exc!r}\n'
                f'Protobuf: {proto_exc!r}'
            )


def hash_eip712(eip712: EIPToSign) -> dict[str, Any]:
    """Return the hashed V4 EIP-712 domain and struct objects to be signed.

    Throws on errors.
    """
    try:
        eip712_domain = hash_domain(
            {
                'primaryType': 'EIP712Domain',
                'domain': asdict(eip712.domain),
                'types': eip712.types,
            }
        )
        eip712_hash = hash_eip712_message(
            {
                'primaryType': eip712.primaryType,
                'message': eip712.message,
                'types': eip712.types,
            }
        )

        return {
            'domain': eip712_domain,
            'message': eip712_hash,
        }
    except (ValueError, TypeError, KeyError, IndexError) as e:
        raise ValueError('Could not hash EIP-712 object') from e
