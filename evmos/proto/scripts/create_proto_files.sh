#!/bin/bash
# NOTE: protoc is required
set -euo pipefail

I=$(pwd)/autogen/proto
DEST_PY=$(pwd)/autogen/py/
mkdir -p $DEST_PY
cd $I
# # This generates js protos (used for testing)
# DEST=$(pwd)/tests/proto/
# mkdir -p $DEST
# grpc_tools_node_protoc --proto_path=$I --js_out=import_style=commonjs,binary:$DEST --grpc_out=generate_package_definition:$DEST $(find $(pwd)/proto -iname "*.proto")

# This generates ts protos (used for src)
protoc \
--python_betterproto_out=$DEST_PY \
-I $I \
$(find $I -iname "*.proto")

touch $DEST_PY/__init__.py
