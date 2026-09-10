#!/usr/bin/env python3
"""nbgen — generate Jupyter notebooks from lightweight `.mdnb` sources.

Sources live under tools/nbsrc/, mirroring the course tree:

    tools/nbsrc/01_math/week_01/day_01_summation/exercise.mdnb
      -> 01_math/week_01/day_01_summation/exercise.ipynb

Format rules (a `.mdnb` file is just text):

  * Text outside code fences becomes a **markdown cell** (contiguous text is
    merged into one cell).
  * A fence opened with exactly ```python becomes a **code cell**.
  * To *display* code inside a markdown cell, fence it with ```py instead —
    anything other than ```python stays markdown.
  * A line containing only ---NBGEN-BREAK--- forces a cell boundary.

Usage:
    python tools/nbgen.py                    # regenerate everything
    python tools/nbgen.py path/to/file.mdnb  # or a directory / single file

Generated notebooks are committed clean (no outputs) — learners run them.
"""

from __future__ import annotations

import json
import sys
import uuid
from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parent / "nbsrc"
REPO_ROOT = SRC_ROOT.parent.parent


def parse_source(text: str) -> list[tuple[str, str]]:
    lines = text.splitlines()
    cells: list[tuple[str, str]] = []
    buf: list[str] = []
    in_code = False

    def flush() -> None:
        while buf and not buf[0].strip():
            buf.pop(0)
        while buf and not buf[-1].strip():
            buf.pop()
        if buf:
            cells.append(("code" if in_code else "markdown", "\n".join(buf)))
        buf.clear()

    for line in lines:
        if not in_code and line.strip().startswith("```python"):
            flush()
            in_code = True
        elif in_code and line.strip() == "```":
            flush()
            in_code = False
        elif line.strip() == "---NBGEN-BREAK---":
            flush()
        else:
            buf.append(line)
    flush()
    return cells


def _to_cell(kind: str, src: str) -> dict:
    lines = src.splitlines()
    source = [line + "\n" for line in lines[:-1]] + [lines[-1]]
    if kind == "markdown":
        return {
            "cell_type": "markdown",
            "id": uuid.uuid4().hex[:8],
            "metadata": {},
            "source": source,
        }
    return {
        "cell_type": "code",
        "id": uuid.uuid4().hex[:8],
        "metadata": {},
        "execution_count": None,
        "outputs": [],
        "source": source,
    }


def build_notebook(text: str) -> dict:
    return {
        "cells": [_to_cell(kind, src) for kind, src in parse_source(text)],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> int:
    args = sys.argv[1:]
    sources: list[Path] = []
    if not args:
        sources = sorted(SRC_ROOT.rglob("*.mdnb"))
    else:
        for a in args:
            p = Path(a)
            if p.is_dir():
                sources.extend(sorted(p.rglob("*.mdnb")))
            else:
                sources.append(p)

    written = 0
    for src in sources:
        try:
            rel = src.resolve().relative_to(SRC_ROOT)
        except ValueError:
            rel = Path(src)
            out = REPO_ROOT / rel.with_suffix(".ipynb")
        else:
            out = REPO_ROOT / rel.with_suffix(".ipynb")
        out.parent.mkdir(parents=True, exist_ok=True)
        nb = build_notebook(src.read_text(encoding="utf-8"))
        out.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        written += 1
    print(f"nbgen: wrote {written} notebooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
