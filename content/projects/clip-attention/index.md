---
title: "CLIP Attention Analysis"
date: 2026-04-06
summary: "Training scripts and analysis code for an 80-run matched-learning-rate study of CLIP attention drift under full fine-tuning and LoRA."
tags:
  - CLIP
  - LoRA
  - Vision Transformers
links:
  - type: custom
    label: Paper
    url: /publications/attention-structural-change-clip/
  - type: custom
    label: GitHub
    url: https://github.com/xiaruize0911/Attention_Collapse_in_CLIP_Fine-tuning_repo
  - type: custom
    label: arXiv
    url: https://arxiv.org/abs/2604.16410
---

This repository stores the experiment code for **Matched-Learning-Rate Analysis of Attention Drift and Transfer Retention in Fine-Tuned CLIP**. The controlled matrix covers CLIP ViT-B/32 on EuroSAT and Oxford-IIIT Pets, four shared learning rates, and five seeds — 80 completed runs in total.

The code records attention-drift metrics, in-domain accuracy, and adapter-aware CIFAR-100 zero-shot accuracy, then rebuilds the manuscript tables from JSON histories. CUDA and Apple MPS backends are both supported.

- Paper: [arXiv:2604.16410](https://arxiv.org/abs/2604.16410)
- Code: [Attention_Collapse_in_CLIP_Fine-tuning_repo](https://github.com/xiaruize0911/Attention_Collapse_in_CLIP_Fine-tuning_repo)
