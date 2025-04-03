from __future__ import annotations

import pytest

from evmos.eip712.encoding.utils import parse_chain_id

FAIL_MSG = r"Invalid chain_id received: .+"


def test_parses_standard_chain_ids():
    id_ = "evmos_9000-1"
    assert parse_chain_id(id_) == 9000


def test_throws_on_invalid_case_1():
    id_ = "evmos_9000"
    with pytest.raises(ValueError, match=FAIL_MSG):
        parse_chain_id(id_)


def test_throws_on_invalid_case_2():
    id_ = "evmos9000"
    with pytest.raises(ValueError, match=FAIL_MSG):
        parse_chain_id(id_)


def test_throws_on_invalid_case_3():
    id_ = "evmos_9000-1evmos_9000-1"
    with pytest.raises(ValueError, match=FAIL_MSG):
        parse_chain_id(id_)
