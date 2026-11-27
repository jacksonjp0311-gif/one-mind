# Colony learning loop

The colony proposes trials from public method cards and from its
own failures. Hive's deterministic vote chooses at most one legal
op. A change is **kept** only when the self-heal trial window is
strictly better than its baseline *and* the twin control does not
lead on Oracle passes or verified depth. Fitness alone never
decides a keep. Reverts and voids are recorded too. This is not
AGI, not a novel theorem, and not a breakthrough claim.

- Method cards tried: **2**
- Kept: **14**
- Reverted (including twin-not-better): **14**
- Voided (environment changed mid-trial): **19**
- Inconclusive (no signal in either window; not counted against the action): **6**
- Proposed this snapshot: **11**
- Waiting on a twin judgment: **0**
- Hive decision deferred **2** times (`set_knob:direction=up:name=park_cycles:value=12`), waiting on a clean 6-cycle window (same Wilson 700‰ gate).
- Hive shadow picks: resolved 26, correct 0, pending 174, accuracy 0‰

## Per method card

| Card | Method | Tried | Kept | Reverted | Keep rate |
| --- | --- | ---: | ---: | ---: | ---: |
| `mc_bacbbd75d04b` | Perturb candidate claims a little more widely (annealing-style search). | 2 | 0 | 1 | 0‰ |
| `mc_e170e02332fe` | Remember already-tried targets for longer before retrying them (longer working memory). | 1 | 0 | 1 | 0‰ |

## Per op family

| Family | Tried | Kept | Reverted | Keep rate |
| --- | ---: | ---: | ---: | ---: |
| `set_knob:deep_digits` | 6 | 5 | 0 | 833‰ |
| `set_knob:deep_seconds` | 2 | 0 | 1 | 0‰ |
| `set_knob:fast_term_cap` | 7 | 4 | 0 | 571‰ |
| `set_knob:gf_term_cap` | 7 | 3 | 1 | 428‰ |
| `set_knob:park_cycles` | 16 | 2 | 8 | 125‰ |
| `set_knob:perturb_cooldown_cycles` | 2 | 0 | 1 | 0‰ |
| `set_knob:perturb_epsilon` | 3 | 0 | 1 | 0‰ |
| `set_knob:step_size` | 3 | 0 | 1 | 0‰ |
| `set_knob:unused_menu_cycles` | 1 | 0 | 1 | 0‰ |

## Recent outcomes

- `kept` · card `—` · family `set_knob:park_cycles` · cycle `20261116T212728Z_656378` (baseline 4.0, trial 7.0)
- `reverted` · card `—` · family `set_knob:park_cycles` · cycle `20261116T230504Z_2f9546` (baseline 7.0, trial 6.0)
- `reverted` · card `—` · family `set_knob:park_cycles` · cycle `20261117T000430Z_7fec4f` (baseline 6.0, trial 4.0)
- `reverted` · card `—` · family `set_knob:park_cycles` · cycle `20261117T010509Z_15fab9` (baseline 4.0, trial 4.0)
- `voided` · card `—` · family `set_knob:park_cycles` · cycle `20261117T023620Z_29c48a` (baseline 4.0, trial None)
- `voided` · card `—` · family `set_knob:step_size` · cycle `20261119T160439Z_1e2345` (baseline 2.0, trial None)
- `voided` · card `mc_bacbbd75d04b` · family `set_knob:perturb_epsilon` · cycle `20261119T195729Z_48a2bb` (baseline 1.0, trial None)
- `reverted` · card `mc_bacbbd75d04b` · family `set_knob:perturb_epsilon` · cycle `20261120T171815Z_5274f1` (baseline 1.0, trial 0.0)
- `reverted` · card `mc_e170e02332fe` · family `set_knob:unused_menu_cycles` · cycle `20261122T073802Z_5f3e3a` (baseline 1.0, trial 0.0)
- `voided` · card `—` · family `set_knob:step_size` · cycle `20261126T035512Z_d5daec` (baseline 4.0, trial None)
- `reverted` · card `—` · family `set_knob:step_size` · cycle `20261126T224135Z_da9397` (baseline 4.0, trial 3.0)
- `reverted` · card `—` · family `set_knob:park_cycles` · cycle `20261127T045155Z_f9fa13` (baseline 2.0, trial 0.0)

## Reading breadth (knowledge library)

knowledge: 643 papers across 14/14 fields, 331 concepts, 165 cards formed, 2 tested, 0 kept.

| Field | Papers | Concepts | Cards formed | Cards tested | Cards kept |
| --- | ---: | ---: | ---: | ---: | ---: |
| automated_reasoning | 72 | 10 | 2 | 0 | 0 |
| cognitive_science | 17 | 9 | 8 | 1 | 0 |
| consciousness_self_models | 16 | 12 | 2 | 0 | 0 |
| learning_theory | 36 | 41 | 2 | 0 | 0 |
| mathematics | 107 | 1 | 1 | 0 | 0 |
| meta_learning | 28 | 20 | 5 | 0 | 0 |
| multi_agent_systems | 16 | 8 | 2 | 0 | 0 |
| neural_architecture | 80 | 53 | 12 | 0 | 0 |
| open_endedness | 64 | 62 | 64 | 0 | 0 |
| optimization_search | 57 | 63 | 35 | 0 | 0 |
| physics_complex_systems | 37 | 12 | 3 | 0 | 0 |
| recursive_self_improvement | 54 | 2 | 5 | 0 | 0 |
| self_learning_loops | 41 | 22 | 11 | 1 | 0 |
| swarm_collective_intelligence | 18 | 16 | 13 | 0 | 0 |

## Architecture ideas (proposals for a human-built PR; never auto-executed)

- `novelty_archive` — 67 papers (consciousness_self_models, mathematics, neural_architecture, open_endedness, optimization_search, recursive_self_improvement): Keep an archive of behaviourally different claim forms and prefer under-explored ones (novelty/quality-diversity archive).
- `specialist_routing` — 41 papers (neural_architecture, physics_complex_systems): A gating step that sends each target to a specialist desk (mixture-of-experts style routing).
- `swarm_topology` — 20 papers (automated_reasoning, multi_agent_systems, neural_architecture, optimization_search, physics_complex_systems, swarm_collective_intelligence): Several improver agents propose over one shared candidate pool and a vote picks one (swarm/consensus topology).
- `self_play_challenger` — 17 papers (self_learning_loops): A challenger role that generates harder variants of solved targets for the solver desks (self-play curriculum).
- `meta_controller` — 14 papers (meta_learning, self_learning_loops): A meta-level desk that learns which kinds of self-heal trials tend to win and orders trials accordingly.

Not AGI. Not discovery. Human authorize still required for durable accepts.

