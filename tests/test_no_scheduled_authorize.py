"""Scheduled runs never authorize; standing trust runs only on a human dispatch with authorize=true."""
import re
from pathlib import Path

WF = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "one-mind-evolve.yml"


def test_authorize_is_off_unless_human_dispatch_says_true():
    # One Mind has no authorize input and no Authorizer step.
    s = WF.read_text(encoding="utf-8")
    assert "authorize:" not in s
    assert "Authorizer(" not in s
