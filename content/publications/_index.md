---
title: ''
date: 2026-04-06
type: landing

design:
  spacing: '5rem'

sections:
  - block: markdown
    content:
      title: Research
      subtitle: ''
      text: |
        <p class="section-kicker">Papers and working notes</p>

        Work collected here sits at the intersection of generative modeling, accessibility, and evaluation. The peer-reviewed and preprint papers are listed first. The working papers ask what should count as a good system once it leaves the benchmark and enters a classroom, clinic, or public office.
    design:
      columns: '1'
      css_class: 'page-intro'

  - block: collection
    id: papers
    content:
      title: Papers
      filters:
        folders:
          - publications
        featured_only: false
    design:
      view: article-grid
      columns: 1
      css_class: 'publication-list'
---
