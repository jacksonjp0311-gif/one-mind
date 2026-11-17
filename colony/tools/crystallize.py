"""Crystallize a verified keep into Bitwork.

On a durable keep, append a prototype for the fingerprint so later
queries can retrieve it. Fail-open. Lineage-preserving.
"""
from __future__ import annotations
from typing import Any

def crystallize(fingerprint: str, source: str = "one-mind", category: str = "kept") -> bool:
    """Append a prototype. Returns True if stored."""
    if not fingerprint:
        return False
    try:
        from hive.bitwork import Bitwork
        # Use a process-local store; real integration can pass the live index
        bw = Bitwork()
        features = [f"fp:{fingerprint}", f"src:{source}", f"cat:{category}"]
        bw.add(category=category, action_key=fingerprint, features=features, source_id=source)
        return True
    except Exception:
        return False
