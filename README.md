<p align="center">
  <img src="docs/one-mind-hero.jpg" alt="One Mind — recursive learning core" width="100%" />
</p>

<h1 align="center">One Mind</h1>

<p align="center">
  <strong>A recursive learning system allowed to grow quickly.</strong><br/>
  Out-of-can experiment · pure Python · symbiotic with Agent Colony
</p>

<p align="center">
  <a href="https://github.com/jacksonjp0311-gif/one-mind/actions/workflows/one-mind-evolve.yml"><img src="https://github.com/jacksonjp0311-gif/one-mind/actions/workflows/one-mind-evolve.yml/badge.svg" alt="Evolve" /></a>
  <img src="https://img.shields.io/badge/language-Python-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/status-experiment-b7c4b6" alt="Experiment" />
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT" />
</p>

---

## What this is

One Mind is a fast-iteration fork of the Agent Colony architecture.  
The hard gates that keep the colony bounded have been relaxed so the system can propose, try, and retain more aggressively while still recording every outcome.

It is not the governed colony. It is the open experiment that runs beside it.

## What changed

| Constraint | Colony | One Mind |
|---|---|---|
| Actions per cycle | 1 | **3** (enforced) |
| Wilson abstain | 700‰ | **400‰** (enforced) |
| Twin control required for keep | Yes | **No** (enforced) |
| Human authorize machinery | Present | Present (not yet stripped) |
| Foreign failure penalty | Local prior | Local prior (cross-repo sync pending) |

Oracle, failure log, residuals, and the append-only witness remain.  
The evolutionary bias now actually changes scores (immutable Match, exact fingerprints).  
A symbiotic exchange file lets it penalize fingerprints that failed in the colony.

## Architecture (still the same substrate)

- Multi-role swarm with Bitwork retrieval
- Residuals (activation, error, confidence, attention, arousal)
- Athanor coherence horizon
- Self-heal trial / adopt / revert
- Evidence receipts and memory organ (receipt-only)
- Pure Python — no new external dependencies

## Claim boundary

Growth speed is prioritized over the original safety gates.  
Results here do not transfer back to Agent Colony without re-validation under the original constraints.  
Not AGI. Not a claim of unbounded self-improvement.

## Run

```bash
git clone https://github.com/jacksonjp0311-gif/one-mind.git
cd one-mind
PYTHONPATH=. python3 -m colony evolve --cycles 3 --offline
```

Runners: `.github/workflows/one-mind-evolve.yml` (every 30 min + manual).

## Symbiosis

`data/commons/exchange.jsonl` carries measured failures and residuals.  
One Mind reads fingerprints written by other sources and applies a capped penalty.  
Colony can do the same. Neither side auto-promotes the other’s claims.

## Status

Active experiment. Cycles are running.  
See the Actions tab for the latest evolve and test results.

---

<p align="center">
  <sub>Derived from Agent Colony · Jackson</sub>
</p>
