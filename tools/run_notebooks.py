#!/usr/bin/env python3
"""Execute notebooks end-to-end as a smoke test.

Usage:
    python tools/run_notebooks.py nb1.ipynb [nb2.ipynb ...]

Set QRC_DATA=synthetic to force lesson notebooks onto their offline
synthetic-data path (this is what `make check-nb` does). Notebooks are
executed in place but NOT saved with outputs — this is a smoke test,
not a rendering step.
"""

from __future__ import annotations

import os
import sys
import time

os.environ.setdefault("QRC_DATA", "synthetic")

import nbformat  # noqa: E402
from nbclient import NotebookClient  # noqa: E402


def run(path: str, timeout: int = 900) -> bool:
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name="python3",
        resources={"metadata": {"path": os.path.dirname(os.path.abspath(path))}},
    )
    t0 = time.time()
    try:
        client.execute()
        print(f"PASS  {path}  ({time.time() - t0:.0f}s)")
        return True
    except Exception as e:  # noqa: BLE001
        print(f"FAIL  {path}: {type(e).__name__}: {str(e)[:500]}")
        return False


def main() -> int:
    paths = sys.argv[1:]
    if not paths:
        print("usage: run_notebooks.py nb1.ipynb [nb2.ipynb ...]")
        return 2
    results = [run(p) for p in paths]
    n_fail = results.count(False)
    print(f"\n{len(results) - n_fail}/{len(results)} notebooks passed")
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
