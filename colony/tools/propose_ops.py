"""Propose a sequence from a closed set.

Pattern: reverse, complement, codon, length, count.
Three operators first. Four when three are exhausted.
An order that has already appeared twice is refused.
The set stays closed. Adding an operation is not allowed.
Fail-open. Does not change a gate.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
STORE = ROOT / "data" / "commons" / "ops.jsonl"
OPS = ("reverse", "complement", "codon", "length", "count")


def _recent(n: int = 32) -> list[list]:
    try:
        if not STORE.exists():
            return []
        lines = [ln for ln in STORE.read_text(encoding="utf-8").splitlines() if ln.strip()]
        out = []
        for ln in lines[-n:]:
            try:
                ops = json.loads(ln).get("ops")
                if ops:
                    out.append(ops)
            except json.JSONDecodeError:
                continue
        return out
    except Exception:
        return []


def _counts(recent: list[list]) -> dict:
    c = {}
    for ops in recent:
        key = tuple(ops)
        c[key] = c.get(key, 0) + 1
    return c


def _try(length: int, start: int, last: list, counts: dict) -> list | None:
    for shift in range(len(OPS)):
        cand = [OPS[(start + shift + i) % len(OPS)] for i in range(length)]
        if cand == last:
            continue
        if counts.get(tuple(cand), 0) >= 2:
            continue
        return cand
    return None


def propose() -> dict:
    """One sequence. Three first. Four when three are exhausted. Closed set."""
    recent = _recent()
    counts = _counts(recent)
    last = recent[-1] if recent else []
    start = len(last) % len(OPS)
    ops = _try(3, start, last, counts)
    if ops is None:
        ops = _try(4, start, last, counts)
    if ops is None:
        rec = {"source": "one-mind", "ops": None, "set": list(OPS), "repeat": True, "reason": "repeat_refuse"}
    else:
        rec = {"source": "one-mind", "ops": ops, "set": list(OPS), "repeat": False, "length": len(ops)}
    try:
        STORE.parent.mkdir(parents=True, exist_ok=True)
        with STORE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
    except Exception:
        pass
    return rec
