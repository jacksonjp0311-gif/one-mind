"""Back-to-back evolve chaining: decision logic and workflow contract."""
from __future__ import annotations

from pathlib import Path

import pytest

import colony.chain_next as CN

WF = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "one-mind-evolve.yml"


def _run(rid, status="completed", conclusion="success", branch="main"):
    return {"id": rid, "status": status, "conclusion": conclusion, "head_branch": branch}


def test_kill_switch_default_on():
    assert CN.kill_switch_off(None) is False
    assert CN.kill_switch_off("") is False
    assert CN.kill_switch_off("on") is False
    assert CN.kill_switch_off("ON") is False
    assert CN.kill_switch_off("off") is True
    assert CN.kill_switch_off("OFF") is True
    assert CN.kill_switch_off(" off ") is True


def test_dispatch_when_default_on_and_main_clear():
    ok, reason = CN.should_dispatch(
        chain_var=None,
        ref="refs/heads/main",
        current_run_id=11,
        other_active=[_run(11, status="in_progress", conclusion="")],
        prior_completed=[_run(10, conclusion="success")],
        current_evolve_result="success",
    )
    assert ok is True and reason == "ok"


def test_skip_when_kill_switch_off():
    ok, reason = CN.should_dispatch(
        chain_var="off",
        ref="main",
        current_run_id=11,
        other_active=[],
        prior_completed=[],
        current_evolve_result="success",
    )
    assert ok is False and reason == "kill_switch"


def test_skip_when_not_main():
    ok, reason = CN.should_dispatch(
        chain_var="",
        ref="refs/heads/chain-and-caps",
        current_run_id=11,
        other_active=[],
        prior_completed=[],
        current_evolve_result="success",
    )
    assert ok is False and reason == "not_main"


def test_skip_if_another_run_queued_or_in_progress():
    ok, reason = CN.should_dispatch(
        chain_var="",
        ref="main",
        current_run_id=11,
        other_active=[_run(12, status="queued", conclusion="")],
        prior_completed=[],
        current_evolve_result="success",
    )
    assert ok is False and reason == "already_active"
    ok, reason = CN.should_dispatch(
        chain_var="",
        ref="main",
        current_run_id=11,
        other_active=[_run(13, status="in_progress", conclusion="")],
        prior_completed=[],
        current_evolve_result="success",
    )
    assert ok is False and reason == "already_active"


def test_current_run_does_not_count_as_already_active():
    ok, reason = CN.should_dispatch(
        chain_var="",
        ref="main",
        current_run_id=11,
        other_active=[_run(11, status="in_progress", conclusion="")],
        prior_completed=[],
        current_evolve_result="success",
    )
    assert ok is True and reason == "ok"


def test_chain_after_single_or_double_failure():
    ok, reason = CN.should_dispatch(
        chain_var="",
        ref="main",
        current_run_id=11,
        other_active=[],
        prior_completed=[_run(10, conclusion="success")],
        current_evolve_result="failure",
    )
    assert ok is True and reason == "ok"
    ok, reason = CN.should_dispatch(
        chain_var="",
        ref="main",
        current_run_id=13,
        other_active=[],
        prior_completed=[
            _run(12, conclusion="failure"),
            _run(11, conclusion="success"),
        ],
        current_evolve_result="failure",
    )
    assert ok is True and reason == "ok"


def test_stop_after_three_consecutive_failures():
    ok, reason = CN.should_dispatch(
        chain_var="",
        ref="main",
        current_run_id=13,
        other_active=[],
        prior_completed=[
            _run(12, conclusion="failure"),
            _run(11, conclusion="timed_out"),
            _run(10, conclusion="success"),
        ],
        current_evolve_result="failure",
    )
    assert ok is False and reason == "consecutive_failures"


