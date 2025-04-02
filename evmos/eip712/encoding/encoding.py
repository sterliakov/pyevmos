from __future__ import annotations

from typing_extensions import deprecated

from evmos.eip712.base import EIP712Signatures, EIPToSign
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
                "Could not cast byte_src to either StdSignDoc or SignDoc:\n"
                f"Amino: {amino_exc!r}\n"
                f"Protobuf: {proto_exc!r}"
            ) from proto_exc


@deprecated("Call .hash() directly instead")
def hash_eip712(eip712: EIPToSign) -> EIP712Signatures:
    """Return the hashed V4 EIP-712 domain and struct objects to be signed."""
    return eip712.hash()
