from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, Final, Generic, TypeVar

import bech32
from eth_typing import HexStr
from eth_utils import keccak

from evmos.utils.polyfill import removeprefix

ADDRESS_REGEX: Final = re.compile(r'^0x[0-9a-fA-F]{40}$')


def to_checksum_address(address: HexStr, chain_id: int | None = None) -> HexStr:
    """Convert address to checksum address."""
    strip_address = removeprefix(address, '0x').lower()
    prefix = (str(chain_id) + '0x') if chain_id is not None else ''
    keccak_hash = keccak((prefix + strip_address).encode()).hex()
    output = '0x' + ''.join(
        byte.upper() if int(hash_byte, 16) >= 8 else byte
        for byte, hash_byte in zip(strip_address, keccak_hash)
    )
    return HexStr(output)


def is_valid_address(address: HexStr) -> bool:
    """Check if address is in a proper format."""
    return bool(ADDRESS_REGEX.match(address))


def is_valid_checksum_address(address: HexStr, chain_id: int | None = None) -> bool:
    """Check if checksum address is valid."""
    return bool(
        is_valid_address(address)
        and (to_checksum_address(address, chain_id) == address)
    )


_T = TypeVar('_T')


@dataclass
class ChainConverter(Generic[_T]):
    """Chain decoder-encoder pair."""

    decoder: Callable[[_T], bytes]
    """Address decoder for given chain."""
    encoder: Callable[[bytes], _T]
    """Address encoder for given chain."""
    name: str
    """Chain name."""


def make_checksummed_hex_decoder(
    chain_id: int | None = None,
) -> Callable[[HexStr], bytes]:
    """Make decoder for hex-based address."""

    def decoder(data: HexStr) -> bytes:
        """Address decoder."""
        stripped = removeprefix(data, '0x')
        if (
            not is_valid_checksum_address(data, chain_id)
            and stripped != stripped.lower()
            and stripped != stripped.upper()
        ):
            raise ValueError('Invalid address checksum.')
        return bytes.fromhex(stripped)

    return decoder


def make_checksummed_hex_encoder(
    chain_id: int | None = None,
) -> Callable[[bytes], HexStr]:
    """Make encoder for hex-based address."""

    def encoder(data: bytes) -> HexStr:
        """Address encoder."""
        return to_checksum_address(HexStr(data.hex()), chain_id)

    return encoder


def hex_checksum_chain(
    name: str, chain_id: int | None = None
) -> ChainConverter[HexStr]:
    """Chain with hex address."""
    return ChainConverter(
        decoder=make_checksummed_hex_decoder(chain_id),
        encoder=make_checksummed_hex_encoder(chain_id),
        name=name,
    )


ETH: Final = hex_checksum_chain('ETH')
"""Eth chain address converter."""


def make_bech32_decoder(current_prefix: str) -> Callable[[str], bytes]:
    """Make decoder for bech32-based address."""

    def decoder(data: str) -> bytes:
        """Address decoder."""
        prefix, words = bech32.bech32_decode(data)
        if prefix != current_prefix:
            raise ValueError('Unrecognised address format')

        decoded = bech32.convertbits(words, 5, 8, False)
        if decoded is None or len(decoded) < 2 or len(decoded) > 40:
            raise ValueError('Unrecognised address format')
        return bytes(decoded)

    return decoder


def make_bech32_encoder(prefix: str) -> Callable[[bytes], str]:
    """Make encoder for bech32-based address."""

    def encoder(data: bytes) -> str:
        """Address encoder."""
        return bech32.bech32_encode(prefix, bech32.convertbits(data, 8, 5))

    return encoder


def bech32_chain(name: str, prefix: str) -> ChainConverter[str]:
    """Chain with bech32 address."""
    return ChainConverter(
        decoder=make_bech32_decoder(prefix),
        encoder=make_bech32_encoder(prefix),
        name=name,
    )


ETHERMINT: Final = bech32_chain('ETHERMINT', 'ethm')
"""Ethermint chain address converter."""


def eth_to_ethermint(eth_address: HexStr) -> str:
    """Eth -> Ethermint address conversion."""
    data = ETH.decoder(eth_address)
    return ETHERMINT.encoder(data)


def ethermint_to_eth(ethermint_address: str) -> HexStr:
    """Ethermint -> Eth address conversion."""
    data = ETHERMINT.decoder(ethermint_address)
    return ETH.encoder(data)


EVMOS: Final = bech32_chain('EVMOS', 'evmos')
"""Evmos chain address converter."""


def eth_to_evmos(eth_address: HexStr) -> str:
    """Eth -> Evmos address conversion."""
    data = ETH.decoder(eth_address)
    return EVMOS.encoder(data)


def evmos_to_eth(evmos_address: str) -> HexStr:
    """Evmos -> Eth address conversion."""
    data = EVMOS.decoder(evmos_address)
    return ETH.encoder(data)


OSMOSIS: Final = bech32_chain('OSMOSIS', 'osmo')
"""Osmosis chain address converter."""


def eth_to_osmosis(eth_address: HexStr) -> str:
    """Eth -> Osmosis address conversion."""
    data = ETH.decoder(eth_address)
    return OSMOSIS.encoder(data)


def osmosis_to_eth(evmos_address: str) -> HexStr:
    """Osmosis -> Eth address conversion."""
    data = OSMOSIS.decoder(evmos_address)
    return ETH.encoder(data)


COSMOS: Final = bech32_chain('COSMOS', 'cosmos')
"""Cosmos chain address converter."""


def eth_to_cosmos(eth_address: HexStr) -> str:
    """Eth -> Cosmos address conversion."""
    data = ETH.decoder(eth_address)
    return COSMOS.encoder(data)


def cosmos_to_eth(evmos_address: str) -> HexStr:
    """Cosmos -> Eth address conversion."""
    data = COSMOS.decoder(evmos_address)
    return ETH.encoder(data)


KYVE: Final = bech32_chain('KORELLIA', 'kyve')
"""Kyve chain address converter."""


def eth_to_kyve(eth_address: HexStr) -> str:
    """Eth -> Kyve address conversion."""
    data = ETH.decoder(eth_address)
    return KYVE.encoder(data)


def kyve_to_eth(kyve_address: str) -> HexStr:
    """Kyve -> Eth address conversion."""
    data = KYVE.decoder(kyve_address)
    return ETH.encoder(data)
