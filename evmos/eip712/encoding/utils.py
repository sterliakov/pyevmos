from __future__ import annotations

import re


def parse_chain_id(chain_id: str) -> int:
    """Parse Chain ID string into number. Throws error on failure case."""
    res = re.match(r"^([a-z]+)_(?P<target>[1-9]\d*)-([1-9]\d*)$", chain_id)
    if res is None:
        raise ValueError(f"Invalid chain_id received: {chain_id}")

    return int(res.group("target"))
