# Benchmark witness — 2026-11-28T14:09:08Z

- ok_all: `True`
- aggregate_score: `0.8818`
- delta_vs_previous: `0.0003`

- `fft_microbench` ok=True score=1.0 err=1.0255547068925031e-10 s=0.001775 impl=fft_impl_cooley_tukey_iter_v1_slow0
- `fft_stress_microbench` ok=True score=0.6823 err=1.0140415624166922e-09 s=0.008506 impl=fft_impl_cooley_tukey_iter_v1_slow0
- `autodiff_microbench` ok=True score=1.0 err=6.47925602059729e-11 s=0.000108 impl=autodiff_reverse_tape_v1
- `lemma_microbench` ok=True score=0.8579 err=0.0 s=10.173943 impl=lemma_impl_v2_basic10_hard187
- `kinematics_microbench` ok=True score=0.8688 err=0.0 s=0.000126 impl=kinematics_impl_v1_enabled5

