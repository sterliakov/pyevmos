#!/bin/bash
# NOTE: protoc is required
set -euo pipefail
shopt -s globstar

cd evmos/proto

root_dir=$(pwd)/autogen
protos_dir=$root_dir/proto
dest_py_dir=$root_dir/py/
mkdir -p "$dest_py_dir"
rm -rf "${dest_py_dir:?must be set}"/*
cd "$protos_dir"

protoc \
    --python_betterproto_out="$dest_py_dir" \
    -I "$protos_dir" \
    "$protos_dir"/**/*.proto
touch "$dest_py_dir/__init__.py"

cd "$root_dir"
pre-commit run --all-files &>/dev/null || true
git apply links.patch
