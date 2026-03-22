# Final Submission Checklist

This checklist consolidates the IEEE Access resubmission requirements with the current state of this workspace.

## Required IEEE Access resubmission items

- [x] **Reviewer comments addressed in the manuscript**  
	The manuscript has been updated to address structure, literature review, signer-disjoint evaluation, conditioning controls, claim calibration, runtime reporting, and limitations.

- [x] **Grammar and wording reviewed**  
	Major wording was revised to reduce overclaiming and improve clarity. A final manual proofread is still recommended before portal upload.

- [x] **Math formatting checked against IEEE style**  
	Equations use italic single-letter variables, upright units, and explicit vector notation where used.

- [x] **References checked for consistency and relevance**  
	Reviewer-suggested references were incorporated where relevant, and the bibliography compiles successfully.

- [x] **Response-to-reviewers document prepared**  
	File: `text2sign_paper/RESPONSE_TO_REVIEWERS.md`

- [x] **Highlighted revised manuscript prepared**  
	Files: `text2sign_paper/main_highlighted.tex`, `text2sign_paper/main_highlighted.pdf`

- [x] **Clean revised manuscript prepared**  
	Files: `text2sign_paper/main.tex`, `text2sign_paper/main.pdf`

- [x] **LaTeX source and PDF both available**  
	Clean and highlighted variants both exist and compile.

- [x] **Author biographies included**  
	Included in both manuscript sources.

- [ ] **Supplementary files packaged (only if they were already part of peer review)**  
	No new supplementary material should be uploaded unless it was already included previously.

- [x] **Byline-change form decision made**  
	No author-list change is present, so `Request-for-Byline-Change--2-.docx` is **not needed**.

## Manuscript integrity checks completed

- [x] Citations resolve after the full build sequence.
- [x] Wide tables were adapted for the IEEE two-column layout.
- [x] Bibliography URLs now break cleanly instead of pushing content outside the column.
- [x] The title and abstract consistently use the “practical single-GPU” framing.
- [x] The signer-disjoint split statistics in the manuscript match the stated protocol.
- [x] Runtime, memory, and audit numbers match the artifact-backed values already referenced in the manuscript package.
- [x] Limitations now explicitly state that the system is low-resolution, non-real-time, and not yet validated by expert human evaluation.

## Files to upload in the portal

### Main Manuscript
- `text2sign_paper/main.tex`
- `text2sign_paper/main.pdf`

### Highlighted PDF
- `text2sign_paper/main_highlighted.pdf`

### Author’s Response Files
- `text2sign_paper/RESPONSE_TO_REVIEWERS.md`

### Optional / only if applicable
- Supplementary `.zip` package **only if** it was already part of peer review
- Byline-change form **not required** for the current single-author revision

## Build sequence used successfully

For both `main.tex` and `main_highlighted.tex`, the following sequence completed successfully:

1. `pdflatex`
2. `bibtex`
3. `pdflatex`
4. `pdflatex`

## Recommended final manual checks before upload

- [ ] Open `main.pdf` and `main_highlighted.pdf` and visually verify float placement page by page.
- [ ] Confirm the highlighted PDF style is acceptable for the portal review workflow.
- [ ] Do one final English-language proofread for small typography issues (hyphenation, em dashes, line breaks).
- [ ] Verify the portal metadata uses the revised title exactly as in the manuscript.

## Submission-readiness assessment

### Administrative readiness

**Ready.** The required manuscript, highlighted version, and response letter are now present in the workspace.

### Technical readiness

**Borderline but defensible for resubmission.** The manuscript now answers the major reviewer concerns more honestly and concretely, especially on:

- signer-disjoint evaluation,
- missing literature coverage,
- conditioning controls,
- runtime and memory reporting,
- and explicit limitations.

### Would further experiments still help?

**Yes, if time permits.** The strongest remaining weakness is not formatting but evidence: the model still lacks direct human/expert sign-language evaluation, and the conditioning-control audit shows that text faithfulness remains weak. One additional stronger experiment would improve the resubmission materially, for example:

- a larger prompt-faithfulness audit with more prompts and repeats,
- a stronger back-translation or recognition-based semantic proxy,
- or expert qualitative assessment on a small sample.

### Practical recommendation

- **If you need to resubmit soon:** the package is now coherent enough to submit.
- **If you can afford one more revision cycle:** a targeted faithfulness-focused experiment would meaningfully improve the paper’s chances.

## Artifact references

- Runbook: `text_to_sign/RESUBMISSION_RUNBOOK.md`
- Automation summary: `text_to_sign/resubmission_results_summary.md`
- Benchmark artifact: `text_to_sign/benchmark_results.json`
- Back-translation probe: `text_to_sign/backtranslation_probe.json`
- Conditioning audit artifact: `text_to_sign/conditioning_ablation_eval_20260320/conditioning_ablation_summary.json`
