---
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
    - block: collection
      content:
        title: My Blog
        subtitle: ''
        text: ''
        # Page type to display. E.g. post, talk, publication...
        page_type: blog
        # Choose how many pages you would like to display (0 = all pages)
        count: 0
        # Filter on criteria
        filters:
          kinds: ["page"]
          author: ''
          category: ''
          tag: ''
          exclude_featured: false
          exclude_future: false
          exclude_past: false
          publication_type: ''
        # Choose how many pages you would like to offset by
        offset: 0
        # Page order: descending (desc) or ascending (asc) date.
        order: desc
      design:
        # Choose a layout view
        view: card
        # Reduce spacing
        spacing:
            margin: [0, 0, 0, 0]
        padding: [0, 0, 0, 0]

---