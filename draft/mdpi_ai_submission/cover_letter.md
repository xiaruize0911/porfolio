Dear Editors of *AI*,

Please consider our manuscript, **"Attention Structural Change During CLIP Fine-Tuning: A Comparative Study of Full Fine-Tuning, LoRA, and Regularization,"** for publication as an Article in *AI*.

This work studies an important question in modern artificial intelligence and computer vision: how downstream adaptation changes the internal attention structure of a pretrained vision--language model. Using CLIP ViT-B/32 as a case study, we compare full fine-tuning, LoRA, and explicit regularization across stored experiments on EuroSAT and Oxford-IIIT Pets. Beyond standard downstream accuracy, we quantify structural change using attention entropy, effective receptive field, Gini concentration, head diversity, attention rollout, patch-to-patch entropy, and representational similarity. The results show that full fine-tuning is more structurally disruptive than LoRA on the clearest comparison, and that learning rate is the strongest observed driver of attention contraction.

We believe the manuscript fits *AI* well because it addresses foundational questions in artificial intelligence, deep learning, transfer learning, and computer vision while also providing a reproducible empirical analysis of model adaptation behavior. The paper should be of interest to readers working on parameter-efficient tuning, vision transformers, representation stability, and robust deployment of pretrained models.

The manuscript emphasizes conservative interpretation: it reports corrected exact tests for the small-sample learning-rate sweep, clarifies the limitations of per-layer inferential claims, and corrects the zero-shot evaluation path for LoRA checkpoints. We believe these revisions improve both the rigor and the transparency of the study.

We confirm that this manuscript is original, has not been published previously, and is not under consideration for publication elsewhere. The author has approved the manuscript and agrees with its submission to *AI*.

Thank you for your time and consideration.

Sincerely,

Ruize Xia
Nanjing Foreign Language School, Nanjing, Jiangsu, China
xiaruize0911@gmail.com
