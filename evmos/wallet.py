from __future__ import annotations

import base64
from typing import Any, Final

import requests
from eth_account import Account
from eth_typing import HexStr
from eth_utils import keccak

from evmos.proto import create_tx_raw
from evmos.provider import BroadcastMode, BroadcastPostBody, generate_endpoint_broadcast
from evmos.transactions import (
    Chain,
    Fee,
    Sender,
    TxGenerated,
    create_tx_raw_eip712,
    signature_to_web3_extension,
)

# Copied from
# https://github.com/hanchon-live/evmos-ts-wallet/blob/main/src/signer.ts
# with major modifications.


# Chain helpers

LOCALNET_CHAIN: Final = Chain(
    chain_id=9000,
    cosmos_chain_id="evmos_9000-1",
)

LOCALNET_FEE: Final = Fee(
    amount="2000000000000",
    denom="atevmos",
    gas="200000",
)

MAINNET_CHAIN: Final = Chain(
    chain_id=9001,
    cosmos_chain_id="evmos_9001-2",
)

MAINNET_FEE: Final = Fee(
    amount="6000000000000",
    denom="atevmos",
    gas="600000",
)

TESTNET_CHAIN: Final = Chain(
    chain_id=9000,
    cosmos_chain_id="evmos_9000-4",
)

TESTNET_FEE: Final = Fee(
    amount="15000000000000000",
    denom="atevmos",
    gas="600000",
)


def broadcast(
    transaction_body: BroadcastPostBody,
    url: str = "http://127.0.0.1:1317",
    timeout: int | None = 5,
) -> dict[str, Any]:
    """Broadcast a transaction.

    Args:
        transaction_body: data to broadcast, json payload (not stringified).
        url: REST API URL to use.
        timeout: HTTP timeout, pass `None` to disable.

    Returns:
        Info about broadcasted transaction or failure reasons.
    """
    post = requests.post(
        f"{url}{generate_endpoint_broadcast()}", json=transaction_body, timeout=timeout
    )
    return post.json()  # type: ignore[no-any-return]


# FIXME: broadcast_mode belongs to ``broadcast``, not here
def sign_transaction(
    tx: TxGenerated,
    private_key: HexStr,
    broadcast_mode: BroadcastMode = BroadcastMode.BLOCK,
) -> BroadcastPostBody:
    """Sign transaction using payload method (keplr style)."""
    data_to_sign = base64.b64decode(tx.sign_direct.sign_bytes)

    signature_raw = Account.unsafe_sign_hash(data_to_sign, private_key=private_key)

    signed_tx = create_tx_raw(
        bytes(tx.sign_direct.body),
        bytes(tx.sign_direct.auth_info),
        [signature_raw.signature],
    )
    return {
        "tx_bytes": base64.b64encode(bytes(signed_tx.message)).decode(),
        "mode": broadcast_mode,
    }


def sign_transaction_eip712(
    sender: Sender,
    tx: TxGenerated,
    private_key: HexStr,
    chain: Chain = TESTNET_CHAIN,
    broadcast_mode: BroadcastMode = BroadcastMode.BLOCK,
) -> BroadcastPostBody:
    """Sign transaction using eip712 method (metamask style)."""
    hashes = tx.eip_to_sign.hash()
    data_to_sign = keccak(b"\x19\x01" + hashes["domain"] + hashes["message"])

    signature_raw = Account.unsafe_sign_hash(data_to_sign, private_key=private_key)
    extension = signature_to_web3_extension(
        chain,
        sender,
        signature_raw.signature,
    )
    signed_tx = create_tx_raw_eip712(
        tx.legacy_amino.body,
        tx.legacy_amino.auth_info,
        extension,
    )

    return {
        "tx_bytes": base64.b64encode(bytes(signed_tx.message)).decode(),
        "mode": broadcast_mode,
    }
