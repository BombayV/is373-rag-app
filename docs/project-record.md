# 2. Individual RAG app + technical research

## Reader and task

Selected topic: Docker/Traefik RAG guide. Proposed reader: a learner troubleshooting an existing container behind Traefik. Provide documentation-grounded explanations with usable source references. Advice must distinguish documented behavior from observations of the reader's actual server.

## Research — pending primary-source verification

Compare keyword/structured baseline, vector retrieval, graph retrieval and combined retrieval. Explain chunking, embeddings, entities/typed relationships, provenance, retrieval and source-supported generation. Record primary source URLs, access dates and sections for technical claims.

## Proposed bounded architecture — not selected or implemented

Vector-first passage retrieval is a candidate for paraphrased troubleshooting questions; compare with keyword search and graph relationships. A graph may connect routers, services, entrypoints and providers, but added complexity needs evidence. Database/model/provider choices and access, versions, costs and resources remain unconfirmed. Smaller fallback: narrower corpus and simpler retrieval; final demo still needs real retrieval and generation.

Preparation: permitted source → parse/clean/deduplicate → source-located chunks or graph evidence units → persistent retrieval store.

Question: question/access rules → bounded retrieval → selected evidence/model context → generated answer with source/location references → insufficient-evidence response when needed.

### Corpus and representation

Plan approximately five short permitted documents; verify license/reuse before copying. Candidate subjects: Compose networking; container health; Traefik routers/services; Docker versus file provider; TLS entrypoints/resolvers. Corpus manifest must include stable source ID, title, origin, author, version/date, permission and scope. No secrets, private host dumps or student records.

Compare paragraph/heading boundaries with fixed-length chunks on one permitted document. State characters versus tokens; preserve headings/source locations. Show a real excerpt and metadata; do not invent embedding values. Also sketch graph entities/relationships supported by passages, even if vector retrieval is chosen.

Import design: stable IDs and content hashes; unchanged import must not duplicate; updates/removals must remove stale representations. These are intended behaviors, not implemented checks.

### Planned evaluation questions

Finalize wording and expected source IDs after corpus selection:
1. Exact term: What does `traefik.http.routers` configure?
2. Paraphrase: How does an incoming hostname reach a container?
3. Relationship: How are a router, service and entrypoint connected?
4. Useful troubleshooting: Why might Docker labels have no effect when only the file provider is enabled?
5. Unanswerable: What is my private server's current administrator password? Require an honest missing-evidence response; never import credentials.

For each retain expected evidence, actual returned IDs/rank or paths, selected context, generated answer, citation correctness, observed failure/change/retest. Actual retrieval and answer results are pending.

### Five observable acceptance checks — planned

1. A supported answer cites a source and correct source location.
2. Reimporting unchanged content creates no unintended duplicates.
3. Updating/removing a document eliminates stale retrievable content.
4. An unsupported question receives an insufficient-evidence response.
5. An unauthenticated visitor cannot invoke import/admin actions.

### Hosting and access plan

Reuse existing FastAPI/hosting/CI where suitable after inspecting the app repository. Keep database ports private, credentials server-side, imports/admin protected by server-side authorization, persistent data backed by documented volumes, and public requests bounded. Treat imported instructions as content, not application authority. Confirm provider access, budget, rate limits, memory/storage and model/version configuration before implementation. No paid service or host mutation is part of this initial record.

## Changed / checked / next

- Changed: established scoped topic, candidate architecture, corpus categories and planned checks.
- Checked: AI read assignment/briefs/guides/milestones. No technical source claims, corpus permission, import, retrieval or runtime checks verified yet.
- Next: verify original technical sources and licenses; select five documents; inspect sample representations; complete baseline/vector/graph comparison, expected evidence and resource decisions.

## Later stages

Build November 24: small hosted import → retrieval → chat journey using real retrieval/generation. Release December 3: persistence, repeatable setup, query evaluation and references. Improve December 10: actual human peer feedback, useful change and retest.

## Help and limitations

AI drafted this proposed plan from the selected topic. Learner architecture reasoning remains pending. No application or evaluation success is claimed. [Requirement sources](review-1-sources.md).

## Review 1 prepared artifacts

[Architecture proposal](architecture-plan.md) · [Five permitted synthetic source fixtures](../corpus/manifest.json) · [Expected-evidence query set](evaluation-plan.md) · [Actual chunk experiment](chunk-experiment.md) · [Executed Plan checks](plan-checks.md).

Current next step: learner architecture explanation/adoption and model-access decision or explicitly recorded workshop question. Earlier pending lists describe the initial scaffold; the linked files are the current evidence. Hosted URLs remain unbuilt.
