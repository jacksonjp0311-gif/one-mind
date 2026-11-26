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
- Reverted (including twin-not-better): **12**
- Voided (environment changed mid-trial): **19**
- Inconclusive (no signal in either window; not counted against the action): **6**
- Proposed this snapshot: **10**
- Waiting on a twin judgment: **0**
- Hive decision deferred **2** times (`set_knob:direction=up:name=park_cycles:value=12`), waiting on a clean 6-cycle window (same Wilson 700‰ gate).
- Hive shadow picks: resolved 34, correct 0, pending 166, accuracy 0‰

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
| `set_knob:park_cycles` | 15 | 2 | 7 | 133‰ |
| `set_knob:perturb_cooldown_cycles` | 2 | 0 | 1 | 0‰ |
| `set_knob:perturb_epsilon` | 3 | 0 | 1 | 0‰ |
| `set_knob:step_size` | 2 | 0 | 0 | 0‰ |
| `set_knob:unused_menu_cycles` | 1 | 0 | 1 | 0‰ |

## Recent outcomes

- `kept` · card `—` · family `set_knob:park_cycles` · cycle `20261116T192905Z_bc22f0` (baseline 4.0, trial 5.0)
- `reverted` · card `—` · family `set_knob:park_cycles` · cycle `20261116T202906Z_a13d81` (baseline 5.0, trial 4.0)
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

## Reading breadth (knowledge library)

knowledge: 602 papers across 14/14 fields, 305 concepts, 154 cards formed, 2 tested, 0 kept.

| Field | Papers | Concepts | Cards formed | Cards tested | Cards kept |
| --- | ---: | ---: | ---: | ---: | ---: |
| automated_reasoning | 64 | 9 | 2 | 0 | 0 |
| cognitive_science | 17 | 9 | 8 | 1 | 0 |
| consciousness_self_models | 16 | 12 | 2 | 0 | 0 |
| learning_theory | 35 | 40 | 2 | 0 | 0 |
| mathematics | 105 | 1 | 1 | 0 | 0 |
| meta_learning | 25 | 17 | 4 | 0 | 0 |
| multi_agent_systems | 15 | 8 | 2 | 0 | 0 |
| neural_architecture | 72 | 46 | 11 | 0 | 0 |
| open_endedness | 58 | 57 | 59 | 0 | 0 |
| optimization_search | 51 | 57 | 33 | 0 | 0 |
| physics_complex_systems | 37 | 12 | 3 | 0 | 0 |
| recursive_self_improvement | 50 | 1 | 3 | 0 | 0 |
| self_learning_loops | 39 | 20 | 11 | 1 | 0 |
| swarm_collective_intelligence | 18 | 16 | 13 | 0 | 0 |

## Architecture ideas (proposals for a human-built PR; never auto-executed)

- `novelty_archive` — 62 papers (consciousness_self_models, mathematics, neural_architecture, open_endedness, optimization_search, recursive_self_improvement): Keep an archive of behaviourally different claim forms and prefer under-explored ones (novelty/quality-diversity archive).
- `specialist_routing` — 36 papers (neural_architecture, physics_complex_systems): A gating step that sends each target to a specialist desk (mixture-of-experts style routing).
- `swarm_topology` — 19 papers (automated_reasoning, multi_agent_systems, neural_architecture, optimization_search, physics_complex_systems, swarm_collective_intelligence): Several improver agents propose over one shared candidate pool and a vote picks one (swarm/consensus topology).
- `self_play_challenger` — 15 papers (self_learning_loops): A challenger role that generates harder variants of solved targets for the solver desks (self-play curriculum).
- `meta_controller` — 12 papers (meta_learning, self_learning_loops): A meta-level desk that learns which kinds of self-heal trials tend to win and orders trials accordingly.

Not AGI. Not discovery. Human authorize still required for durable accepts.

