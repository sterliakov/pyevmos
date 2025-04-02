from __future__ import annotations

import pytest


@pytest.fixture
def pubkey() -> bytes:
    return bytes.fromhex(
        "0a210288b1f531b87871dbc037295187255cae4ba0c4bc37ca726105b2140afd0e6917"
    )
