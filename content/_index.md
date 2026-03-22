---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  spacing: '6rem'

sections:
  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |
        {{< home-hero-floating-title >}}

        ### Our Mission

        This site investigates how artificial intelligence can be designed, governed, and taught in ways that protect **human dignity**, strengthen **public trust**, and expand **social opportunity**.

        Inspired by the interdisciplinary spirit of technology, philosophy, and civic engagement, the project asks a simple but demanding question: **How do we build intelligent systems without losing sight of the people they are meant to serve?**

        The answer lives in research, essays, real-world experience, and community-facing work. In other words: fewer black boxes, more human responsibility.
    design:
      columns: '1'
      css_class: 'text-center homepage-hero-section'

  - block: collection
    id: research
    content:
      title: Research
      subtitle: 'Compiled papers and working notes on accessibility, efficient AI systems, and responsible model adaptation'
      text: ''
      filters:
        folders:
          - publications
        featured_only: true
      count: 3
    design:
      view: article-grid
      columns: 3

  - block: collection
    id: experience
    content:
      title: Experience
      subtitle: 'Internships and practical engineering work'
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
      subtitle: 'Meetings, workshops, and hands-on learning'
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

  - block: resume-biography-3
    content:
      username: admin
      text: ''
      headings:
        about: 'About the Founder'
        education: 'Education'
        interests: 'Focus Areas'
    design:
      css_class: hbx-bg-gradient
      avatar:
        size: medium
        shape: circle
---
