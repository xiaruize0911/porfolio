# Response to Reviewers

**Original Manuscript ID:** Access-2026-08381  
**Original Article Title:** "Text2Sign: A Computationally Efficient Diffusion Architecture for Text-to-Sign Language Video Generation"

To: IEEE Access Editor  
Re: Response to reviewers

Dear Editor,

Thank you for allowing the resubmission of this manuscript and for the detailed reviewer feedback. The revised package includes:

1. a point-by-point response to all reviewer comments (this document),
2. an updated highlighted manuscript (`main_highlighted.tex` / `main_highlighted.pdf`) with changes marked against the previously rejected/uploaded manuscript version, and
3. a clean revised manuscript (`main.tex` / `main.pdf`).

The revision substantially recalibrates the paper in direct response to the rejection letter dated 17-Mar-2026. In particular, it softens overstated efficiency claims, clarifies that the work is a **practical single-GPU research baseline rather than a real-time deployment system**, tightens the signer-generalization protocol, expands the related-work coverage, adds contextual comparison against prior systems, and makes the limitations substantially more explicit.

## Reviewer 1

### Concern 1
**Reviewer’s concern:** The manuscript should better contextualize the work within the broader evolution of sign-language computing and include additional recent recognition / depth / Fourier-based literature.

**Author response:** We agree. The revised manuscript broadens the introduction and related-work sections to distinguish sign language recognition, translation, and production, and to clarify why recognition advances do not solve the inverse generation problem addressed here.

**Author action:** Added and integrated the requested and closely related references, including `IDF-Sign`, `FSign-Net`, the spatial-temporal Fourier network for 3D sign recognition, the spatio-temporal prosodic/angle feature work, and the redundancy-reduction paper. The discussion now explicitly positions Text2Sign as a synthesis-oriented system rather than a recognition model.

### Concern 2
**Reviewer’s concern:** The claim of computational efficiency was vague and should be grounded in concrete throughput on target hardware.

**Author response:** We agree that the original wording was too strong. Rather than claiming real-time or edge readiness, the revised paper now frames the contribution as a **single-GPU practical baseline** with explicit runtime and memory measurements.

**Author action:** Updated the title and framing throughout the manuscript; reported the measured tuned audit runtime as **12.60 s per 32-frame clip (2.54 frames/s) with 3.12 GB peak inference memory on one NVIDIA L4**; and explicitly stated that the system is **not** real-time or edge-ready in its present form.

### Concern 3
**Reviewer’s concern:** Standard video metrics such as FVD may not correlate with human understanding of sign language.

**Author response:** We agree. The revised manuscript now treats distributional video metrics and motion heuristics as supporting evidence only, not as measures of linguistic correctness.

**Author action:** Strengthened the metric caveats in the experimental setup, discussion, and limitations; clarified that these metrics do not assess intelligibility or signer preference; and explicitly noted the absence of expert linguistic evaluation.

### Concern 4
**Reviewer’s concern:** The manuscript should explain how the frozen CLIP encoder may help with unseen prompts.

**Author response:** We agree. The revised discussion now explains that frozen CLIP may transfer broader semantic structure from large-scale vision-language pretraining, which plausibly helps behavior on prompts that are semantically related to but not identical with the limited training phrases.

**Author action:** Expanded the discussion of frozen text conditioning and added explicit caution that this does **not** establish sign-linguistic correctness on unseen prompts.

### Concern 5
**Reviewer’s concern:** The manuscript should compare the method directly with representative prior systems.

**Author response:** We agree, with the caveat that most prior systems differ in output modality, dataset, or evaluation protocol.

**Author action:** Added a contextual comparison table spanning text-to-pose systems, rule-based/avatar systems, commercial overlay systems, and the present RGB-video diffusion system. The table is explicitly labeled as contextual rather than a direct leaderboard.

### Concern 6
**Reviewer’s concern:** The limitations should be highlighted more clearly.

**Author response:** We agree.

**Author action:** Expanded the limitations section to address low resolution, short clip length, lack of human/expert evaluation, non-real-time inference, and constrained dataset diversity.

### Concern 7
**Reviewer’s concern:** Avoid unsubstantiated and exaggerated claims.

**Author response:** We agree and revised the paper accordingly.

**Author action:** Reframed the paper as a practical systems study and single-GPU research baseline, rather than a complete or deployment-ready sign-language production solution.

## Reviewer 2

### Concern 1
**Reviewer’s concern:** The computational-efficiency claim was overstated relative to the model size and inference speed.

**Author response:** We agree. This concern motivated the strongest reframing in the revision.

**Author action:** Replaced the earlier “computationally efficient” positioning with “practical single-GPU”; added explicit latency and memory measurements; and stated directly that the system remains far from interactive deployment.

### Concern 2
**Reviewer’s concern:** The evaluation did not adequately target linguistic correctness, intelligibility, or semantic match to the text prompt.

**Author response:** We agree that the evaluation remains incomplete from a linguistic standpoint.

**Author action:** Tightened the discussion of metric limitations, retained the back-translation proxy only as indirect evidence, and emphasized in multiple sections that the current results should not be interpreted as demonstrating linguistically reliable sign production.

### Concern 3
**Reviewer’s concern:** The short ablations were underpowered for strong architectural conclusions.

