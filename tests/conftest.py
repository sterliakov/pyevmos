from __future__ import annotations

import os

import dotenv
import pytest

from evmos.transactions import Sender

dotenv.load_dotenv()


@pytest.fixture()
def url():
    return os.getenv('EVMOS_REST_API_URL', 'https://rest.evmos-testnet.lava.build')


@pytest.fixture()
def sender_addr():
    return os.getenv('SENDER_ADDRESS')


@pytest.fixture()
def sender_pub():
    return os.getenv('SENDER_PUBKEY')


@pytest.fixture()
def sender(sender_addr, sender_pub) -> Sender:
    return Sender(sender_addr, 0, 0, sender_pub)


@pytest.fixture()
def sender_pk():
    return os.getenv('SENDER_PRIVKEY')


@pytest.fixture()
def receiver_addr():
    return os.getenv('RECEIVER_ADDRESS')


@pytest.fixture()
def receiver_pub():
    return os.getenv('RECEIVER_PUBKEY')


@pytest.fixture()
def receiver(receiver_addr, receiver_pub) -> Sender:
    return Sender(receiver_addr, 0, 0, receiver_pub)


@pytest.fixture()
def receiver_pk():
    return os.getenv('RECEIVER_PRIVKEY')
