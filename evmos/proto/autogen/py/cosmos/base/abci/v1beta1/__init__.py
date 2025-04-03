# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/base/abci/v1beta1/abci.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf

from .....tendermint import abci as ____tendermint_abci__


@dataclass(eq=False, repr=False)
class TxResponse(betterproto.Message):
    """
    TxResponse defines a structure containing relevant tx data and metadata. The
    tags are stringified and the log is JSON decoded.
    """

    height: int = betterproto.int64_field(1)
    """The block height"""

    txhash: str = betterproto.string_field(2)
    """The transaction hash."""

    codespace: str = betterproto.string_field(3)
    """Namespace for the Code"""

    code: int = betterproto.uint32_field(4)
    """Response code."""

    data: str = betterproto.string_field(5)
    """Result bytes, if any."""

    raw_log: str = betterproto.string_field(6)
    """
    The output of the application's logger (raw string). May be
    non-deterministic.
    """

    logs: List["AbciMessageLog"] = betterproto.message_field(7)
    """The output of the application's logger (typed). May be non-deterministic."""

    info: str = betterproto.string_field(8)
    """Additional information. May be non-deterministic."""

    gas_wanted: int = betterproto.int64_field(9)
    """Amount of gas requested for transaction."""

    gas_used: int = betterproto.int64_field(10)
    """Amount of gas consumed by transaction."""

    tx: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(11)
    """The request transaction bytes."""

    timestamp: str = betterproto.string_field(12)
    """
    Time of the previous block. For heights > 1, it's the weighted median of
    the timestamps of the valid votes in the block.LastCommit. For height == 1,
    it's genesis time.
    """

    events: List["____tendermint_abci__.Event"] = betterproto.message_field(13)
    """
    Events defines all the events emitted by processing a transaction. Note,
    these events include those emitted by processing all the messages and those
    emitted from the ante handler. Whereas Logs contains the events, with
    additional metadata, emitted only by processing the messages.
    Since: cosmos-sdk 0.42.11, 0.44.5, 0.45
    """


@dataclass(eq=False, repr=False)
class AbciMessageLog(betterproto.Message):
    """ABCIMessageLog defines a structure containing an indexed tx ABCI message log."""

    msg_index: int = betterproto.uint32_field(1)
    log: str = betterproto.string_field(2)
    events: List["StringEvent"] = betterproto.message_field(3)
    """
    Events contains a slice of Event objects that were emitted during some
    execution.
    """


@dataclass(eq=False, repr=False)
class StringEvent(betterproto.Message):
    """
    StringEvent defines en Event object wrapper where all the attributes
    contain key/value pairs that are strings instead of raw bytes.
    """

    type: str = betterproto.string_field(1)
    attributes: List["Attribute"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Attribute(betterproto.Message):
    """
    Attribute defines an attribute wrapper where the key and value are
    strings instead of raw bytes.
    """

    key: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GasInfo(betterproto.Message):
    """GasInfo defines tx execution gas context."""

    gas_wanted: int = betterproto.uint64_field(1)
    """GasWanted is the maximum units of work we allow this tx to perform."""

    gas_used: int = betterproto.uint64_field(2)
    """GasUsed is the amount of gas actually consumed."""


@dataclass(eq=False, repr=False)
class Result(betterproto.Message):
    """Result is the union of ResponseFormat and ResponseCheckTx."""

    data: bytes = betterproto.bytes_field(1)
    """
    Data is any data returned from message or handler execution. It MUST be
    length prefixed in order to separate data from multiple message executions.
    """

    log: str = betterproto.string_field(2)
    """Log contains the log information from message or handler execution."""

    events: List["____tendermint_abci__.Event"] = betterproto.message_field(3)
    """
    Events contains a slice of Event objects that were emitted during message
    or handler execution.
    """


@dataclass(eq=False, repr=False)
class SimulationResponse(betterproto.Message):
    """
    SimulationResponse defines the response generated when a transaction is
    successfully simulated.
    """

    gas_info: "GasInfo" = betterproto.message_field(1)
    result: "Result" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MsgData(betterproto.Message):
    """
    MsgData defines the data returned in a Result object during message
    execution.
    """

    msg_type: str = betterproto.string_field(1)
    data: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class TxMsgData(betterproto.Message):
    """
    TxMsgData defines a list of MsgData. A transaction will have a MsgData object
    for each message.
    """

    data: List["MsgData"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SearchTxsResult(betterproto.Message):
    """SearchTxsResult defines a structure for querying txs pageable"""

    total_count: int = betterproto.uint64_field(1)
    """Count of all txs"""

    count: int = betterproto.uint64_field(2)
    """Count of txs in current page"""

    page_number: int = betterproto.uint64_field(3)
    """Index of current page, start from 1"""

    page_total: int = betterproto.uint64_field(4)
    """Count of total pages"""

    limit: int = betterproto.uint64_field(5)
    """Max count txs per page"""

    txs: List["TxResponse"] = betterproto.message_field(6)
    """List of txs in current page"""