**Author response:** We agree. The revised paper now presents these ablations as **indicative short-budget studies**, not definitive architecture proof.

**Author action:** Rewrote the framing of the 3-epoch ablations, contrasted them with the longer signer-disjoint production run, and used more cautious language in the abstract, discussion, and conclusion.

### Concern 4
**Reviewer’s concern:** The quality metrics and sample sizes were not strong enough to support broad claims.

**Author response:** We agree.

**Author action:** Clarified the compact-audit nature of the reported follow-up results, explicitly described them as bounded reproducibility-oriented checks, and removed any language implying that a small-sample metric slice is a definitive quality evaluation.

### Concern 5
**Reviewer’s concern:** The “frozen CLIP is better” conclusion needed stronger controls.

**Author response:** We agree. The revised manuscript no longer presents frozen CLIP as a universally superior text-conditioning strategy. Instead, it limits the conclusion to the evidence available under the present training budget and adds explicit controls to show what can and cannot be inferred from the current checkpoint.

**Author action:** Added a conditioning-control audit covering **frozen CLIP**, **no-text**, **random-text**, and **partially fine-tuned CLIP** variants. The paper now states clearly that removing text worsens stability, but random-text and partially fine-tuned CLIP remain numerically close to frozen CLIP on coarse pixel-space prompt-sensitivity proxies. The revised discussion therefore treats the result as evidence of **weakly expressed conditioning under the current checkpoint**, not as proof of broad semantic superiority for frozen CLIP.

### Concern 6
**Reviewer’s concern:** The factorized-vs-full-attention story was not fully settled.

**Author response:** We agree that the current evidence is limited to the studied resolution and clip length.

**Author action:** Added an explicit scaling table and revised the discussion to make clear that the factorized-attention claim is bounded to the present setting rather than universally established across longer clips and higher resolutions.

### Concern 7
**Reviewer’s concern:** Generalization claims required a signer-disjoint split and clearer reporting.

**Author response:** We agree.

**Author action:** The revision uses a signer-disjoint 90/10 split with reported signer counts and zero overlap by construction, and the manuscript now explicitly states that this protocol provides a stronger—though still imperfect—estimate of generalization.

### Concern 8
**Reviewer’s concern:** Conditioning should be isolated with no-text, random-text, and encoder-variant controls.

**Author response:** We agree.

**Author action:** Added the conditioning-control audit described above and integrated the result into the discussion as a negative-but-informative finding.

### Concern 9
**Reviewer’s concern:** Code release would improve reproducibility.

**Author response:** We agree that reproducibility is important.

**Author action:** The workspace now maintains a clean package structure, explicit artifact references, and consistent runbook/checklist documentation to support resubmission and future release preparation. We note, however, that the public-release decision remains separate from manuscript revision itself.

## Reviewer 3

### Concern 1
**Reviewer’s concern:** The abstract should reduce unnecessary abbreviations, state the main contributions more clearly, and state the limitations.

**Author response:** We agree.

**Author action:** Rewrote the abstract to reduce overclaiming, state the three main design questions more clearly, provide the final measured runtime/memory result, and explicitly note key limitations.

### Concern 2
**Reviewer’s concern:** The methodology should appear as a dedicated section rather than as part of the introduction.

**Author response:** We agree.

**Author action:** The manuscript now presents **Methodology** as a dedicated section with clearer subsectioning.

### Concern 3
**Reviewer’s concern:** The literature review should be expanded and should include several missing references.

**Author response:** We agree.

**Author action:** Expanded the related-work section and incorporated the requested references, including Ko et al. (2019), Kahlon and Singh (2023), Maia et al. (2025), Filhol et al. (2016), and Rodríguez-Correa et al. (2023), in addition to the broader recognition and accessibility references requested by Reviewer 1.

### Concern 4
**Reviewer’s concern:** The model should be compared with existing or similar approaches.

**Author response:** We agree.

**Author action:** Added the contextual comparison table described above and explicitly discussed why direct numerical comparison is limited by differing modalities and protocols.

### Concern 5
**Reviewer’s concern:** The multi-metric comparison was a strength.

**Author response:** We appreciate this observation.

**Author action:** Preserved the normalized multi-metric comparison while adding stronger caveats about what those metrics do and do not establish.

### Concern 6
**Reviewer’s concern:** The writing quality and structure needed refinement.

**Author response:** We agree.

**Author action:** Polished the structure and wording throughout the abstract, related work, methodology, results, discussion, and conclusion, with particular attention to claim calibration and limitations.

## Additional manuscript-level actions completed

- Fixed LaTeX bibliography URL breaking by enabling better URL hyphenation and line breaking.
- Fixed over-wide tables in the IEEE two-column layout by resizing genuinely wide tables and using starred table placement where appropriate.
- Recompiled both the clean and highlighted manuscripts through the full **pdflatex → bibtex → pdflatex → pdflatex** cycle.

## Closing statement

We thank the Editor and reviewers again for the constructive feedback. The revised manuscript is substantially more cautious, better documented, and better aligned with the actual evidence. Most importantly, it now presents the work as a practical single-GPU baseline with explicit limitations, rather than as a solved sign-language production system.

Best regards,  
**Ruize Xia**
