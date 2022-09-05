from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Literal, Mapping, overload

import requests
from typing_extensions import Concatenate, ParamSpec

from evmos.eip712 import (
    EIPToSign,
    create_eip712,
    generate_fee,
    generate_message,
    generate_types,
)
from evmos.proto import MessageGenerated, create_transaction
from evmos.proto.transactions import TxGeneratedBase as TxGeneratedBase


@dataclass
class Fee:
    """Fee for message."""

    amount: str
    denom: str
    gas: str


@dataclass
class Sender:
    """Message sender."""

    account_address: str
    sequence: int = 0
    account_number: int = 0
    pubkey: str = ''

    def update_from_chain(self, url: str = 'http://127.0.0.1:1317') -> None:
        """Set `sequence`, `account_number` and possibly `pubkey` from API response."""
        response = requests.get(
            f'{url}/cosmos/auth/v1beta1/accounts/{self.account_address}'
        )
        resp = response.json()

        self.sequence = int(resp['account']['base_account']['sequence'])
        self.account_number = int(resp['account']['base_account']['account_number'])
        if not self.pubkey:
            self.pubkey = resp['account']['base_account']['pub_key']['key']


@dataclass
class Chain:
    """Chain definition."""

    chain_id: int
    cosmos_chain_id: str


@dataclass
class TxGenerated(TxGeneratedBase):
    """Transaction generated by this library (with EIP to sign)."""

    eip_to_sign: EIPToSign


_P = ParamSpec('_P')


def to_generated_base(
    func: Callable[Concatenate[str, _P], MessageGenerated[Any]]
) -> Callable[Concatenate[Chain, Sender, Fee, str, _P], TxGeneratedBase]:
    """Wrap function returning message with transaction base."""
    # Not using functools.wraps, because signature is altered

    def inner(
        chain: Chain,
        sender: Sender,
        fee: Fee,
        memo: str,
        *args: _P.args,
        **kwargs: _P.kwargs,
    ) -> TxGeneratedBase:
        msg_cosmos = func(sender.account_address, *args, **kwargs)

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
            sign_direct=tx.sign_direct,
            legacy_amino=tx.legacy_amino,
        )

    inner.__doc__ = func.__doc__
    inner.__name__ = func.__name__
    return inner


@overload
def to_generated(
    types_def: dict[str, Any], proto: Literal[True]
) -> Callable[
    [Callable[Concatenate[str, _P], tuple[Mapping[str, Any], MessageGenerated[Any]]]],
    Callable[Concatenate[Chain, Sender, Fee, str, _P], TxGenerated],
]:
    ...


@overload
def to_generated(
    types_def: dict[str, Any], proto: Literal[False] = ...
) -> Callable[
    [Callable[_P, tuple[Mapping[str, Any], MessageGenerated[Any]]]],
    Callable[Concatenate[Chain, Sender, Fee, str, _P], TxGenerated],
]:
    ...


def to_generated(
    types_def: dict[str, Any], proto: bool = False
) -> Callable[
    [Callable[_P, tuple[Mapping[str, Any], MessageGenerated[Any]]]],
    Callable[Concatenate[Chain, Sender, Fee, str, _P], TxGenerated],
] | Callable[
    [Callable[Concatenate[str, _P], tuple[Mapping[str, Any], MessageGenerated[Any]]]],
    Callable[Concatenate[Chain, Sender, Fee, str, _P], TxGenerated],
]:
    """Wrap function returning message with transaction."""

    def _inner(
        chain: Chain,
        sender: Sender,
        fee: Fee,
        memo: str,
        msg: Mapping[str, Any],
        msg_cosmos: MessageGenerated[Any],
    ) -> TxGenerated:
        # EIP712
        fee_object = generate_fee(
            fee.amount,
            fee.denom,
            fee.gas,
            sender.account_address,
        )
        types = generate_types(types_def)

        messages = generate_message(
            str(sender.account_number),
            str(sender.sequence),
            chain.cosmos_chain_id,
            memo,
            fee_object,
            msg,
        )
        eip_to_sign = create_eip712(types, chain.chain_id, messages)

        # Cosmos

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

        return TxGenerated(
            sign_direct=tx.sign_direct,
            legacy_amino=tx.legacy_amino,
            eip_to_sign=eip_to_sign,
        )

    if proto:

        def decorator(
            func: Callable[
                Concatenate[str, _P], tuple[Mapping[str, Any], MessageGenerated[Any]]
            ]
        ) -> Callable[Concatenate[Chain, Sender, Fee, str, _P], TxGenerated]:
            def inner(
                chain: Chain,
                sender: Sender,
                fee: Fee,
                memo: str,
                *args: _P.args,
                **kwargs: _P.kwargs,
            ) -> TxGenerated:
                msg, msg_cosmos = func(sender.account_address, *args, **kwargs)
                return _inner(chain, sender, fee, memo, msg, msg_cosmos)

            inner.__doc__ = func.__doc__
            inner.__name__ = func.__name__
            return inner

        return decorator

    else:

        def decorator2(
            func: Callable[_P, tuple[Mapping[str, Any], MessageGenerated[Any]]]
        ) -> Callable[Concatenate[Chain, Sender, Fee, str, _P], TxGenerated]:
            def inner(
                chain: Chain,
                sender: Sender,
                fee: Fee,
                memo: str,
                *args: _P.args,
                **kwargs: _P.kwargs,
            ) -> TxGenerated:
                msg, msg_cosmos = func(*args, **kwargs)
                return _inner(chain, sender, fee, memo, msg, msg_cosmos)

            inner.__doc__ = func.__doc__
            inner.__name__ = func.__name__
            return inner

        return decorator2
