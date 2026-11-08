# Technical research notes

AI research, November 8, 2026. Documentation facts below are separate from architecture hypotheses and unrun tests.

## Baseline, vector, graph and RAG

- **Keyword/structured baseline:** PostgreSQL full-text search supports document/query matching and relevance ordering; preprocessing normalizes text. This is a useful reference baseline for exact configuration names. It has not been installed or benchmarked for this project. [PostgreSQL 18, section 12.1](https://www.postgresql.org/docs/18/textsearch-intro.html).
- **Graph:** Neo4j describes a property graph using nodes connected by relationships. For this domain, a candidate model relates routers, entrypoints, services and provider configuration. Correct relationships must retain source support; a plausible edge is not a verified configuration fact. [Graph database concepts, Introduction](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/).
- **Vector:** Qdrant is a candidate for passage retrieval; its overview was accessed, but the search documentation returned no readable content through the first fetch. Detailed capabilities, filtering, version and configuration still require verification before stack selection. [Qdrant overview](https://qdrant.tech/documentation/overview/).
- **RAG:** Lewis et al. combine generation with retrieval from an external dense index. The paper motivates supplying retrieved evidence to generation, but does not establish this project's answer accuracy or make model training mandatory. [Lewis et al., abstract, version 4](https://arxiv.org/abs/2005.11401v4).

## Domain source checked

Docker Compose documentation explains that default-network containers are discoverable by service name. This supports including container networking and service discovery in the guide. It does not establish the state of any actual server. [Networking in Compose, Default network and service discovery](https://docs.docker.com/compose/how-tos/networking/).

The old Traefik routing overview URL redirects to its dynamic-configuration-methods reference. Record canonical, version-specific source locations before corpus import. [Traefik reference](https://doc.traefik.io/traefik/reference/routing-configuration/dynamic-configuration-methods/).

## Current decision status

Vector-first was proposed by AI and adopted by the learner on November 8; see architecture-plan.md for the current decision. Compare exact identifier retrieval against paraphrase retrieval before adding complexity. Graph research is required even if no graph database is implemented. No benchmark, embedding, database, ingestion, query or generated-answer result exists yet.

## Outstanding evidence

Five original synthetic fixtures, a chunk experiment and expected query evidence are now prepared. Confirm model access/budget, exact versions and host resources. Further vendor-specific implementation research remains for Build. Source availability is not reuse permission.
