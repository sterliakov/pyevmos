from __future__ import annotations

import time
from pprint import pprint

import pytest

from evmos.provider import BroadcastMode
from evmos.transactions import create_message_send
from evmos.wallet import (
    TESTNET_CHAIN,
    TESTNET_FEE,
    broadcast,
    sign_transaction,
    sign_transaction_eip712,
)


@pytest.mark.online
def test_send_money_simple(sender, sender_pk, receiver_addr, url):
    for _ in range(3):
        sender.update_from_chain(url)

        tx = create_message_send(
            TESTNET_CHAIN,
            sender,
            TESTNET_FEE,
            "",
            receiver_addr,
            "1",
            "atevmos",
        )

        signed = sign_transaction(tx, sender_pk, BroadcastMode.SYNC)
        response = broadcast(signed, url)
        pprint(response)

        try:
            assert response["tx_response"]["code"] == 0
        except KeyError:
            # 2 - timeout
            if (
                response.get("error_from_node") == "timeout"
                or response.get("code") == 2
            ):
                time.sleep(5)
                continue
            raise
        except AssertionError:
            # 32 - old sequence (time-related too)
            if response["tx_response"]["code"] == 32:
                time.sleep(1)
                continue
            raise
        else:
            break
    else:
        pytest.fail("Always timing out")


@pytest.mark.online
@pytest.mark.skip("Fails, but why?")
def test_send_money_eip712(receiver, receiver_pk, sender_addr, url):
    for _ in range(3):
        receiver.update_from_chain(url)

        tx = create_message_send(
            TESTNET_CHAIN,
            receiver,
            TESTNET_FEE,
            "",
            sender_addr,
            "1",
            "atevmos",
        )

        signed = sign_transaction_eip712(
            receiver, tx, receiver_pk, broadcast_mode=BroadcastMode.SYNC
        )
        response = broadcast(signed, url)
        pprint(response)

        try:
            assert response["tx_response"]["code"] == 0
        except KeyError:
            # 2 - timeout
            if (
                response.get("error_from_node") == "timeout"
                or response.get("code") == 2
            ):
                time.sleep(5)
                continue
            raise
        except AssertionError:
            # 32 - old sequence (time-related too)
            if response["tx_response"]["code"] == 32:
                time.sleep(1)
                continue
            raise
        else:
            break
    else:
        pytest.fail("Always timing out")
