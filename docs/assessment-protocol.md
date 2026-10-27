# Assessment protocol

This protocol applies equally to a scientist, an independent reviewer, or an agent.
It evaluates a research object's STAMPED profile, not a person's ability, a publication's scientific merit, or the value of a project.

## Establish the object and source

1. Identify the entry point: DOI, repository URL, directory, or deposited record.
2. Record the revision, release, or dated snapshot being assessed and the scope of computational results.
   If the entry point is mutable, state that limit.
3. Use the exact rubric version.
   Record its byte-level SHA-256 when available.
4. Start from the entry point and follow explicit references to implementations, data, environments, provenance, and related records.
   Describe that discovery path in each evidence item.
   Do not silently repair missing links through unrelated searches or personal knowledge.

Externally supplied or independently discovered evidence can be discussed, but must be identified as such and must not erase a discoverability gap in the assessed object.
An external service failure is distinct from an absent link.

## Apply criterion-specific anchors

Read the principle, question, evidence guidance, and complete anchors.
Select the highest anchor whose whole description is supported by the available evidence.
Do not award points simply for a named technology, the number of files, a familiar platform, a prestigious venue, or a polished description.

Each response has a score or `null`.
Missing response keys and null scores are unanswered, contribute zero to a provisional total, and keep the report incomplete.
An assigned zero is a completed judgment against an anchor, not an unanswered item.
Use the anchor text to explain why zero is warranted; do not infer that unobserved practices never occurred.

The observation field distinguishes:

- `observed`: assessable evidence was located, including partial fulfillment;
- `not_findable`: the stated search path did not expose the needed evidence;
- `inaccessible`: a located resource could not be inspected;
- `absent`: inspected evidence establishes the particular missing feature;
- `not_assessed`: the reviewer has not reached a judgment; score must be null.

If evidence is insufficient to choose any anchor responsibly, leave the score null and explain the uncertainty.
If the criterion itself is about reachability, an unfindable component may support an explicit low anchor.
Keep those judgments separate from implementation claims that require access to the component.

Do not invent intermediate scores for a binary criterion.
The anchors define the available values, not a slider between them.
No criterion is removed from the score because of a freeform applicability claim; record the objection in `feedback` so explicit applicability rules can be considered in a later version.

## Record evidence and confidence

Evidence entries identify the locator, what was observed, the discovery path, and access status.
Prefer revision-specific URLs and precise file sections or commands.
State whether claims derive from documentation, inspected code, recorded historical execution, or execution performed for this assessment.
Never describe an execution as performed if it was only documented elsewhere.

Reviewers may optionally provide:

- evidence support: `insufficient`, `partial`, `sufficient`, or `conflicting`, describing how the cited evidence supports the assigned rating;
- confidence: `low`, `moderate`, or `high`, describing confidence in the rating;
- rationale and criterion feedback;
- an improvement flag to identify a useful follow-up.

Blank or null optional judgments mean “not provided.”
None of these fields earns or subtracts points.
This separation does not prevent a criterion from assessing whether the research object itself supplies provenance or documentation where STAMPED requires it.

## Review without overwriting

Each contribution has an assessment ID and reviewer identity.
To review an existing assessment, create another contribution with `review_of` pointing to the original assessment ID.
Retain the original responses.
A reviewer can agree, change a score, add evidence, or flag ambiguous anchors; document substantive changes in rationale or feedback.
Different reviewers can use the same workflow and input format regardless of how their judgment was produced.

Each contribution has a separate total, profile, weights, and completion count.
There is no automatic consensus or average across reviewers.
When comparing profiles, check weights, object revision, and rubric version first.
A complete set of answers does not establish that independent review or execution occurred.

## Learn from the pilot

Record confusing wording, missing applicability cases, conflicting evidence, difficult-to-find resources, and disagreement over anchors as criterion feedback.
Use overall comments for limits applying to the full assessment.
Preserve the original evidence and judgments when revising the rubric, and version changes to criteria, anchors, or scoring.

Review a range of research objects and compare independently produced ratings.
The worked example exercises the workflow; it does not establish inter-rater reliability, validity, or generalizability.
Analyze disagreements before changing criteria: a difference may arise from evidence access, interpretation, scope, or a genuine ambiguity in the rubric.
Agreement alone does not prove validity.

Local files and share links can carry the full contribution bundle.
Do not infer that exporting or sharing a report centrally submits its feedback.
There is no central collection service in the initial pilot.
