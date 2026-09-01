---
title: "On-Device Diffusion Kernels"
date: 2026-03-21
summary: "Kernel-level work on MoDiff: fused low-bit operators and cache-update fusion for measured, not only counted, diffusion speedups."
tags:
  - Systems
  - Quantization
  - Diffusion
links:
  - type: custom
    label: Paper
    url: /publications/real-time-on-device-diffusion/
  - type: custom
    label: GitHub
    url: https://github.com/xiaruize0911/MoDiff
---

This project turns Modulated Diffusion (MoDiff) from an operation-count story into a hardware result. The manuscript reports fused low-bit kernels and a cache-update fusion strategy that cuts extra memory traffic during iterative denoising.

On the evaluated setup, the implementation reaches up to **1.8×** runtime speedup over FP32 and up to **42.2%** lower memory I/O. The public tree lives at [github.com/xiaruize0911/MoDiff](https://github.com/xiaruize0911/MoDiff), forked from the official ICML 2025 MoDiff codebase and used as the systems implementation path for the paper.

- Paper: [Real-Time On-Device Diffusion](/publications/real-time-on-device-diffusion/)
- Code: [github.com/xiaruize0911/MoDiff](https://github.com/xiaruize0911/MoDiff)
