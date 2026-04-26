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
abstract: This IEEE Access article presents Text2Sign, a single-GPU diffusion baseline for text-to-sign language video generation. The system combines a frozen vision-language text encoder with a 3D encoder-decoder backbone and factorized spatial-temporal attention, balancing generation quality with realistic compute limits.
summary: An IEEE Access article on a single-GPU diffusion baseline for text-to-sign language video generation.
tags:
- Accessibility
- Diffusion Models
- Sign Language
- Video Generation
featured: true
links:
  - type: custom
    label: DOI
    url: https://doi.org/10.1109/ACCESS.2026.3686260
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
**Published in:** IEEE Access<br>
**DOI:** [10.1109/ACCESS.2026.3686260](https://doi.org/10.1109/ACCESS.2026.3686260)<br>
**Source:** ORCID record [0009-0000-0501-0943](https://orcid.org/0009-0000-0501-0943)

## Abstract

Sign language is a primary communication channel for millions of Deaf and hard-of-hearing people, yet generating signer video directly from text remains difficult because video diffusion models are expensive to train and evaluate. This article presents **Text2Sign**, a single-GPU diffusion baseline for text-to-sign language video generation. The model combines a frozen vision-language text encoder with a three-dimensional encoder-decoder backbone and factorized spatial and temporal attention, reducing the cost of full spatio-temporal attention while preserving motion coherence. The results indicate that pretrained text conditioning improves generalization under limited data, although the system remains limited to low-resolution short clips and does not yet include expert linguistic evaluation. The contribution should therefore be read as an efficiency-oriented research baseline rather than a complete sign-language production system.

## Read the paper

{{< pdf-inline-viewer url="/publications/text2sign/paper.pdf" >}}
