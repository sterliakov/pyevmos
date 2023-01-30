#!/bin/bash
# NOTE: protoc is required
set -euo pipefail
cd evmos/proto

I=$(pwd)/autogen/proto
DEST_PY=$(pwd)/autogen/py/
mkdir -p "$DEST_PY"
rm -rf "$DEST_PY"/*
cd "$I"

protoc \
    --python_betterproto_out="$DEST_PY" \
    -I "$I" \
    $(find "$I" -iname "*.proto")

touch "$DEST_PY/__init__.py"
