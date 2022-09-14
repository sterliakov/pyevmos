#! /usr/bin/env bash

set -euo pipefail

BASE=evmos/proto/autogen/proto
OUT_RST=docs/source/proto_external
OUT=$OUT_RST/_proto_auto/
OUT_RST_INDEX=docs/source/autogen_proto.rst
template=/out/_template.html

rm -rf $OUT_RST
mkdir -p $OUT_RST
rm -rf $OUT
mkdir -p $OUT

cp docs/source/_templates/proto.html ${OUT}_template.html

curfiles=$(find $BASE -maxdepth 1 -type f -name '*.proto' | cut -c27- )
if [ "$curfiles" ]
then
    docker run --rm \
        --user "$(id -u):$(id -g)" \
        -v "$(pwd)/$BASE:/protos" \
        -v "$(pwd)/$OUT:/out" \
        pseudomuto/protoc-gen-doc \
        --doc_opt="$template,proto.html" \
        $curfiles
fi

for d in $(find $BASE -maxdepth 1 -mindepth 1 -type d);
do
    echo "$d"
    curfiles=$(find "$d" -maxdepth 1 -type f -name '*.proto' | cut -c27- )
    if [ "$curfiles" ]
    then
        docker run --rm \
            --user "$(id -u):$(id -g)" \
            -v "$(pwd)/$BASE:/protos" \
            -v "$(pwd)/$OUT:/out" \
            pseudomuto/protoc-gen-doc \
            --doc_opt="$template,$(echo "$d" | cut -c27- | sed -e 's=/=_=g').html" \
            $curfiles
    fi
done

for d in $(find $BASE -maxdepth 2 -mindepth 2 -type d);
do
    echo "$d"
    curfiles=$(find "$d" -type f -name '*.proto' | cut -c27- )
    if [ "$curfiles" ]
    then
        docker run --rm \
            --user "$(id -u):$(id -g)" \
            -v "$(pwd)/$BASE:/protos" \
            -v "$(pwd)/$OUT:/out" \
            pseudomuto/protoc-gen-doc \
            --doc_opt="$template,$(echo "$d" | cut -c27- | sed -e 's=/=_=g').html" \
            $curfiles
    fi
done

rm "$OUT/_template.html"

rm -f "$OUT_RST_INDEX"

{
    printf 'Original protobuf files documentation\n'
    printf '=====================================\n\n'
    printf '.. toctree::\n'
    printf '    :caption: Proto messages contents\n\n'
} >> $OUT_RST_INDEX

for f in $(find "$OUT" -type f | sort)
do
    fbase=$(basename "$f")
    fbase="${fbase%.*}"
    printf '    proto_external/%s\n' "$fbase" >> $OUT_RST_INDEX

    final_rst="$OUT_RST/$fbase.rst"
    header=${fbase//_//}
    header=${header%.*}
    {
        printf '%s\n' "$header"
        (yes '=' || true) | head -n ${#header} | tr -d '\n'
        printf '\n.. raw:: html\n'
        printf '    :file: _proto_auto/%s.html\n\n' "$fbase"
    } >> $final_rst
done

chmod -R 666 "$OUT_RST"
chmod 777 "$OUT_RST"
chmod -R 666 "$OUT"
chmod 777 "$OUT"
chmod 666 "$OUT_RST_INDEX"
