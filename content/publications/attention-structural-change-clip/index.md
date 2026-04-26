---
title: "Attention Heatmap Drift in a Contrastively Pretrained Vision–Language Model: A Controlled Matched-Learning-Rate Comparison of Full Fine-Tuning and Low-Rank Adaptation"
authors:
- admin
date: "2026-04-06T00:00:00Z"
publishDate: "2026-04-06T00:00:00Z"
publication_types: ["preprint"]
publication: "Preprints"
publication_short: "Preprint"
doi: "10.20944/preprints202604.0317.v1"
abstract: This preprint analyzes attention heatmap drift in a contrastively pretrained vision-language model under matched-learning-rate comparisons of full fine-tuning and low-rank adaptation. It studies CLIP ViT-B/32 attention behavior on downstream visual classification tasks using metrics such as attention entropy, effective receptive field, concentration, head diversity, rollout, and representational similarity.
summary: A controlled matched-learning-rate study of CLIP attention heatmap drift under full fine-tuning and low-rank adaptation.
tags:
- CLIP
- LoRA
- Vision Transformers
- Model Adaptation
featured: true
links:
  - type: custom
    label: DOI
    url: https://doi.org/10.20944/preprints202604.0317.v1
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
**DOI:** [10.20944/preprints202604.0317.v1](https://doi.org/10.20944/preprints202604.0317.v1)<br>
**Source:** ORCID record [0009-0000-0501-0943](https://orcid.org/0009-0000-0501-0943)

## Abstract

Fine-tuning contrastive vision-language models such as CLIP is an essential step for downstream task specialization, yet the associated changes in internal attention geometry remain insufficiently characterized. This preprint investigates attention heatmap drift in a contrastively pretrained vision-language model through a controlled matched-learning-rate comparison of full fine-tuning and low-rank adaptation. The study uses a multi-faceted metric suite, including CLS-to-patch attention entropy, effective receptive field, concentration, head diversity, attention rollout, representational analysis, and subset-sensitivity tests. The results provide a structural lens for understanding transformer adaptation and suggest that preserving attention structure is an important mechanism for maintaining foundation-model generalization.

## Read the paper

{{< pdf-inline-viewer url="/publications/attention-structural-change-clip/paper.pdf" >}}
