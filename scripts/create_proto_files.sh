#!/bin/bash
# NOTE: protoc is required
set -euo pipefail
shopt -s globstar

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
plugin_path=$script_dir/betterproto_wrapped.py

cd evmos/proto

root_dir=$(pwd)/autogen
protos_dir=$root_dir/proto
dest_py_dir=$root_dir/py/
mkdir -p "$dest_py_dir"
rm -rf "${dest_py_dir:?must be set}"/*
cd "$protos_dir"

protoc \
    --python_betterproto_wrapped_out="$dest_py_dir" \
    --plugin=protoc-gen-python_betterproto_wrapped="$plugin_path" \
    -I "$protos_dir" \
    "$protos_dir"/**/*.proto
touch "$dest_py_dir/__init__.py"

cd "$root_dir"
pre-commit run -a trailing-whitespace || true
pre-commit run -a ruff-format || true

# Fix `something` followed by non-terminal which is fine in MD but not in rst.
# shellcheck disable=SC2016
find py -name '*.py' -exec \
    sed -i -E -e 's/`([^`]+)`([^`])/`\1`\\\\s\2/g' -e 's/\\\\s([ `"_])/\1/g' {} \;

# This step isn't critical and only applies cosmetic links changes
git apply links.patch
