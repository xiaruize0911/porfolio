---
title: ''
date: 2026-09-01
type: landing

design:
  spacing: '5rem'

sections:
  - block: markdown
    content:
      title: Projects
      subtitle: ''
      text: |
        <p class="section-kicker">Code, models, and tools</p>

        These projects sit next to the papers: public training code, model checkpoints, and software that had to work for other people, not only for a figure in a PDF.
    design:
      columns: '1'
      css_class: 'page-intro'

  - block: collection
    content:
      title: Selected work
      subtitle: ''
      text: ''
      count: 0
      filters:
        folders:
          - projects
        featured_only: false
      order: desc
    design:
      css_class: responsive-card-grid
      view: card
      columns: 2
---
