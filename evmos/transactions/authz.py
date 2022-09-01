from __future__ import annotations

from evmos.proto import (
    RevokeMessages,
    StakeAuthTypes,
    create_msg_grant,
    create_msg_revoke,
    create_stake_authorization,
    create_transaction,
)
from evmos.transactions.common import Chain, Fee, Sender, TxGeneratedBase


def create_tx_msg_stake_authorization(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    bot_address: str,
    validator_address: str,
    denom: str,
    duration_in_seconds: int,
    max_tokens: str | None = None,
) -> TxGeneratedBase:
    """Create a transaction with message for stake authorization."""
    # EIP712
    # This is blocked until EvmosV7 is released with the eip712 any messages fixes!

    # Cosmos
    msg_stake_grant = create_stake_authorization(
        validator_address,
        denom,
        max_tokens,
        StakeAuthTypes.AUTHORIZATION_TYPE_DELEGATE,  # type: ignore
    )
    msg_cosmos = create_msg_grant(
        sender.account_address,
        bot_address,
        msg_stake_grant,
        duration_in_seconds,
    )
    tx = create_transaction(
        msg_cosmos,
        memo,
        fee.amount,
        fee.denom,
        int(fee.gas),
        'ethsecp256',
        sender.pubkey,
        sender.sequence,
        sender.account_number,
        chain.cosmos_chain_id,
    )

    return TxGeneratedBase(
        sign_direct=tx['signDirect'],
        legacy_amino=tx['legacyAmino'],
    )


def create_tx_msg_stake_revoke_authorization(
    chain: Chain,
    sender: Sender,
    fee: Fee,
    memo: str,
    bot_address: str,
) -> TxGeneratedBase:
    """Create a transaction with message for stake authorization revoke."""
    # EIP712
    # This is blocked until EvmosV7 is released with the eip712 any messages fixes!

    # Cosmos
    msg_cosmos = create_msg_revoke(
        sender.account_address,
        bot_address,
        RevokeMessages.REVOKE_MSG_DELEGATE,
    )
    tx = create_transaction(
        msg_cosmos,
        memo,
        fee.amount,
        fee.denom,
        int(fee.gas),
        'ethsecp256',
        sender.pubkey,
        sender.sequence,
        sender.account_number,
        chain.cosmos_chain_id,
    )

    return TxGeneratedBase(
        sign_direct=tx['signDirect'],
        legacy_amino=tx['legacyAmino'],
    )
