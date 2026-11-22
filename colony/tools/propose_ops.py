"""Propose a sequence from a closed set.

Pattern: reverse, complement, codon, length, count.
At most three. A repeat of the last kept sequence is not a proposal.
The set stays closed. Adding an operation is not allowed.
Fail-open. Does not change a gate.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
STORE = ROOT / "data" / "commons" / "ops.jsonl"
OPS = ("reverse", "complement", "codon", "length", "count")


def _last() -> list | None:
    try:
        if not STORE.exists():
            return None
        lines = [ln for ln in STORE.read_text(encoding="utf-8").splitlines() if ln.strip()]
        if not lines:
            return None
        return json.loads(lines[-1]).get("ops")
    except Exception:
        return None


def propose() -> dict:
    """One sequence. Different from the last. Closed set. At most three."""
    last = _last() or []
    # Rotate. First proposal is the known three. Later ones shift.
    start = len(last) % len(OPS)
    ops = [OPS[(start + i) % len(OPS)] for i in range(3)]
    if ops == last:
        ops = [OPS[(start + 1 + i) % len(OPS)] for i in range(3)]
    rec = {"source": "one-mind", "ops": ops, "set": list(OPS), "repeat": False}
    try:
        STORE.parent.mkdir(parents=True, exist_ok=True)
        with STORE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec) + "\n")
    except Exception:
        pass
    return rec