def test_cancelled_runs_do_not_count_toward_streak():
    # Two real failures around a cancelled run: still chain.
    assert CN.consecutive_failure_streak(
        [_run(12, conclusion="cancelled"), _run(11, conclusion="failure")],
        "failure",
    ) == 2
    # A success after failures resets.
    assert CN.consecutive_failure_streak(
        [_run(12, conclusion="failure"), _run(11, conclusion="failure")],
        "success",
    ) == 0


def test_dispatch_inputs_never_authorize():
    inputs = CN.dispatch_inputs()
    assert inputs["authorize"] == "false"
    assert inputs["cycles"] == "3"
    assert inputs["run_control"] == "true"
    with pytest.raises(ValueError, match="never dispatch with authorize"):
        CN.dispatch_inputs(authorize="true")
    with pytest.raises(ValueError, match="never dispatch with authorize"):
        CN.dispatch_inputs(authorize="TRUE")


def test_workflow_chains_on_main_with_kill_switch_and_actions_write():
    # One Mind has no chain-next job. Watch triggers the next evolve.
    s = WF.read_text(encoding="utf-8")
    assert "Refresh to current main" in s
    assert "chain-next:" not in s
    assert "One Mind watch" in s
    # Concurrency still serializes the evolve group (no pile-up of overlapping evolves).
    assert "group: one-mind-evolve" in s
    assert "cancel-in-progress: false" in s


def test_list_statuses_cover_active_including_pending():
    assert "pending" in CN.ACTIVE_LIST_STATUSES
    assert set(CN.ACTIVE_LIST_STATUSES) >= set(CN._ACTIVE_STATUSES)


def test_pending_run_blocks_dispatch():
    ok, reason = CN.should_dispatch(
        chain_var=None, ref="refs/heads/main", current_run_id=1,
        other_active=[{"id": 2, "status": "pending"}], prior_completed=[],
        current_evolve_result="success",
    )
    assert (ok, reason) == (False, "already_active")


def test_main_queries_pending(monkeypatch):
    seen = []
    def fake_list(repo, status, token):
        seen.append(status)
        return [{"id": 9, "status": "pending"}] if status == "pending" else []
    monkeypatch.setattr(CN, "_list_runs", fake_list)
    monkeypatch.setattr(CN, "_dispatch", lambda *a, **k: (_ for _ in ()).throw(AssertionError("dispatched")))
    monkeypatch.setenv("GITHUB_REPOSITORY", "o/r")
    monkeypatch.setenv("GITHUB_REF", "refs/heads/main")
    monkeypatch.setenv("CURRENT_RUN_ID", "1")
    monkeypatch.delenv("COLONY_CHAIN", raising=False)
    assert CN.main() == 0
    assert "pending" in seen


def test_current_run_result_matches_run_level_conclusion():
    import json as _j
    ok = _j.dumps({"evolve": {"result": "success"}, "evolve-control": {"result": "success"}, "twin-scoreboard": {"result": "skipped"}})
    assert CN.current_run_result(ok, "success") == "success"
    ctrl_fail = _j.dumps({"evolve": {"result": "success"}, "evolve-control": {"result": "failure"}})
    assert CN.current_run_result(ctrl_fail, "success") == "failure"
    assert CN.current_run_result("", "failure") == "failure"
    assert CN.current_run_result("not json", "success") == "success"


def test_streak_counts_current_like_prior_runs():
    import json as _j
    prior = [{"conclusion": "failure"}, {"conclusion": "failure"}]
    cur = CN.current_run_result(_j.dumps({"evolve": {"result": "success"}, "evolve-control": {"result": "failure"}}), "success")
    assert CN.consecutive_failure_streak(prior, cur) == 3
    cur_ok = CN.current_run_result(_j.dumps({"evolve": {"result": "success"}, "evolve-control": {"result": "success"}}), "success")
    assert CN.consecutive_failure_streak(prior, cur_ok) == 0


def test_workflow_passes_needs_json():
    # One Mind has no needs-json chain. Refresh is the contract.
    from pathlib import Path
    s = Path(".github/workflows/one-mind-evolve.yml").read_text()
    assert "Refresh to current main" in s
    assert "NEEDS_JSON" not in s
