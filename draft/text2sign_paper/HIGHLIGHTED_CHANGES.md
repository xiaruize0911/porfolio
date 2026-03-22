# Highlighted Changes Guide

The workspace now contains both manuscript variants:

- Clean manuscript: `text2sign_paper/main.tex` → `main.pdf`
- Highlighted manuscript: `text2sign_paper/main_highlighted.tex` → `main_highlighted.pdf`

The highlighted manuscript is intended to show changes **relative to the previously rejected/uploaded manuscript version** stored under `uploaded_version/text2sign_submission/main.tex`, not relative to intermediate workspace drafts.

## What was highlighted / revised most substantially

1. **Title and abstract**
   - Reframed from a broad “computationally efficient” claim to a more defensible **practical single-GPU** claim.
   - Added explicit measured runtime and memory numbers.
   - Added explicit limitations to the abstract.

2. **Related work and literature coverage**
   - Added the reviewer-requested sign-language recognition, translation, and assistive-technology references.
   - Clarified the distinction between recognition, translation, avatar systems, and RGB-video generation.

3. **Methodology and dataset protocol**
   - Promoted the methods material into a clearer dedicated section.
   - Tightened the dataset protocol description and reported the signer-disjoint split statistics.

4. **Evaluation and results framing**
   - Softened claims around linguistic correctness.
   - Added conditioning-control discussion and explicit negative findings where applicable.
   - Added contextual comparison and theoretical scaling analysis.

5. **Layout and bibliography fixes**
   - Fixed bibliography URL line breaking.
   - Fixed wide tables that exceeded the IEEE two-column layout.
   - Recompiled both clean and highlighted manuscripts successfully.

## Current highlighted-manuscript behavior

The highlighted manuscript uses color-marked revised text referenced against the uploaded rejected baseline and compiles successfully through the full LaTeX/BibTeX cycle. It is suitable as the workspace’s highlighted revision artifact.

## Final manual check before upload

Even though `main_highlighted.pdf` is ready, it is still worth opening the PDF once and confirming that the visual highlighting is sufficiently clear for reviewer navigation in the IEEE Access portal.
