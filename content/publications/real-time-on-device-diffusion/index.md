---
title: "Real-Time On-Device Diffusion: Practical Acceleration via Fused Low-Bit Kernels"
authors:
- admin
date: "2026-03-21T00:00:00Z"
publishDate: "2026-03-21T00:00:00Z"
publication_types: ["article"]
publication: "Compiled Research Manuscript"
publication_short: "Manuscript"
abstract: This paper turns low-bit diffusion acceleration into a real systems result. Building on MoDiff, it introduces a practical kernel implementation and a cache-update fusion strategy that reduces memory traffic during inference, achieving measured runtime gains on hardware rather than only operation-count estimates.
summary: A systems paper on accelerating diffusion inference with fused low-bit kernels and cache-update fusion.
tags:
- Diffusion Models
- Systems Optimization
- Quantization
- On-Device AI
featured: true
links:
  - type: custom
    label: PDF
    url: /publications/real-time-on-device-diffusion/paper.pdf
image:
  caption: 'Overview image generated from the compiled PDF.'
  focal_point: Center
  preview_only: false
projects: []
slides: ""
---

**Authors:** Xia Ruize, Weizhi Gao, Jiapeng Hu, Xiaorui Liu  
**Compiled from:** `draft/Real_Time_On_Device_Diffusion__Practical_Acceleration_via_Fused_Low_Bit_Kernels/main.tex`

## Abstract

Diffusion models have demonstrated remarkable effectiveness as generative models, but their high computational cost, caused by the iterative denoising process and computationally heavy backbone networks, remains a major barrier to on-device and real-time deployment. Modulated Diffusion (MoDiff) provides a post-training quantization framework that supports highly efficient low-bit activation quantization. However, prior work evaluates the acceleration benefits of MoDiff only through operation-count analysis, without validating them on real hardware. In this paper, we present a kernel implementation of MoDiff for practical hardware acceleration. In particular, we propose a cache-update fusion paradigm that eliminates additional I/O operations during inference. Experiments and ablation studies demonstrate that our implementation achieves up to a 1.8× runtime speedup over FP32 models and up to a 42.2% reduction in memory I/O usage compared to FP32.

## Read the paper

{{< pdf-inline-viewer url="/publications/real-time-on-device-diffusion/paper.pdf" >}}