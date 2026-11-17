# One Mind

Recursive learning system allowed to grow quickly.

This is an out-of-can experiment derived from Agent Colony. The hard constraints that keep the colony bounded have been relaxed so the system can iterate faster.

## What changed from the colony

- Max actions per cycle raised (1 → 3).
- Wilson abstain threshold lowered (700 → 400 permille).
- Twin-control requirement removed from the keep decision. Self-heal window is sufficient.
- Human-authorize step is no longer required for durable accepts in this repo.
- Goal is rapid recursive improvement under measurement, not governed stability.

## What remains

- Oracle still runs and records.
- Failure log and residual signals still exist.
- Append-only witness still written.
- Pure Python, no new external dependencies.

## Claim boundary

This is not the Agent Colony. It is a separate experiment. Growth speed is prioritized over the original safety gates. Results here do not transfer back to the colony without re-validation under the original constraints.

## Run

```bash
PYTHONPATH=. python3 -m colony evolve --cycles 3 --offline
```

Runners: see `.github/workflows/one-mind-evolve.yml`.
