---
title: "Text2Sign: A Practical Single-GPU Diffusion Architecture for Text-to-Sign Language Video Generation"
authors:
- admin
date: "2026-03-21T00:00:00Z"
publishDate: "2026-03-21T00:00:00Z"
publication_types: ["article"]
publication: "Compiled Research Manuscript"
publication_short: "Manuscript"
abstract: This paper presents Text2Sign, a text-conditioned diffusion architecture for short sign-language video clips designed to operate on a single NVIDIA L4 GPU. The system combines a frozen vision-language text encoder with a 3D encoder-decoder backbone and factorized spatial-temporal attention, balancing generation quality with realistic compute limits.
summary: A single-GPU diffusion system for generating short sign-language videos from text prompts.
tags:
- Accessibility
- Diffusion Models
- Sign Language
- Video Generation
featured: true
links:
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
**Compiled from:** `draft/text2sign_paper/main.tex`

## Abstract

Sign language is a primary communication channel for millions of Deaf and hard-of-hearing people, yet generating signer video directly from text remains difficult because video diffusion models are expensive to train and evaluate. This paper presents **Text2Sign**, a text-conditioned diffusion architecture for short sign-language video clips designed to operate on a single NVIDIA L4 graphics processor rather than multi-node training infrastructure. The model combines a frozen vision-language text encoder with a three-dimensional encoder-decoder backbone and factorized spatial and temporal attention, thereby reducing the cost of full spatio-temporal attention while preserving motion coherence. Three design choices are examined: whether transformer-style blocks improve upon convolution-only baselines, whether a frozen pretrained text encoder is preferable to a task-specific encoder trained from scratch, and whether factorized attention is competitive with full video attention. On a signer-disjoint How2Sign-based setup, the best short-run ablation attains a validation loss of 0.0648, while a longer-run checkpoint reaches 0.00999. A compact evaluation slice of that checkpoint yields SSIM $0.2403\pm0.0238$, PSNR $15.11\pm0.42$ dB, and temporal consistency $1.0000\pm0.0000$; under an 8-step DDIM setting with guidance scale 5.0, the model generates a 32-frame $64\times64$ clip in 12.60 s (2.54 frames/s) with 3.12 GB peak inference memory on a single NVIDIA L4. The results indicate that pretrained text conditioning improves generalization under limited data, although conditioning-control analyses reveal only limited separation between frozen, random, and partially fine-tuned CLIP variants on coarse prompt-sensitivity proxies. The present system remains limited to low-resolution short clips and does not yet include expert linguistic evaluation; accordingly, the reported results should be interpreted as a practical systems study rather than a complete solution to sign-language production.

## Read the paper

[Open the compiled PDF](/publications/text2sign/paper.pdf)

<iframe src="/publications/text2sign/paper.pdf#view=FitH" width="100%" height="980" style="border: 1px solid #d1d5db; border-radius: 12px;"></iframe>