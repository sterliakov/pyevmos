"""Monkey patch :mod:`sphinx` to play well with specific inheritance.

We set __doc_mro__ attribute for classes that should be altered.

Then :func:`sphinx.util.inspect.getmro` is patched to honor this attribute.

Finally, :mod:`sphinx.ext.autosummary` does not read inherited variable members,
so we patch it too to use our brand-new ``getmro``.
"""

from __future__ import annotations

import re

from sphinx.util import inspect


def new_import_ivar_by_name(
    name,
    prefixes=[None],  # noqa: B006  # It is not my decision!
    grouped_exception=False,
):
    """Get instance variables, including parents traversing."""
    from sphinx.ext import autosummary as asum

    # This is original source
    try:
        name, attr = name.rsplit(".", 1)
        real_name, obj, parent, modname = asum.import_by_name(
            name, prefixes, grouped_exception
        )
        qualname = real_name.replace(modname + ".", "")
        analyzer = asum.ModuleAnalyzer.for_module(getattr(obj, "__module__", modname))
        analyzer.analyze()
        if (
            (qualname, attr) in analyzer.attr_docs
            # check for presence in `annotations` to include dataclass attributes
            or (qualname, attr) in analyzer.annotations
        ):
            return real_name + "." + attr, asum.INSTANCEATTR, obj, modname
    except (ImportError, ValueError, asum.PycodeError) as exc:
        raise ImportError from exc
    except asum.ImportExceptionGroup:
        raise  # pass through it as is

    # ===================== Added part ==============================================
    # Try to get something from __annotations__
    if getattr(obj, "__annotations__", {}).get(attr):
        return f"{modname}.{qualname}.{attr}", asum.INSTANCEATTR, obj, modname
    # ===============================================================================

    # Fail as before, if no success.
    raise ImportError


def monkey_patch():
    """Script entry point."""
    from sphinx.ext import autosummary

    autosummary._module.import_ivar_by_name = new_import_ivar_by_name


def fix_altered_signature(app, what, name, obj, options, signature, return_annotation):
    """Fix signature that is created as concatenation of some new fields + existing."""
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
