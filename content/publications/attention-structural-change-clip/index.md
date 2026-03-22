---
title: "Attention Structural Change During CLIP Fine-Tuning: A Comparative Study of Full Fine-Tuning, LoRA, and Regularization"
authors:
- admin
date: "2026-03-21T00:00:00Z"
publishDate: "2026-03-21T00:00:00Z"
publication_types: ["article"]
publication: "Compiled Research Manuscript"
publication_short: "Manuscript"
abstract: This paper analyzes how CLIP ViT-B/32 attention structure changes across 21 fine-tuning configurations on EuroSAT and Oxford-IIIT Pets. It compares full fine-tuning, LoRA, and attention-aware regularization using metrics such as entropy, effective receptive field, Gini concentration, head diversity, rollout, and representational similarity.
summary: A structural analysis of how CLIP attention changes under full fine-tuning, LoRA, and regularization.
tags:
- CLIP
- LoRA
- Vision Transformers
- Model Adaptation
featured: true
links:
  - type: custom
    label: PDF
    url: /publications/attention-structural-change-clip/paper.pdf
image:
  caption: 'Overview image generated from the compiled PDF.'
  focal_point: Center
  preview_only: false
projects: []
slides: ""
---

**Authors:** Ruize Xia  
**Compiled from:** `draft/mdpi_ai_submission/main.tex`

## Abstract

Fine-tuning contrastive vision-language models such as CLIP is an essential step for downstream task specialization, yet the associated changes in the internal attention geometry remain insufficiently characterized. This study investigates the CLIP ViT-B/32 visual encoder across 21 experimental configurations on EuroSAT and Oxford-IIIT Pets, comparing full fine-tuning, low-rank adaptation (LoRA), and explicit attention-based regularization. We employ a multi-faceted metric suite—including CLS-to-patch attention entropy, effective receptive field (ERF), Gini concentration, and head diversity—complemented by attention rollout, CKA representational analysis, and subset-sensitivity tests. Our results demonstrate that full fine-tuning generally induces a contraction of attention support, whereas LoRA configurations maintain or even broaden the spatial distribution relative to the pretrained baseline. Statistical analysis via exact permutation tests identifies the learning rate as a critical determinant of these structural shifts. Furthermore, zero-shot reevaluation confirms that while LoRA incurs minor transfer degradation, it remains significantly more conservative than full fine-tuning. These findings provide a new structural lens for understanding the dynamics of transformer adaptation and suggest that structural preservation is a key mechanism for maintaining the generalizability of foundation models.

## Read the paper

[Open the compiled PDF](/publications/attention-structural-change-clip/paper.pdf)

<iframe src="/publications/attention-structural-change-clip/paper.pdf#view=FitH" width="100%" height="980" style="border: 1px solid #d1d5db; border-radius: 12px;"></iframe>