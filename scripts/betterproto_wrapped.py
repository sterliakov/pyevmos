#! /usr/bin/env python
"""Wrap around betterproto compiler to better preserve docstrings."""

from __future__ import annotations

import sys
import textwrap
from functools import wraps

from betterproto.plugin import models
from betterproto.plugin.main import main as orig_main


@wraps(models.get_comment)
def get_comment(proto_file, path, indent=4) -> str:
    pad = " " * indent
    for sci_loc in proto_file.source_code_info.location:
        if list(sci_loc.path) == path and sci_loc.leading_comments:
            lines = [
                w
                for e in sci_loc.leading_comments.strip().split("\n")
                for w in textwrap.wrap(
                    e.removeprefix(" "),
                    width=88 - indent,
                    break_long_words=False,
                    break_on_hyphens=False,
                )
            ]

            # This is a field, message, enum, service, or method
            if len(lines) == 1 and len(lines[0]) < 88 - indent - 6:
                lines[0] = lines[0].strip('"')
                return f'{pad}"""{lines[0]}"""'
            joined = f"\n{pad}".join(lines)
            return f'{pad}"""\n{pad}{joined}\n{pad}"""'

    return ""


def main():
    models.get_comment = get_comment
    return orig_main()


if __name__ == "__main__":
    sys.exit(main())
