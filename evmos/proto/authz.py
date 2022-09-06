from __future__ import annotations

from enum import Enum
from typing import Final

from betterproto import Message, Timestamp

from evmos.proto.autogen.py.cosmos.authz.v1beta1 import Grant, MsgGrant, MsgRevoke
from evmos.proto.autogen.py.cosmos.base.v1beta1 import Coin
from evmos.proto.autogen.py.cosmos.staking.v1beta1 import (
    AuthorizationType,
    StakeAuthorization,
)
from evmos.proto.utils import MessageGenerated, create_any_message

# authz.ts


def create_msg_grant(
    granter: str,
    grantee: str,
    grant_message: MessageGenerated[Message],
    seconds: int,
) -> MessageGenerated[MsgGrant]:
    """Create grant message."""
    msg = MsgGrant(
        granter=granter,
        grantee=grantee,
        grant=Grant(
            authorization=create_any_message(grant_message),
            expiration=Timestamp(seconds=seconds, nanos=0),
        ),
    )
    return MessageGenerated(
        message=msg,
        path='cosmos.authz.v1beta1.MsgGrant',
    )


class RevokeMessages(str, Enum):
    """Revoke message paths."""

    REVOKE_MSG_DELEGATE = '/cosmos.staking.v1beta1.MsgDelegate'
    """Revoke delegate message path."""
    REVOKE_MSG_WITHDRAW_DELEGATOR_REWARDS = (
        '/cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward'
    )
    """Revoke delegate and withdraw rewards message path."""


def create_msg_revoke(
    granter: str,
    grantee: str,
    type: str | RevokeMessages,  # noqa: A002
) -> MessageGenerated[MsgRevoke]:
    """Create revoke message."""
    msg = MsgRevoke(
        granter=granter,
        grantee=grantee,
        msg_type_url=type,
    )
    return MessageGenerated(
        message=msg,
        path='cosmos.authz.v1beta1.MsgRevoke',
    )


# stake.ts

StakeAuthTypes: Final = AuthorizationType
"""Alias for :class:`evmos.proto.autogen.py.cosmos.staking.v1beta1.AuthorizationType`"""


def create_stake_authorization(
    allow_address: str,
    denom: str,
    max_tokens: str | None,
    authorization_type: AuthorizationType,
) -> MessageGenerated[StakeAuthorization]:
    """Create staking authorization message."""
    msg = StakeAuthorization(
        allow_list=StakeAuthorization.Validators(address=[allow_address]),
        max_tokens=(
            Coin(denom=denom, amount=max_tokens)  # type: ignore[arg-type]
            if max_tokens
            else None
        ),
        authorization_type=authorization_type,
    )

    return MessageGenerated(
        message=msg,
        path='cosmos.staking.v1beta1.StakeAuthorization',
    )
