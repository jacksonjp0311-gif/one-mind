# Benchmark witness — 2026-11-17T15:49:49Z

- ok_all: `True`
- aggregate_score: `0.9091`
- delta_vs_previous: `0.0045`

- `fft_microbench` ok=True score=1.0 err=1.0255547068925031e-10 s=0.000943 impl=fft_impl_cooley_tukey_iter_v1_slow0
- `fft_stress_microbench` ok=True score=0.8184 err=1.0140415624166922e-09 s=0.004192 impl=fft_impl_cooley_tukey_iter_v1_slow0
- `autodiff_microbench` ok=True score=1.0 err=6.47925602059729e-11 s=6.1e-05 impl=autodiff_reverse_tape_v1
- `lemma_microbench` ok=True score=0.8585 err=0.0 s=5.505996 impl=lemma_impl_v2_basic10_hard187
- `kinematics_microbench` ok=True score=0.8688 err=0.0 s=7.1e-05 impl=kinematics_impl_v1_enabled5

