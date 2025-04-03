#!/bin/bash

set -euo pipefail

ETHERMINT_TAG=v0.19.3
EVMOS_TAG=v8.2.3

cd evmos/proto
protos_root="$(pwd)/autogen"
mkdir -p "$protos_root/proto"
rm -rf "$protos_root/proto"/*

# Ethermint
temp=$(mktemp -d)
cd "$temp"
git clone https://github.com/evmos/ethermint/
cd ethermint/
git checkout "tags/$ETHERMINT_TAG"
cp -r ./proto/* "$protos_root/proto"
cp -r ./third_party/proto/* "$protos_root/proto"
cd "$temp"
rm -rf ethermint

# Evmos
git clone https://github.com/evmos/evmos/
cd evmos/
git checkout "tags/$EVMOS_TAG"
cp -r ./proto/* "$protos_root/proto"
cp -r ./third_party/proto/* "$protos_root/proto"
cd "$temp"
rm -rf evmos

cd ~
rm -r "$temp"
