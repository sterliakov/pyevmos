# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/applications/interchain_accounts/v1/account.proto, ibc/applications/interchain_accounts/v1/genesis.proto, ibc/applications/interchain_accounts/v1/metadata.proto, ibc/applications/interchain_accounts/v1/packet.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from typing import List

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf

from .....cosmos.auth import v1beta1 as ____cosmos_auth_v1_beta1__
from ..controller import v1 as _controller_v1__
from ..host import v1 as _host_v1__


class Type(betterproto.Enum):
    """
    Type defines a classification of message issued from a controller chain to
    its associated interchain accounts host
    """

    TYPE_UNSPECIFIED = 0
    """Default zero value enumeration"""

    TYPE_EXECUTE_TX = 1
    """Execute a transaction on an interchain accounts host chain"""


@dataclass(eq=False, repr=False)
class Metadata(betterproto.Message):
    """
    Metadata defines a set of protocol specific data encoded into the ICS27
    channel version bytestring See ICS004:
    https://github.com/cosmos/ibc/tree/main/spec/core/ics-004-channel-and-packet-semantics
    """

    version: str = betterproto.string_field(1)
    """version defines the ICS27 protocol version"""

    controller_connection_id: str = betterproto.string_field(2)
    """
    controller_connection_id is the connection identifier associated with the
    controller chain
    """

    host_connection_id: str = betterproto.string_field(3)
    """
    host_connection_id is the connection identifier associated with the host
    chain
    """

    address: str = betterproto.string_field(4)
    """
    address defines the interchain account address to be fulfilled upon the
    OnChanOpenTry handshake step NOTE: the address field is empty on the
    OnChanOpenInit handshake step
    """

    encoding: str = betterproto.string_field(5)
    """encoding defines the supported codec format"""

    tx_type: str = betterproto.string_field(6)
    """
    tx_type defines the type of transactions the interchain account can execute
    """


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the interchain accounts genesis state"""

    controller_genesis_state: 'ControllerGenesisState' = betterproto.message_field(1)
    host_genesis_state: 'HostGenesisState' = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ControllerGenesisState(betterproto.Message):
    """
    ControllerGenesisState defines the interchain accounts controller genesis
    state
    """

    active_channels: List['ActiveChannel'] = betterproto.message_field(1)
    interchain_accounts: List[
        'RegisteredInterchainAccount'
    ] = betterproto.message_field(2)
    ports: List[str] = betterproto.string_field(3)
    params: '_controller_v1__.Params' = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class HostGenesisState(betterproto.Message):
    """HostGenesisState defines the interchain accounts host genesis state"""

    active_channels: List['ActiveChannel'] = betterproto.message_field(1)
    interchain_accounts: List[
        'RegisteredInterchainAccount'
    ] = betterproto.message_field(2)
    port: str = betterproto.string_field(3)
    params: '_host_v1__.Params' = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ActiveChannel(betterproto.Message):
    """
    ActiveChannel contains a connection ID, port ID and associated active channel
    ID
    """

    connection_id: str = betterproto.string_field(1)
    port_id: str = betterproto.string_field(2)
    channel_id: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class RegisteredInterchainAccount(betterproto.Message):
    """
    RegisteredInterchainAccount contains a connection ID, port ID and associated
    interchain account address
    """

    connection_id: str = betterproto.string_field(1)
    port_id: str = betterproto.string_field(2)
    account_address: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class InterchainAccountPacketData(betterproto.Message):
    """
    InterchainAccountPacketData is comprised of a raw transaction, type of
    transaction and optional memo field.
    """

    type: 'Type' = betterproto.enum_field(1)
    data: bytes = betterproto.bytes_field(2)
    memo: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CosmosTx(betterproto.Message):
    """
    CosmosTx contains a list of sdk.Msg's. It should be used when sending
    transactions to an SDK host chain.
    """

    messages: List['betterproto_lib_google_protobuf.Any'] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class InterchainAccount(betterproto.Message):
    """
    An InterchainAccount is defined as a BaseAccount & the address of the account
    owner on the controller chain
    """

    base_account: '____cosmos_auth_v1_beta1__.BaseAccount' = betterproto.message_field(
        1
    )
    account_owner: str = betterproto.string_field(2)
