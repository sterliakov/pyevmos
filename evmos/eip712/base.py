from __future__ import annotations

from typing import Any, Sequence


def create_eip712(
    types: dict[str, Any], chain_id: int, message: dict[str, Any]
) -> dict[str, Any]:
    """Create `EIP712 <https://eips.ethereum.org/EIPS/eip-712>`_ data."""
    return {
        'types': types,
        'primaryType': 'Tx',
        'domain': {
            'name': 'Cosmos Web3',
            'version': '1.0.0',
            'chainId': chain_id,
            'verifyingContract': 'cosmos',
            'salt': '0',
        },
        'message': message,
    }


def generate_message_with_multiple_transactions(
    account_number: str,
    sequence: str,
    chain_cosmos_id: str,
    memo: str,
    fee: dict[str, Any],
    msgs: Sequence[dict[str, Any]],
) -> dict[str, Any]:
    """Create a message with multiple transactions included."""
    return {
        'accountNumber': account_number,
        'chainId': chain_cosmos_id,
        'fee': fee,
        'memo': memo,
        'msgs': msgs,
        'sequence': sequence,
    }


def generate_message(
    account_number: str,
    sequence: str,
    chain_cosmos_id: str,
    memo: str,
    fee: dict[str, Any],
    msg: dict[str, Any],
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
        'EIP712Domain': [
            {'name': 'name', 'type': 'string'},
            {'name': 'version', 'type': 'string'},
            {'name': 'chainId', 'type': 'uint256'},
            {'name': 'verifyingContract', 'type': 'string'},
            {'name': 'salt', 'type': 'string'},
        ],
        'Tx': [
            {'name': 'accountNumber', 'type': 'string'},
            {'name': 'chainId', 'type': 'string'},
            {'name': 'fee', 'type': 'Fee'},
            {'name': 'memo', 'type': 'string'},
            {'name': 'msgs', 'type': 'Msg[]'},
            {'name': 'sequence', 'type': 'string'},
        ],
        'Fee': [
            {'name': 'feePayer', 'type': 'string'},
            {'name': 'amount', 'type': 'Coin[]'},
            {'name': 'gas', 'type': 'string'},
        ],
        'Coin': [
            {'name': 'denom', 'type': 'string'},
            {'name': 'amount', 'type': 'string'},
        ],
        'Msg': [
            {'name': 'type', 'type': 'string'},
            {'name': 'value', 'type': 'MsgValue'},
        ],
    }
    types.update(msg_values)
    return types


def generate_fee(amount: str, denom: str, gas: str, fee_payer: str) -> dict[str, Any]:
    """Generate fee definition structure."""
    return {
        'amount': [
            {
                'amount': amount,
                'denom': denom,
            },
        ],
        'gas': gas,
        'feePayer': fee_payer,
    }
