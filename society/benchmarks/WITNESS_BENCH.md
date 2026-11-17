# Benchmark witness — 2026-11-17T08:15:26Z

- ok_all: `True`
- aggregate_score: `0.8842`
- delta_vs_previous: `0.0001`

- `fft_microbench` ok=True score=1.0 err=1.0255547068925031e-10 s=0.0016 impl=fft_impl_cooley_tukey_iter_v1_slow0
- `fft_stress_microbench` ok=True score=0.6945 err=1.0140415624166922e-09 s=0.007788 impl=fft_impl_cooley_tukey_iter_v1_slow0
- `autodiff_microbench` ok=True score=1.0 err=6.47925602059729e-11 s=9.7e-05 impl=autodiff_reverse_tape_v1
- `lemma_microbench` ok=True score=0.8579 err=0.0 s=10.141909 impl=lemma_impl_v2_basic10_hard187
- `kinematics_microbench` ok=True score=0.8688 err=0.0 s=0.000138 impl=kinematics_impl_v1_enabled5

