# 2. Individual RAG app + technical research

## Reader and scope

Docker/Traefik guide for a learner investigating an existing container/proxy setup. Review 1 uses five explicitly fictional lab documents; answers must distinguish these facts from unknown real-server conditions. No running app or hosted URL exists yet.

## Research and decision

[Primary-source research](technical-research.md) · [Vector/graph/keyword comparison, chosen architecture and flow diagram](architecture-plan.md).

The learner adopted the AI-suggested vector-first approach for passage explanations/paraphrases, compared with keyword search, and deferred graph implementation because five short documents do not yet justify a second database. This is an adopted design hypothesis, not a measured result. Graph concepts and a source-supported entity/relationship sketch remain in the research.

## Sources, representation and evaluation

[Five permitted synthetic documents and version/hash manifest](../corpus/manifest.json) · [Actual chunking comparison](chunk-experiment.md) · [Five questions with expected source IDs/sections](evaluation-plan.md) · [Executed Plan checks and limits](plan-checks.md).

Import/reimport/update/removal behavior, source-location metadata, real embeddings, retrieval, bounded generation, citations and five observable acceptance checks are designed in the architecture/evaluation records. Actual database/import/retrieval/generation outputs remain unrun. The fixture corpus is AI-authored, not observed production evidence.

## Hosting and unresolved setup

Proposed FastAPI app and private persistent Qdrant store behind existing hosting; no server changes performed. Embedding/generation models, package versions, provider access, actual host memory/storage and budget are unconfirmed. These are explicit Nov 10/12 workshop questions before committing to a paid stack. Exact versions and a working hosted journey are required for Build, not claimed at Plan. See resource/access limits in the architecture plan.

## Changed / checked / next

- Changed: five source fixtures, comparison and adopted architecture, import/retrieval diagram, graph sketch, expected-evidence queries and five planned acceptance checks.
- Checked: manifest JSON, unique IDs, source paths and hashes; executed heading-aware versus fixed 160-character chunk experiment. AI research and operations are disclosed.
- Next: resolve model access/resource questions at Nov 10/12 workshop, pin compatible versions, implement the real hosted import → retrieval → generation journey by November 24. No paid service selected or spending authorized.

## Contribution and later stages

[Reviewed learner/AI contribution record](https://github.com/BombayV/is373-portfolio/blob/main/docs/learner-decisions.md). AI drafted/researched/authored fixtures and ran Plan checks; learner selected topic and adopted proposed architecture/reason. Release December 3 requires persistence/setup/source/query evidence; Improve December 10 requires real human feedback, meaningful change and retest.

[Requirement sources](review-1-sources.md) · [Portfolio record](https://github.com/BombayV/is373-portfolio/blob/main/docs/project-record.md).
