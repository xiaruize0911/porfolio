---
title: "University Ranking"
date: 2026-01-22
summary: "A bilingual university-search app and REST API that aggregates QS, US News, and related ranking sources into one catalog."
tags:
  - Full stack
  - Education
  - APIs
links:
  - type: custom
    label: Frontend
    url: https://github.com/xiaruize0911/University_Ranking_Frontend
  - type: custom
    label: Backend
    url: https://github.com/xiaruize0911/University_Ranking_Backend
---

**University Ranking** is a product-shaped project rather than a paper: a searchable catalog of universities with bilingual names, theme and language preferences, and ranking data drawn from multiple public sources.

The backend is a REST API over SQLite, with ETL scripts that normalize institution names across datasets and expose filtering by name, country, city, and ranking scheme. The frontend is a React Native / web client with navigation, search, detail pages, and React Query for background refresh.

I wrote about the architecture and the "vibe coding" process on [xiaruize.org](https://xiaruize.org/).

- Frontend: [University_Ranking_Frontend](https://github.com/xiaruize0911/University_Ranking_Frontend)
- Backend: [University_Ranking_Backend](https://github.com/xiaruize0911/University_Ranking_Backend)
