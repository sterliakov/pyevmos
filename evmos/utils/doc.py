from __future__ import annotations

from typing import Any, Callable, TypeVar

_C = TypeVar("_C", bound=Callable[..., Any])


def _inherit(func: Callable[..., Any]) -> Callable[[_C], _C]:
    """Mark function as inheriting (via decorator) from ``func``.

    See `fix_altered_signature` method in ``conf.py`` for some context.
    """

    def decorator(inner: _C) -> _C:
        inner.__doc__ = func.__doc__
        inner.__name__ = func.__name__
        inner.__qualname__ = func.__qualname__
        inner.__module__ = func.__module__
        inner._inherit_signature_from_ = func  # type: ignore[attr-defined]

        return inner

    return decorator
