---
title: "Matched-Learning-Rate Analysis of Attention Drift and Transfer Retention in Fine-Tuned CLIP"
authors:
- admin
date: "2026-04-06T00:00:00Z"
publishDate: "2026-04-06T00:00:00Z"
publication_types: ["preprint"]
publication: "arXiv preprint arXiv:2604.16410"
publication_short: "arXiv"
doi: "10.48550/arXiv.2604.16410"
abstract: |
  CLIP adaptation can improve in-domain accuracy while degrading out-of-domain transfer, but Full Fine-Tuning and LoRA are often compared under different learning-rate conventions. This 80-run study holds the learning-rate grid fixed across CLIP ViT-B/32 on EuroSAT and Oxford-IIIT Pets. Learning rate strongly modulates attention drift. At matched learning rates, LoRA preserves substantially more zero-shot CIFAR-100 transfer than Full Fine-Tuning. Attention drift is treated as a descriptive diagnostic of representation preservation rather than a causal explanation of transfer behavior.
summary: An 80-run matched-learning-rate study of CLIP attention drift, LoRA, and zero-shot transfer retention.
tags:
- CLIP
- LoRA
- Vision Transformers
- Model Adaptation
featured: true
links:
  - type: custom
    label: arXiv
    url: https://arxiv.org/abs/2604.16410
  - type: custom
    label: Preprints.org
    url: https://doi.org/10.20944/preprints202604.0317.v1
  - type: custom
    label: Code
    url: https://github.com/xiaruize0911/Attention_Collapse_in_CLIP_Fine-tuning_repo
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
**arXiv:** [2604.16410](https://arxiv.org/abs/2604.16410)  
**Earlier preprint:** [10.20944/preprints202604.0317.v1](https://doi.org/10.20944/preprints202604.0317.v1)  
**Code:** [Attention_Collapse_in_CLIP_Fine-tuning_repo](https://github.com/xiaruize0911/Attention_Collapse_in_CLIP_Fine-tuning_repo)  
**ORCID:** [0009-0000-0501-0943](https://orcid.org/0009-0000-0501-0943)

## Abstract

CLIP adaptation can improve in-domain accuracy while degrading out-of-domain transfer, but comparisons between Full Fine-Tuning (Full FT) and LoRA are often confounded by different learning-rate conventions. This paper studies how adaptation method and optimization scale jointly shape attention drift and transfer retention in CLIP using a controlled matched-learning-rate comparison of Full FT and LoRA.

The completed matrix contains 80 runs on CLIP ViT-B/32 across EuroSAT and Oxford-IIIT Pets, spanning four shared learning rates (1e-6, 5e-6, 1e-5, and 5e-5) and five seeds. The study evaluates attention-drift metrics, best validation accuracy, and adapter-aware CIFAR-100 zero-shot accuracy.

Learning rate strongly modulates structural change. On EuroSAT, Full FT moves from mild entropy broadening at 1e-6 to marked contraction at 5e-5, whereas LoRA remains entropy-positive across the full matched grid. At matched learning rates, LoRA preserves substantially more zero-shot transfer than Full FT, averaging 45.13% versus 11.28% CIFAR-100 accuracy on EuroSAT and 58.01% versus 8.54% on Pets. Oxford-IIIT Pets also reveals a regime effect: low-learning-rate LoRA underfits in-domain, so method-only averages can obscure when LoRA becomes competitive.

Overall, matched-learning-rate evaluation materially changes the interpretation of Full FT versus LoRA. Attention drift is most useful as a descriptive diagnostic of representation preservation rather than a causal explanation of transfer behavior.

## Read the paper

{{< pdf-inline-viewer url="/publications/attention-structural-change-clip/paper.pdf" >}}
