"""Documentation helpers."""

from __future__ import annotations

import re

from sphinx.util import inspect


def fix_altered_signature(app, what, name, obj, options, signature, return_annotation):
    """Fix signature that is created as concatenation of some new fields + existing."""
    del app, options
    if (
        "autogen" not in name
        and "Fee" in (signature or "")
        and ".Fee" not in (signature or "")
    ):
        return (
            signature.replace("Fee", "evmos.transactions.common.Fee"),
            return_annotation,
        )

    if what != "function" or not hasattr(obj, "_inherit_signature_from_"):
        return signature, return_annotation

    # initially signature contains (..., *args: _P.args, **kwargs: _P.kwargs)
    orig, *_ = signature.partition("*")  # '(arg: str, ..., last_arg: str'
    add, *_ = str(inspect.signature(obj._inherit_signature_from_))[1:].partition(" ->")
    return f"{orig}{add}", return_annotation


SINCE_RE = re.compile(r"Since: cosmos-sdk (\d+\.\d+(\.\d+)?)")


def fix_directives(app, what, name, obj, options, lines):
    del app, what, obj, options
    if "autogen" not in name:
        return

    res = (
        " ".join(lines)
        .replace("`", "``")
        .replace("````", "``")
        .replace("|", r"\|")
        .replace("*", r"\*")
        .replace("cosmos- sdk", "cosmos-sdk")
    )
    res = SINCE_RE.sub(r"\n\n.. versionadded:: \1\n\n", res)
    lines[:] = re.split(r"  +", (res + "  "))


def setup(app):
    """Set up this extension."""
    app.connect("autodoc-process-signature", fix_altered_signature)
    app.connect("autodoc-process-docstring", fix_directives)
