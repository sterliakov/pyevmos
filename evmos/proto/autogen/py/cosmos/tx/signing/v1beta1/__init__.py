# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/tx/signing/v1beta1/signing.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf

from ....crypto.multisig import v1beta1 as ___crypto_multisig_v1_beta1__


class SignMode(betterproto.Enum):
    """
    SignMode represents a signing mode with its own security guarantees.
    This enum should be considered a registry of all known sign modes
    in the Cosmos ecosystem. Apps are not expected to support all known
    sign modes. Apps that would like to support custom  sign modes are
    encouraged to open a small PR against this file to add a new case
    to this SignMode enum describing their sign mode so that different
    apps have a consistent version of this enum.
    """

    SIGN_MODE_UNSPECIFIED = 0
    """
    SIGN_MODE_UNSPECIFIED specifies an unknown signing mode and will be
    rejected.
    """

    SIGN_MODE_DIRECT = 1
    """
    SIGN_MODE_DIRECT specifies a signing mode which uses SignDoc and is
    verified with raw bytes from Tx.
    """

    SIGN_MODE_TEXTUAL = 2
    """
    SIGN_MODE_TEXTUAL is a future signing mode that will verify some
    human-readable textual representation on top of the binary representation
    from SIGN_MODE_DIRECT.
    Since: cosmos-sdk 0.50
    """

    SIGN_MODE_DIRECT_AUX = 3
    """
    SIGN_MODE_DIRECT_AUX specifies a signing mode which uses
    SignDocDirectAux. As opposed to SIGN_MODE_DIRECT, this sign mode does not
    require signers signing over other signers' `signer_info`\\s.
    Since: cosmos-sdk 0.46
    """

    SIGN_MODE_LEGACY_AMINO_JSON = 127
    """
    SIGN_MODE_LEGACY_AMINO_JSON is a backwards compatibility mode which uses
    Amino JSON and will be removed in the future.
    """

    SIGN_MODE_EIP_191 = 191
    """
    SIGN_MODE_EIP_191 specifies the sign mode for EIP 191 signing on the Cosmos
    SDK. Ref: https://eips.ethereum.org/EIPS/eip-191
    Currently, SIGN_MODE_EIP_191 is registered as a SignMode enum variant,
    but is not implemented on the SDK by default. To enable EIP-191, you need
    to pass a custom `TxConfig` that has an implementation of
    `SignModeHandler` for EIP-191. The SDK may decide to fully support
    EIP-191 in the future.
    Since: cosmos-sdk 0.45.2
    """


@dataclass(eq=False, repr=False)
class SignatureDescriptors(betterproto.Message):
    """SignatureDescriptors wraps multiple SignatureDescriptor's."""

    signatures: List["SignatureDescriptor"] = betterproto.message_field(1)
    """signatures are the signature descriptors"""


@dataclass(eq=False, repr=False)
class SignatureDescriptor(betterproto.Message):
    """
    SignatureDescriptor is a convenience type which represents the full data for
    a signature including the public key of the signer, signing modes and the
    signature itself. It is primarily used for coordinating signatures between
    clients.
    """

    public_key: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)
    """public_key is the public key of the signer"""

    data: "SignatureDescriptorData" = betterproto.message_field(2)
    sequence: int = betterproto.uint64_field(3)
    """
    sequence is the sequence of the account, which describes the
    number of committed transactions signed by a given address. It is used to prevent
    replay attacks.
    """


@dataclass(eq=False, repr=False)
class SignatureDescriptorData(betterproto.Message):
    """Data represents signature data"""

    single: "SignatureDescriptorDataSingle" = betterproto.message_field(1, group="sum")
    """single represents a single signer"""

    multi: "SignatureDescriptorDataMulti" = betterproto.message_field(2, group="sum")
    """multi represents a multisig signer"""


@dataclass(eq=False, repr=False)
class SignatureDescriptorDataSingle(betterproto.Message):
    """Single is the signature data for a single signer"""

    mode: "SignMode" = betterproto.enum_field(1)
    """mode is the signing mode of the single signer"""

    signature: bytes = betterproto.bytes_field(2)
    """signature is the raw signature bytes"""


@dataclass(eq=False, repr=False)
class SignatureDescriptorDataMulti(betterproto.Message):
    """Multi is the signature data for a multisig public key"""

    bitarray: "___crypto_multisig_v1_beta1__.CompactBitArray" = (
        betterproto.message_field(1)
    )
    """bitarray specifies which keys within the multisig are signing"""

    signatures: List["SignatureDescriptorData"] = betterproto.message_field(2)
    """signatures is the signatures of the multi-signature"""
