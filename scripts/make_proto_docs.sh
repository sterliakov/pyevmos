#! /usr/bin/env bash

# Get all files like proto/*/*.proto

set -euo pipefail

BASE=evmos/proto/autogen/proto
OUT=docs/source/_static/proto
OUT_RST=docs/source/autogen_proto.rst

rm -rf $OUT

curfiles=$(find $BASE -maxdepth 1 -type f -name '*.proto' | cut -c27- )
if [ "$curfiles" ]
then
    docker run --rm \
        --user "$(id -u):$(id -g)" \
        -v $(pwd)/$BASE:/protos \
        -v $(pwd)/$OUT:/out \
        pseudomuto/protoc-gen-doc \
        --doc_opt="html,proto.html" \
        $curfiles
fi

for d in $(find $BASE -maxdepth 1 -mindepth 1 -type d);
do
    echo $d
    curfiles=$(find $d -maxdepth 1 -type f -name '*.proto' | cut -c27- )
    if [ "$curfiles" ]
    then
        docker run --rm \
            --user "$(id -u):$(id -g)" \
            -v $(pwd)/$BASE:/protos \
            -v $(pwd)/$OUT:/out \
            pseudomuto/protoc-gen-doc \
            --doc_opt="html,$(echo $d | cut -c27- | sed -e 's=/=_=g').html" \
            $curfiles
    fi
done

for d in $(find $BASE -maxdepth 2 -mindepth 2 -type d);
do
    echo $d
    curfiles=$(find $d -type f -name '*.proto' | cut -c27- )
    if [ "$curfiles" ]
    then
        docker run --rm \
            --user "$(id -u):$(id -g)" \
            -v $(pwd)/$BASE:/protos \
            -v $(pwd)/$OUT:/out \
            pseudomuto/protoc-gen-doc \
            --doc_opt="html,$(echo $d | cut -c27- | sed -e 's=/=_=g').html" \
            $curfiles
    fi
done

chmod -R 666 "$OUT"
chmod 777 "$OUT"

# I can't understand original templates, so just do possible minimum
find $OUT -type f | xargs -n1 sed -i \
    's@<h1 id="title">Protocol Documentation</h1>@<div style="display: flex; justify-content: space-between; align-items: center;"><h1 id="title">Protocol Documentation</h1><a href="/">Back to package documentation</a></div>@'

rm -f "$OUT_RST"

printf 'Original protobuf files documentation\n' >> $OUT_RST
printf '=====================================\n\n' >> $OUT_RST
for f in $(find $OUT -type f | sort)
do
    header_under=$(echo $f | cut -c27-)
    header=$(echo $header_under | sed -e 's=_=/=g')
    header=${header%.*}
    printf "%s\n" $header >> $OUT_RST
    (yes '-' || true) | head -n ${#header} | tr -d '\n' >> $OUT_RST
    printf '\n`%s <%s>`_\n\n' $header_under $(echo $f | cut -c12-) >> $OUT_RST
done

chmod -R 666 "$OUT_RST"
