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

        {{< site-stats >}}

        <div class="mission-panel">

        <p class="section-kicker">The through-line</p>

        ### Build capable systems without losing the people they are meant to serve.

        This site collects research, engineering, essays, and school-facing work on artificial intelligence. The technical questions are about generation, adaptation, and efficiency. The civic questions are about dignity, access, and responsibility. They belong in the same place.

        </div>
    design:
      columns: '1'
      css_class: 'homepage-hero-section'

  - block: collection
    id: research
    content:
      title: Research
      subtitle: 'Peer-reviewed and preprint work on accessible generation, model adaptation, and on-device diffusion'
      text: ''
      filters:
        folders:
          - publications
        featured_only: true
      count: 3
    design:
      view: article-grid
      columns: 3
      css_class: 'section-research'

  - block: markdown
    content:
      title: Selected projects
      subtitle: 'Code, models, and tools that sit next to the papers'
      text: |
        {{< selected-projects >}}
    design:
      columns: '1'
      css_class: 'section-projects'

  - block: collection
    id: concerns
    content:
      title: Concerns
      subtitle: 'Longer essays on fairness, labor, and the physical costs behind AI development'
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
    id: experience
    content:
      title: Experience
      subtitle: 'Engineering programs and practical work beyond the classroom'
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

  - block: collection
    id: club
    content:
      title: NFLS AI Club
      subtitle: 'A student community for technical skill, critical reading, and public-facing AI literacy'
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
    id: blog
    content:
      title: Notes
      subtitle: 'Study notes on machine learning, optimization, and how models actually learn'
      text: ''
      page_type: blog
      count: 3
      filters:
        kinds: ["page"]
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      offset: 0
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
