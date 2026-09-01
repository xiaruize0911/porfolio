---
title: ''
date: 2026-04-06
type: landing

design:
  spacing: '5rem'

sections:
  - block: markdown
    content:
      title: Work
      subtitle: ''
      text: |
        <p class="section-kicker">Results</p>

        These pages are the work that follows the ideas: access, compute limits, and visible adaptation. Venue and preprint links live on each paper page, as publication details rather than as the point of the site.
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
