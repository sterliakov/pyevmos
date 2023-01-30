#!/bin/bash

set -euo pipefail
cd evmos/proto
MYFOLDER="$(pwd)/autogen"
mkdir -p "$MYFOLDER/proto"
rm -rf "$MYFOLDER/proto"/*

# Ethermint
cd /tmp
git clone https://github.com/evmos/ethermint/
cd ethermint/
git checkout tags/v0.19.3
cp -r ./proto/* "$MYFOLDER/proto"
cp -r ./third_party/proto/* "$MYFOLDER/proto"
cd /tmp
rm -rf ethermint

# Evmos
cd /tmp
git clone https://github.com/evmos/evmos/
cd evmos/
git checkout tags/v8.2.3
cp -r ./proto/* "$MYFOLDER/proto"
cp -r ./third_party/proto/* "$MYFOLDER/proto"
cd /tmp
rm -rf evmos
