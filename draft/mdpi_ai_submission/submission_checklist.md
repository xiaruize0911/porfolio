# MDPI AI Submission Checklist

## Highest-impact items before upload

- Replace placeholder metadata in `main.tex`:
  - `Author`
  - `AuthorNames`
  - `address`
  - `corres`
  - `authorcontributions`
  - `funding`
- Confirm the title, abstract, and keywords match the final scientific emphasis.
- Verify that all authors approve the exact submitted version.

## Reproducibility improvements that help acceptance

- Prefer a **public archival repository** for code and analysis artifacts if possible.
  - Ideal: GitHub + Zenodo DOI, or institutional repository.
  - Then update `\dataavailability{...}` with the public DOI/URL.
- If possible, include supplementary material listing:
  - exact experiment configuration files;
  - figure/table generation scripts;
  - follow-up metrics JSON used in the manuscript.

## Manuscript-quality checks

- Re-read the abstract to keep it within MDPI’s preferred length and fully self-contained.
- Verify every figure is cited in order and has clear standalone captions.
- Verify every table is cited in order and remains readable in two-column layout.
- Consider moving Flowers102 to supplementary material if a stricter, leaner main narrative is preferred.
- Double-check that all claims about significance remain conservative and consistent with the paper’s stated limitations.

## Technical submission checks

- Compile from `mdpi_ai_submission/` and confirm `main.pdf` builds without missing files.
- ZIP the entire `mdpi_ai_submission/` directory for LaTeX submission.
- Keep file size under MDPI limits.

## Editorial-strategy checks

- Use the prepared `cover_letter.md` as the base cover letter.
- Suggest three reviewers with expertise in:
  - vision transformers / CLIP;
  - parameter-efficient fine-tuning / LoRA;
  - representation analysis or interpretability in deep learning.
- Avoid suggesting anyone who has collaborated with the authors within the last three years.

## Nice-to-have upgrades

- Add ORCID identifiers if available.
- Add a short public repository README describing how figures and tables were generated.
- If multi-seed results become available soon, mention them in a revision rather than over-claiming now.
