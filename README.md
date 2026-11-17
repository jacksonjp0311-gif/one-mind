<p align="center">
  <img src="docs/one-mind-hero.jpg" alt="One Mind — reciprocal learning core" width="100%" />
</p>

<h1 align="center">One Mind</h1>

<p align="center">
  <strong>A reciprocal learning system with durable memory.</strong><br/>
  Pure Python · symbiotic with <a href="https://github.com/jacksonjp0311-gif/agent-colony">Agent Colony</a>
</p>

<p align="center">
  <a href="https://github.com/jacksonjp0311-gif/one-mind/actions/workflows/one-mind-evolve.yml"><img src="https://github.com/jacksonjp0311-gif/one-mind/actions/workflows/one-mind-evolve.yml/badge.svg" alt="Evolve" /></a>
  <img src="https://img.shields.io/badge/language-Python-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/status-active-b7c4b6" alt="Active" />
  <img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT" />
</p>

---

## What this is

One Mind is a lineage that learns from its own trials and from another system's receipts, without inheriting that system's verdicts.

It proposes self-changes, scores them on a sparse binary field (Bitwork), writes what it sees, and crystallizes patterns that repeat. A later process can reload those patterns and retrieve them by key.

It is not Agent Colony. Colony keeps a tighter gate. One Mind keeps a looser one. They share evidence. They do not share authority.

## What is live

| Surface | State |
|---|---|
| Identity | `source: one-mind` on every receipt |
| Exchange | Bidirectional. Pulls Colony's `exchange.jsonl` before scoring |
| Foreign signal | `foreign_fps` published in telemetry (observed 60–96) |
| Crystallization | `data/commons/crystallized.jsonl` — durable, reloadable, keyed |
| Pruning | Activity-dependent: keep the most-used fingerprints, drop the rest |
| Bias | UCB lift on under-tried fingerprints; foreign penalty on shared failures |
| Keep gate | Trial must strictly beat baseline. Twin not required |

## Architecture

- Bitwork retrieval: 4096-bit sparse prototypes, integer score
- Residuals and a self-heal trial / adopt / revert loop
- Symbiotic exchange: versioned receipts, lineage stamps, no verdict transfer
- Surgical implants: small fail-open functions at existing call sites
- Pure Python. No new external dependencies

## How learning works

1. A cycle proposes an action and scores it.
2. A non-keep writes a receipt (`outcome: reverted`) to the exchange.
3. The other lineage's receipts are pulled and counted as foreign priors.
4. A fingerprint seen twice is crystallized: a durable record with a unique key.
5. On reload, a fresh process loads those records and can retrieve them by key.
6. When the store exceeds its budget, the least-used records are pruned.



## Where the keep lives

Two logs. Do not confuse them.

| Log | What it records | Keep? |
|---|---|---|
| `data/commons/cycle_telemetry.jsonl` | Swarm proposals. Outcome is usually `proposed`. | No |
| `society/systems/self_heal.json` | Trial vs baseline. `adopted_count` is the keep count. Evidence array holds `event: adopt`. | Yes |
| `data/commons/crystallized.jsonl` | Durable records. Category `kept` means a trial beat baseline. Category `stable` means repeated observation. | Yes, if `kept` |

A swarm proposal is not a keep. A keep is an adopt in self-heal state, or a `kept` line in the crystallized file.

## Claim boundary

Durable records are of category `stable` (repeated observation) unless a trial beats baseline, in which case the category is `kept`. Semantic gain is not established. This system does not claim general intelligence.

Results here do not transfer to Agent Colony without re-validation under Colony's gates.

## Run

```bash
git clone https://github.com/jacksonjp0311-gif/one-mind.git
cd one-mind
PYTHONPATH=. python3 -m colony evolve --cycles 3 --offline
```

Runners: `.github/workflows/one-mind-evolve.yml`.

## Symbiosis

`data/commons/exchange.jsonl` is the shared bus.  
One Mind reads Colony. Colony reads One Mind.  
A foreign fingerprint can change a score. It cannot change a keep.

## Status

Active. Cycles are running. Crystallized records and foreign counts are on main.  
See the Actions tab for the latest evolve.
