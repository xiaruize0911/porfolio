---
title: When Bias Becomes Infrastructure
date: 2026-03-23
draft: false
summary: A closer look at how AI systems can formalize unequal treatment, with the health-care risk algorithm study as a concrete warning.
---

# When Bias Becomes Infrastructure

The central ethical problem with AI bias is not only that models can be wrong. It is that they can make unequal treatment appear neutral, technical, and inevitable. Once a decision system is placed inside hospitals, hiring pipelines, schools, or public services, the bias is no longer just a defect in a model. It becomes part of institutional infrastructure. That makes it harder to detect, harder to challenge, and easier to defend. The concern is supported not by one isolated case, but by a pattern across different domains: health care, computer vision, and large-scale evaluation work all show that biased outcomes often arise when systems are trained on proxies that reflect existing inequality.

One of the strongest examples comes from health care. In a 2019 *Science* paper, Ziad Obermeyer and colleagues studied a widely used commercial algorithm in the United States that was helping identify which patients should receive extra medical support. The model used historical health spending as a proxy for medical need. On paper, that may sound reasonable. In practice, it encoded a broken social reality: groups that historically received less care also generated lower medical spending, even when they were sicker. The result was systematic under-referral. The paper found that if the bias were corrected, the share of Black patients selected for additional care would rise from **17.7% to 46.5%**. In other words, the system was not discovering who needed help most; it was reproducing patterns from an unequal health system and relabeling them as efficient triage.

That same structural issue appears in computer vision. Joy Buolamwini and Timnit Gebru's *Gender Shades* study found that commercial gender-classification systems performed extremely unevenly across intersectional groups. According to MIT's summary of the work, error rates were as low as **0.8%** for lighter-skinned men but rose to **20.8% to 34.7%** for darker-skinned women. The lesson is not merely that one benchmark was imperfect. It is that a system can look highly accurate in aggregate while failing badly on the people least represented in the training and evaluation pipeline. A polished average can hide an intolerable subgroup failure.

Large-scale government testing has reinforced this broader concern. NIST's Face Recognition Vendor Test reports that demographic differentials remain measurable across contemporary face-recognition systems, based on evaluations involving nearly **200 algorithms**, nearly **100 developers**, and more than **18 million** images of over **8 million** people. That matters because it shows the issue is not reducible to one company or one anecdote. Even as systems improve, demographic performance gaps remain an engineering and governance problem that requires ongoing scrutiny.

This matters well beyond one algorithm. Modern AI systems learn from traces of past decisions: arrests, loans, grades, hiring records, clicks, purchases, insurance claims, and medical spending. Those records do not simply describe the world. They also record who had access, who was ignored, and whose pain counted. If model builders treat historical data as an objective ground truth, the model can quietly absorb social inequality as if it were signal. The technical pipeline then hides the moral choice. A team can say the model is "just optimizing the data" even when the data itself is the artifact of exclusion.

There is a second problem here: scale changes the character of harm. A biased human decision is serious, but a biased model can produce thousands or millions of similar decisions with consistent speed. That consistency is often marketed as fairness. Yet consistency in a bad rule is not justice. It is automation of error. Worse, once institutions trust a model, human reviewers may defer to it even when warning signs are visible. The model becomes a credibility shield.

This is why fairness in AI cannot be reduced to a dashboard metric. A model can satisfy a narrow statistical target and still be built on a morally broken proxy. The more rigorous question is: what exactly is being predicted, what social process generated the labels, and who is most likely to be mismeasured? If the target variable is already downstream of unequal treatment, better optimization may simply deepen the problem. Taken together, the health-care findings, the facial-analysis evidence, and the NIST evaluations point to the same conclusion: bias in AI is not just about bad intentions or sloppy coding. It is about how institutional history enters data, how aggregate performance hides subgroup harms, and how deployment can turn those harms into routine administration.

The lesson is straightforward. AI systems should not be treated as neutral tools dropped into society from outside. They are built from social data, and social data carries the structure of the institutions that produced it. If those institutions are unequal, the model can scale that inequality with impressive polish. That is why audits, domain review, and careful target selection are not optional extras. They are the minimum standard for building systems that claim to make consequential decisions about people.

## Sources

- Obermeyer Z, Powers B, Vogeli C, Mullainathan S. "Dissecting racial bias in an algorithm used to manage the health of populations." *Science* 366(6464), 447-453 (2019). PubMed summary: <https://pubmed.ncbi.nlm.nih.gov/31649194/>
- MIT Media Lab. "Gender Shades" results and documentation. <https://www.media.mit.edu/projects/gender-shades/results/>
- MIT News. "Study finds gender and skin-type bias in commercial artificial-intelligence systems." 12 February 2018. <https://news.mit.edu/2018/study-finds-gender-skin-type-bias-artificial-intelligence-systems-0212>
- National Institute of Standards and Technology. Face Recognition Vendor Test (FRVT). <https://www.nist.gov/programs-projects/face-recognition-vendor-test-frvt>
