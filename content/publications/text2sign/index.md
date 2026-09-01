---
title: "Text2Sign: A Single-GPU Diffusion Baseline for Text-to-Sign Language Video Generation"
authors:
- admin
date: "2026-01-01T00:00:00Z"
publishDate: "2026-01-01T00:00:00Z"
publication_types: ["article-journal"]
publication: "IEEE Access"
publication_short: "IEEE Access"
doi: "10.1109/ACCESS.2026.3686260"
abstract: |
  Sign language is a primary communication channel for millions of Deaf and hard-of-hearing people, yet generating signer video from text remains expensive. Text2Sign is a text-conditioned diffusion architecture for short sign-language clips that runs on a single NVIDIA L4 GPU. It combines a frozen CLIP text encoder with a 3D encoder-decoder backbone and factorized spatiotemporal attention. On a signer-disjoint How2Sign split, a longer-run checkpoint reaches validation loss 0.00999 and generates a 32-frame 64x64 clip in 12.60 seconds with 3.12 GB peak inference memory. The system remains a research baseline rather than a complete production system. Clips are low-resolution and short, and expert linguistic evaluation is still missing.
summary: Peer-reviewed IEEE Access article on a single-GPU diffusion baseline for text-to-sign language video generation.
tags:
- Accessibility
- Diffusion Models
- Sign Language
- Video Generation
featured: true
links:
  - type: custom
    label: IEEE Access
    url: https://doi.org/10.1109/ACCESS.2026.3686260
  - type: custom
    label: arXiv
    url: https://arxiv.org/abs/2607.13164
  - type: custom
    label: Code
    url: https://github.com/xiaruize0911/text2sign
  - type: custom
    label: Model
    url: https://huggingface.co/xiaruize/text2sign
  - type: custom
    label: PDF
    url: /publications/text2sign/paper.pdf
image:
  caption: 'Overview image generated from the compiled PDF.'
  focal_point: Center
  preview_only: false
projects: []
slides: ""
---

**Authors:** Ruize Xia  
**Published in:** IEEE Access, 2026  
**DOI:** [10.1109/ACCESS.2026.3686260](https://doi.org/10.1109/ACCESS.2026.3686260)  
**arXiv:** [2607.13164](https://arxiv.org/abs/2607.13164)  
**Code:** [github.com/xiaruize0911/text2sign](https://github.com/xiaruize0911/text2sign)  
**Model:** [huggingface.co/xiaruize/text2sign](https://huggingface.co/xiaruize/text2sign)  
**ORCID:** [0009-0000-0501-0943](https://orcid.org/0009-0000-0501-0943)

## Abstract

Sign language is a primary communication channel for millions of Deaf and hard-of-hearing people, yet generating signer video directly from text remains difficult because video diffusion models are expensive to train and evaluate. This article presents **Text2Sign**, a text-conditioned diffusion architecture for short sign-language clips designed to run on a single NVIDIA L4 GPU rather than a multi-node cluster.

The model combines a frozen vision-language text encoder with a three-dimensional encoder-decoder backbone and factorized spatial-temporal attention. That design reduces the cost of full video attention while preserving motion coherence. On a signer-disjoint partition of How2Sign, the best short-run ablation reaches a validation loss of 0.0648, while a longer-run checkpoint reaches 0.00999. On a compact evaluation slice, that checkpoint yields SSIM 0.2403 ± 0.0238, PSNR 15.11 ± 0.42 dB, and temporal consistency 1.0000 ± 0.0000. Under 8-step DDIM sampling with guidance scale 5.0, it generates a 32-frame, 64 × 64 clip in 12.60 seconds (2.54 frames/s) with 3.12 GB peak inference memory.

Held-out audits still show only weak prompt-specific separation, and the system does not yet include expert linguistic evaluation. The contribution should therefore be read as an efficiency-oriented research baseline rather than a complete sign-language production system.

## Read the paper

{{< pdf-inline-viewer url="/publications/text2sign/paper.pdf" >}}
