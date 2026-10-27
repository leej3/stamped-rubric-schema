# Rubric construction and assessment method

This pilot describes how a research object fulfills the STAMPED principles.
It is a perspective on the organization and reproducibility of a work, not a measure of its overall scientific or software quality.
Content validity, reviewer agreement and usefulness across object types have not been established.

## Source and scope

The criterion content comes from the STAMPED manuscript's principle statements, explanatory spectra and summary table.
The draft records the exact source read:

- Repository: <https://github.com/stamped-principles/stamped-paper>
- Manuscript: `main.tex`
- Revision: `5bbb3ed471a5e9bf8c8e91cdef6b96686c4c53ea`
- Source status: **provisional**, pending the author's definitive reconciliation and source pin.

The tracked manuscript was unchanged in the source checkout when read.
Two untracked research notes were present and were not used.
The rubric uses the 20 principle statements in this manuscript, including T.5 and the licensing and access-boundary statements.
It does not silently substitute an earlier released principles instance.
Each criterion links to the manuscript at the recorded revision.
A later source pin requires review, a new rubric version and explicit handling of existing assessments; changing a source pointer alone is not a migration.

The anchors are operational interpretations of STAMPED, not quotations or new canonical principle statements.
They should be revised when actual assessment shows ambiguity, unreasonable burden, missing cases or inconsistent judgments.

## Starting object and evidence boundary

An assessment starts from a named research object: for example, a DOI record, paper, repository, deposited archive or directory.
Record its version or snapshot, the assessment date and the computational scope.
Follow references that the object makes discoverable and record the path to supporting material.
A repository can be one component rather than the whole research object.

Inventory the scoped computational results and their identified components before applying the anchors.
Consider input data, source code, configurations, environment definitions, executable artifacts, results and associated licenses where those component classes exist.
Do not require a nonexistent component class merely to populate a template.
Conversely, do not narrow the inventory silently to exclude an essential dependency that is difficult to retrieve.

Material found through an independent search or supplied separately may help explain a limitation, but does not retroactively make it discoverable from the assessed object.
Record that distinction.
An assessment from a paper DOI and an assessment starting directly at an implementation repository may legitimately have different self-containment findings.

Distinguish an observed absence, a failure to find evidence, inaccessible material and an item not yet assessed.
A controlled-access component is not a failure merely because authorization is required.
An explicit usable access route and the necessary module boundaries can satisfy the corresponding criteria; inaccessible implementation details may still limit other judgments.

## Applying anchors

There are 36 criteria: four for Self-containment, six for Tracking, six for Actionability, six for Modularity, five for Portability, three for Ephemerality and six for Distributability.
Most use 0–3; T-06, P-04 and D-06 are binary.

Choose the highest anchor whose complete description is supported, and explain which conditions are met or unresolved.
Terms such as "all" refer to the explicit scoped inventory.
Where an anchor contains several necessary conditions, fulfilling only one is insufficient.
The zero anchor means that fulfillment is not demonstrated for this assessment; it does not establish that the practice has never occurred.
Leaving an item unanswered is a separate state.

Do not award extra fulfillment points because a reviewer executed software, attached a large amount of evidence or expressed high confidence.
Evidence is used to justify the judgment about the object.
Optional evidence-support and confidence fields describe the judgment and never enter the score formula.
Existing run records, documented procedures and implementation inspection can provide evidence; actual recomputation may strengthen or contradict that support, but is not a universal assessment requirement.

M.2 explicitly permits direct inclusion and links.
Neither packaging mechanism receives preferential credit.
M-05 accepts an explicitly established uniform access condition as the equivalent outcome when no mixed-access boundary exists.
P-02 likewise permits a demonstrated absence of host-specific settings.
These are written anchor cases, not assessor-created exclusions.

T-06 and D-06 operationalize aspirational practices described in the manuscript prose.
They are not new MUST requirements.
A low value is useful information for project prioritization, not a certification failure.
In particular, D-06 may be poorly matched to source-only objects without executable distributions.
Record that applicability objection in the pilot rather than inventing an exclusion or claiming that such an object is defective.

## Scoring and missingness

For each criterion, normalize its assigned value by its maximum anchor value.
A dimension score is 100 times the mean of these normalized values across every criterion in that dimension.
Thus a binary criterion and a 0–3 criterion have equal contribution within their dimension.

