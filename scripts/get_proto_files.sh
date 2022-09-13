#!/bin/bash

set -euo pipefail
cd evmos/proto
MYFOLDER="$(pwd)/aautogen"

# Ethermint
mkdir -p proto
cd /tmp
git clone https://github.com/tharsis/ethermint/
cd ethermint/
cp -r ./proto/* "$MYFOLDER/proto"
cp -r ./third_party/proto/* "$MYFOLDER/proto"
cd /tmp
rm -rf ethermint

# Evmos
cd /tmp
git clone https://github.com/tharsis/evmos/
cd evmos/
cp -r ./proto/* "$MYFOLDER/proto"
cp -r ./third_party/proto/* "$MYFOLDER/proto"
cd /tmp
rm -rf evmos
