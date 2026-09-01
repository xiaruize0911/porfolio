---
title: "Text2Sign"
date: 2026-07-14
summary: "Public training and inference code for a single-GPU text-to-sign-language diffusion model, with a Hugging Face checkpoint."
tags:
  - Diffusion
  - Accessibility
  - PyTorch
links:
  - type: custom
    label: Paper
    url: /publications/text2sign/
  - type: custom
    label: GitHub
    url: https://github.com/xiaruize0911/text2sign
  - type: custom
    label: Hugging Face
    url: https://huggingface.co/xiaruize/text2sign
---

**Text2Sign** is the public implementation behind the IEEE Access article of the same name. The repository provides a PyTorch training and inference path for short sign-language clips generated from text, using a frozen CLIP text encoder, a 3D backbone, factorized spatiotemporal attention, and DDIM sampling.

The design target is a single NVIDIA L4 GPU rather than a multi-node cluster. Evaluation uses a signer-disjoint How2Sign split so that appearance memorization is harder to confuse with text-conditioned motion.

- Paper: [IEEE Access](/publications/text2sign/) and [arXiv:2607.13164](https://arxiv.org/abs/2607.13164)
- Code: [github.com/xiaruize0911/text2sign](https://github.com/xiaruize0911/text2sign)
- Checkpoint: [huggingface.co/xiaruize/text2sign](https://huggingface.co/xiaruize/text2sign)
