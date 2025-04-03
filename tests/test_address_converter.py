from __future__ import annotations

from evmos.address_converter import (
    ETH,
    ETHERMINT,
    eth_to_ethermint,
    eth_to_evmos,
    ethermint_to_eth,
    evmos_to_eth,
)


def test_decoders():
    # ETH
    hex_data = ETH.decoder("0xe2D61e49ff8a9d724CC54d338D8076F878aC6b71")
    assert hex_data.hex() == "e2d61e49ff8a9d724cc54d338d8076f878ac6b71"
    # ETHERMINT
    hex_data = ETHERMINT.decoder("ethm1uttpuj0l32whynx9f5ecmqrklpu2c6m3973048")
    assert hex_data.hex() == "e2d61e49ff8a9d724cc54d338d8076f878ac6b71"


def test_encoders():
    # ETH
    address = ETH.encoder(
        bytes.fromhex("e2d61e49ff8a9d724cc54d338d8076f878ac6b71"),
    )
    assert address == "0xe2D61e49ff8a9d724CC54d338D8076F878aC6b71"
    # ETHERMINT
    address = ETHERMINT.encoder(
        bytes.fromhex("e2d61e49ff8a9d724cc54d338d8076f878ac6b71"),
    )
    assert address == "ethm1uttpuj0l32whynx9f5ecmqrklpu2c6m3973048"


def test_converters():
    # ETH
    address = eth_to_ethermint("0xe2D61e49ff8a9d724CC54d338D8076F878aC6b71")
    assert address == "ethm1uttpuj0l32whynx9f5ecmqrklpu2c6m3973048"

    # ETHERMINT
    address = ethermint_to_eth("ethm1uttpuj0l32whynx9f5ecmqrklpu2c6m3973048")
    assert address == "0xe2D61e49ff8a9d724CC54d338D8076F878aC6b71"

    # EVMOS
    address = evmos_to_eth("evmos1z3t55m0l9h0eupuz3dp5t5cypyv674jj7mz2jw")
    assert address == "0x14574a6DFF2Ddf9e07828b4345d3040919AF5652"
    # ETH to EVMOS
    address = eth_to_evmos("0x14574a6DFF2Ddf9e07828b4345d3040919AF5652")
    assert address == "evmos1z3t55m0l9h0eupuz3dp5t5cypyv674jj7mz2jw"
