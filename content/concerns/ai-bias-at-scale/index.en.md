---
title: When Bias Becomes Infrastructure
date: 2026-03-23
draft: false
summary: A closer look at how AI systems can formalize unequal treatment, with the health-care risk algorithm study as a concrete warning.
---

# When Bias Becomes Infrastructure

The central ethical problem with AI bias is not only that models can be wrong. It is that they can make unequal treatment appear neutral, technical, and inevitable. Once a decision system is placed inside hospitals, hiring pipelines, schools, or public services, the bias is no longer just a defect in a model. It becomes part of institutional infrastructure. That makes it harder to detect, harder to challenge, and easier to defend.

One of the strongest examples comes from health care. In a 2019 *Science* paper, Ziad Obermeyer and colleagues studied a widely used commercial algorithm in the United States that was helping identify which patients should receive extra medical support. The model used historical health spending as a proxy for medical need. On paper, that may sound reasonable. In practice, it encoded a broken social reality: groups that historically received less care also generated lower medical spending, even when they were sicker. The result was systematic under-referral. The paper found that if the bias were corrected, the share of Black patients selected for additional care would rise from **17.7% to 46.5%**. In other words, the system was not discovering who needed help most; it was reproducing patterns from an unequal health system and relabeling them as efficient triage.

This matters well beyond one algorithm. Modern AI systems learn from traces of past decisions: arrests, loans, grades, hiring records, clicks, purchases, insurance claims, and medical spending. Those records do not simply describe the world. They also record who had access, who was ignored, and whose pain counted. If model builders treat historical data as an objective ground truth, the model can quietly absorb social inequality as if it were signal. The technical pipeline then hides the moral choice. A team can say the model is "just optimizing the data" even when the data itself is the artifact of exclusion.

There is a second problem here: scale changes the character of harm. A biased human decision is serious, but a biased model can produce thousands or millions of similar decisions with consistent speed. That consistency is often marketed as fairness. Yet consistency in a bad rule is not justice. It is automation of error. Worse, once institutions trust a model, human reviewers may defer to it even when warning signs are visible. The model becomes a credibility shield.

This is why fairness in AI cannot be reduced to a dashboard metric. A model can satisfy a narrow statistical target and still be built on a morally broken proxy. The more rigorous question is: what exactly is being predicted, what social process generated the labels, and who is most likely to be mismeasured? If the target variable is already downstream of unequal treatment, better optimization may simply deepen the problem.

The lesson is straightforward. AI systems should not be treated as neutral tools dropped into society from outside. They are built from social data, and social data carries the structure of the institutions that produced it. If those institutions are unequal, the model can scale that inequality with impressive polish. That is why audits, domain review, and careful target selection are not optional extras. They are the minimum standard for building systems that claim to make consequential decisions about people.

## Source

- Obermeyer Z, Powers B, Vogeli C, Mullainathan S. "Dissecting racial bias in an algorithm used to manage the health of populations." *Science* 366(6464), 447-453 (2019). PubMed summary: <https://pubmed.ncbi.nlm.nih.gov/31649194/>