The overall score is the weighted mean of the seven dimension scores.
All seven dimension weights default to one.
Reviewers can adjust dimension weights; the report must preserve their exact values.
The spider plot displays the seven normalized dimension scores.
It is a profile; polygon area is not a score.

Unanswered criteria remain in the fixed denominator and earn no points in the provisional total.
They remain visibly unanswered rather than being stored as explicit zero ratings.
Reports must show completion and mark incomplete reviews as provisional.
A freeform applicability objection or concluding comment does not remove a criterion from the denominator.
A future rubric can adopt explicit applicability rules once real assessments establish the cases that need them.

The dimension weights and equal weighting within each dimension are pilot conventions, not empirical measurements of the relative importance of STAMPED properties.
MUST, SHOULD and MAY labels preserve the manuscript's distinctions; they do not automatically multiply scores or create pass/fail thresholds.
Scores under different scopes, versions, completion states or weights are not interchangeable.
Even identical scoring conventions do not establish a universal ordering of research quality.

## Multiple reviewers and rubric feedback

Every assessment has a reviewer identity.
Human and agent contributions use the same structure and are judged on their contents.
A review of an earlier assessment references that assessment and preserves its original responses; it does not overwrite or automatically average them.
Each reviewer can retain independent scores, evidence, comments, confidence and weights.

Evidence support can be insufficient, partial, sufficient or conflicting; confidence can be low, moderate or high.
Either may be omitted.
A blank field means not provided, not low confidence or insufficient evidence.
Explain contradictory evidence rather than forcing it into a favorable overall label.

Use criterion feedback for unclear anchors, inaccessible evidence, proposed applicability cases, duplicated effort and differences in interpretation.
Use an overall comment for scope limitations and patterns across criteria.
An optional improvement marker records a project's chosen interest without changing a finding or requiring a model of project priorities.

For pilot evaluation, compare reviewers' raw responses and rationales under the same object snapshot and rubric version.
Examine disagreements before deriving agreement summaries.
Preserve whether a review was independent or referred to a prior assessment.
One worked example is a workflow demonstration, not evidence of rubric validity or inter-rater reliability.

## Coverage and distinctions

| Dimension | Criteria | Principle coverage |
| --- | --- | --- |
| Self-containment | S-01–S-04 | S.1, S.2 |
| Tracking | T-01–T-06 | T.1, T.2, T.3, T.4, T.5 |
| Actionability | A-01–A-06 | A.1, A.2 |
| Modularity | M-01–M-06 | M.1, M.2, M.3, M.4 |
| Portability | P-01–P-05 | P.1, P.2, P.3 |
| Ephemerality | E-01–E-03 | E.1 |
| Distributability | D-01–D-06 | D.1, D.2, D.3 |

The principles intentionally interact.
The rubric distinguishes their questions:

- S asks whether an ingredient is reachable from the root; T asks which exact state is identified; D asks whether another recipient can obtain and preserve that state.
  The same manifest can inform all three without proving all three.
- S-04 asks whether license declarations can be reached.
  M-03 assigns terms to separable modules; M-04 addresses their combination.
  D-04 asks whether the terms have unambiguous resolvable identities.
  This decomposition does not certify legal compatibility.
- T-04 asks whether execution provenance is captured.
  T-05 asks whether it records the component versions involved.
  A-06 asks whether the recorded specification supports replay.
- M-06 asks whether module composition is explicitly specified.
  A-04 asks whether acquisition and assembly are executable.
  P asks whether the environment and host assumptions are specified.
  E asks whether execution starts fresh and can discard mutable state.
  D-03 asks whether build inputs resolve to fixed states.
- T-06 concerns authentication of provenance records.
  D-06 concerns the origin and build source of distributed executable artifacts.
  A signed Git tag alone need not establish the origin of a separately published container.

Related criteria can be correlated.
The pilot has not established statistical independence, equal difficulty or interval-scale distances between anchors.
These are explicit design limitations to investigate through use.

## Construction guidance

The Scholar Evaluation skill informed observable anchors, evidence traceability and separation of judgments from their uncertainty.
Its general scholarly-work criteria, personnel-assessment rules and default missingness formula were not imported into STAMPED.
In particular, this pilot deliberately retains unanswered criteria in a fixed denominator, as agreed for this project.

Kassis, T., Agarwal, V., He, Y., Patel, D., and Brueckner, A. M. (2026).
*Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents.* <https://doi.org/10.48550/arXiv.2609.00065>.
The public arXiv record was checked on 2026-10-27 and listed revision v2, with no journal publication reference.
