#!/bin/bash

set -euo pipefail

EVMOS_TAG=v20.0.0

cd evmos/proto
protos_root="$(pwd)/autogen"
mkdir -p "$protos_root/proto"
rm -rf "$protos_root/proto"/*

temp=$(mktemp -d)
cd "$temp"
git clone -b "$EVMOS_TAG" --depth 1 https://github.com/evmos/evmos/
cd evmos/
make proto-download-deps proto-gen
cp -r ./proto/* "$protos_root/proto"
cp -r ./swagger-proto/third_party/* "$protos_root/proto"

printf "Trying to clean up %s\n" "$temp"...
cd ~
if ! rm -rf "$temp" &>/dev/null; then
    printf "Failed to clean up temporary directory, please do it yourself (%s)\n" "$temp" >&2
    exit 1
fi
