# Worked assessment: paper-remodnav

This is an initial, source-based STAMPED assessment for human review.
It is an exercise of the pilot rubric, not a validation of the rubric or a judgment of the paper's scientific conclusions.
No independent second review has been fabricated.

## Research-object boundary

The entry point is [psychoinformatics-de/paper-remodnav](https://github.com/psychoinformatics-de/paper-remodnav), assessed at commit `34388d3ca78fbd483e022e4e2851be390b7eebf2`.
The assessed task is reproducing the computational numerical results, figures, and manuscript from the linked input datasets and code.
It does not include recollecting participant measurements.
The README explicitly distinguishes the original workflow from its maintained containerized replacement; this assessment follows the latter while noting the documented output difference.

The evidence boundary includes files and Git history in the object, modules explicitly linked through `.gitmodules`, and the DataLad Containers adapter linked and version-named in the README.
A top-level Git revision fixes the module revisions; links to their current default branches were not substituted for those revisions.

## What was inspected

- The entry-point README, `.gitmodules`, `.datalad/config`, Makefiles, `code/mk_figuresnstats.py`, `container/Dockerfile`, OCI manifests, Git tree, root `COPYING`, and selected recorded computation commits.
- The pinned REMoDNaV module at `d28911838f91f33af0db57332f55ccc442d24f66`, including its MIT license, `setup.py`, and nested data-module declaration.
- The pinned eye-movement labels module at `92279db3850ee4282d97001a3f650fc55cb64b4e`, including its tree and `README`.
- The pinned raw-eye-gaze module's `README.rst` at `a6623bff95ae3676ef0ecad262b5c44ded7cb4a1`, including its public-access and PDDL declarations.
- The explicitly linked Anderson data module at `0e6f82708e10b48039763aa1078696e802260674`, including its tree and GPLv3 text.
- The DataLad Containers Docker adapter at version `1.2.3`, the version named by the object's README, to inspect its new-container and `--rm` behavior.

Git metadata was inspected using read-only commands in temporary partial clones.
No dataset contents or container layers were downloaded.
No project code was executed, no container was built, and no numerical reproducibility claim was independently tested.
A signature is present on the referenced `results-containerized` tag; this review did not verify its authenticity.
Remote source-file access is not proof that every annexed payload remains retrievable.

The example answers 34 of 36 criteria.
`E-03` (independence from previous runs) and `D-01` (retrieval of every intended component version) remain unanswered.
Under the agreed fixed-denominator rule they earn no points in the provisional score; they are not recorded as observed failures.
The website and validator calculate the score from the current rubric and the report's explicit weights.
Do not interpret that provisional number without its completion count and criterion-level rationale.

## Findings that the pilot makes visible

The research object provides unusually concrete evidence for identifying components and replaying computations: pinned Git submodules, content-addressed container blobs, recorded commands and inputs/outputs, and explicit replay instructions with an expected unchanged-tree check.
Those are inspected implementation artifacts rather than an inference from the mere presence of DataLad or Docker.

There are also limits.
The Dockerfile uses a mutable Debian base tag and unversioned Debian packages, although several Python packages are pinned and the already-built image is content-addressed.
Preserving an exact image and rebuilding that image from its recipe are different capabilities.
The root CC-BY-4.0 declaration and some module licenses are reachable, but a complete component-to-license map and a recorded compatibility assessment were not found in the inspected material.
No legal compatibility conclusion is implied.

The README reports that the containerized workflow was verified on Debian, macOS, and Windows 10, and explicitly reports a minor difference from the original publication.
That is evidence of a documented claim and correction history; it is not an independent execution result from this review.

## Evidence routes

Each criterion response in `examples/paper-remodnav.json` carries its own locators and discovery paths.
Representative starting points are:

- [Entry-point README](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/README.md).
- [Explicit module links](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/.gitmodules).
- [Recorded analysis execution](https://github.com/psychoinformatics-de/paper-remodnav/commit/57d2565ab70b9d7b41c28aaa253ccc7096900f8d).
- [Recorded image build](https://github.com/psychoinformatics-de/paper-remodnav/commit/3dd49e368d5cfe9ed8ae861d21475ca3fe6b5b9c).
- [Environment recipe](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/container/Dockerfile).
- [Container invocation](https://github.com/psychoinformatics-de/paper-remodnav/blob/34388d3ca78fbd483e022e4e2851be390b7eebf2/.datalad/config).

## How to review this example

Import the JSON into the website and create a separate review with your own identity.
Check the criterion anchors and linked source material, change the ratings you disagree with, and explain why.
Optional evidence-support and confidence judgments describe the review; they do not change its score.
Use criterion feedback to identify ambiguous anchors, overlapping criteria, applicability problems, or evidence that the instructions make hard to find.

Keep the original review and the subsequent review together in the exported bundle.
Disagreement is useful pilot data; it should not be silently replaced by an average.
Fixed-denominator scores and completion counts must be shown together, especially when a reviewer leaves a criterion unanswered.
