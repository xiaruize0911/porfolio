---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  spacing: '5.5rem'

sections:
  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |
        {{< home-hero-floating-title >}}

        <div class="mission-panel">

        <p class="section-kicker">The claim</p>

        ### Build systems that remain answerable to the people they affect.

        The work on this site is not a list of venues first. It is a sequence of ideas about access, compute, and judgment — and then the papers, code, and teaching used to pressure-test them.

        </div>

        {{< core-ideas >}}
    design:
      columns: '1'
      css_class: 'homepage-hero-section'

  - block: markdown
    content:
      title: The work
      subtitle: 'Results that follow from the ideas, not the other way around'
      text: |
        {{< work-results >}}
    design:
      columns: '1'
      css_class: 'section-projects'

  - block: collection
    id: concerns
    content:
      title: Writing
      subtitle: 'Essays that keep the ideas in contact with fairness, labor, and material cost'
      text: ''
      count: 3
      filters:
        folders:
          - concerns
        featured_only: false
      order: desc
    design:
      css_class: responsive-card-grid
      view: card
      columns: 3

  - block: collection
    id: club
    content:
      title: Practice
      subtitle: 'The NFLS AI Club is where the same questions get taught, argued, and tried with other students'
      text: ''
      filters:
        folders:
          - nfls-ai-club
        featured_only: false
      count: 4
      order: desc
    design:
      css_class: responsive-card-grid
      view: card
      columns: 3

  - block: collection
    id: experience
    content:
      title: Elsewhere
      subtitle: 'Places the work left the notebook'
      text: ''
      filters:
        folders:
          - experience
        featured_only: false
      count: 3
      order: desc
    design:
      css_class: responsive-card-grid
      view: card
      columns: 3

  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |
        {{< home-cta >}}
    design:
      columns: '1'
      css_class: 'section-cta'

  - block: resume-biography-3
    content:
      username: admin
      text: ''
      headings:
        about: 'About'
        education: 'Education'
        interests: 'Focus areas'
    design:
      css_class: hbx-bg-gradient
      avatar:
        size: medium
        shape: circle
---
