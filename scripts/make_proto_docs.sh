#! /usr/bin/env bash

set -euo pipefail
shopt -s globstar
shopt -s nullglob

BASE=evmos/proto/autogen/proto
OUT_RST=docs/source/proto_external
OUT=$OUT_RST/_proto_auto/
OUT_RST_INDEX=docs/source/autogen_proto.rst
template=/out/_template.html

rm -rf "$OUT_RST"
mkdir -p "$OUT_RST"
rm -rf "$OUT"
mkdir -p "$OUT"

cp docs/source/_templates/proto.html "${OUT}_template.html"

declare -a top_levels=("$BASE"/*.proto)
top_levels=("${top_levels[@]#*/*/*/*/}")
if [[ -n ${top_levels[*]} ]]; then
    docker run --rm \
        --user "$(id -u):$(id -g)" \
        -v "$(pwd)/$BASE:/protos" \
        -v "$(pwd)/$OUT:/out" \
        pseudomuto/protoc-gen-doc \
        --doc_opt="$template,proto.html" \
        "${top_levels[@]}"
fi

declare -a first_level_dirs=("$BASE"/*/)
for d in "${first_level_dirs[@]}"; do
    declare -a curfiles=("$d"*.proto)
    curfiles=("${curfiles[@]#*/*/*/*/}")
    readarray -t curfiles < <(printf '%s\0' "${curfiles[@]}" | sort -z | xargs -0n1)
    base="${d#*/*/*/*/}"
    base="${base%/}"
    base="${base//\//_}"
    if [[ -n ${curfiles[*]} ]]; then
        docker run --rm \
            --user "$(id -u):$(id -g)" \
            -v "$(pwd)/$BASE:/protos" \
            -v "$(pwd)/$OUT:/out" \
            pseudomuto/protoc-gen-doc \
            --doc_opt="$template,${base}.html" \
            "${curfiles[@]}"
    fi
done

declare -a second_level_dirs=("$BASE"/*/*/)
for d in "${second_level_dirs[@]}"; do
    curfiles=("$d"**/*.proto)
    curfiles=("${curfiles[@]#*/*/*/*/}")
    readarray -t curfiles < <(printf '%s\0' "${curfiles[@]}" | sort -z | xargs -0n1)
    base="${d#*/*/*/*/}"
    base="${base%/}"
    base="${base//\//_}"
    if [[ -n ${curfiles[*]} ]]; then
        docker run --rm \
            --user "$(id -u):$(id -g)" \
            -v "$(pwd)/$BASE:/protos" \
            -v "$(pwd)/$OUT:/out" \
            pseudomuto/protoc-gen-doc \
            --doc_opt="$template,${base}.html" \
            "${curfiles[@]}"
    fi
done

rm "$OUT/_template.html"

rm -f "$OUT_RST_INDEX"

{
    printf 'Original protobuf files documentation\n'
    printf '=====================================\n\n'
    printf '.. toctree::\n'
    printf '    :caption: Proto messages contents\n\n'
} >>$OUT_RST_INDEX

for f in $(find "$OUT" -type f | sort); do
    fbase=$(basename "$f")
    fbase="${fbase%.*}"
    printf '    proto_external/%s\n' "$fbase" >>$OUT_RST_INDEX

    final_rst="$OUT_RST/$fbase.rst"
    header=${fbase//_//}
    header=${header%.*}
    {
        printf '%s\n' "$header"
        set +o pipefail
        yes '=' | head -n ${#header} | tr -d '\n'
        set -o pipefail
        printf '\n.. raw:: html\n'
        printf '    :file: _proto_auto/%s.html\n\n' "$fbase"
    } >>"$final_rst"
done

chown -R "$(id -u)" "$OUT_RST"
chmod -R 666 "$OUT_RST"
chmod 777 "$OUT_RST"
chown -R "$(id -u)" "$OUT"
chmod -R 666 "$OUT"
chmod 777 "$OUT"
chown "$(id -u)" "$OUT_RST_INDEX"
chmod 666 "$OUT_RST_INDEX"

pre-commit run -a trailing-whitespace || true
pre-commit run -a end-of-file-fixer || true
