from __future__ import annotations

from evmos.proto import (
    MessageGenerated,
    MsgGrant,
    MsgRevoke,
    RevokeMessages,
    StakeAuthTypes,
    create_msg_grant,
    create_msg_revoke,
    create_stake_authorization,
)
from evmos.transactions.common import to_generated_base


@to_generated_base
def create_tx_msg_stake_authorization(
    account_address: str,
    bot_address: str,
    validator_address: str,
    denom: str,
    duration_in_seconds: int,
    max_tokens: str | None = None,
) -> MessageGenerated[MsgGrant]:
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
    return create_msg_grant(
        account_address,
        bot_address,
        msg_stake_grant,
        duration_in_seconds,
    )


@to_generated_base
def create_tx_msg_stake_revoke_authorization(
    account_address: str,
    bot_address: str,
) -> MessageGenerated[MsgRevoke]:
    """Create a transaction with message for stake authorization revoke."""
    # EIP712
    # This is blocked until EvmosV7 is released with the eip712 any messages fixes!

    # Cosmos
    return create_msg_revoke(
        account_address,
        bot_address,
        RevokeMessages.REVOKE_MSG_DELEGATE,
    )
