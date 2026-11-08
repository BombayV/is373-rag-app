# Review 2 build progress

November 8, 2026 — work in progress, not ready for submission. Due November 24, 2026 at 1 p.m. Eastern.

## Actual work and checks

Implemented FastAPI interface, terminal-only source importer, Gemini embeddings/generation adapter, Qdrant REST retrieval, source references, persistent request quota and bounded request bodies. Local checks passed for homepage, unconfigured status, missing-import error without a simulated answer, question length, request-body limit and absent public import endpoint. Real browser submitted a sample question and showed the honest missing-import response. No real embeddings, Qdrant storage, generation, repeat-import or hosted E2E verified yet.

## Dependencies

Server resource check: 2 CPU cores, 964 MB RAM, about 187 MB available during inspection, 17 GB disk free, no NVIDIA tool found. Hosted model inference recommended. No model installed and no server/proxy changes made. Existing containers reported unhealthy before this work; investigate actual boundary before deployment.

Candidate free-tier provider: Google Gemini 3.5 Flash-Lite generation and gemini-embedding-001 embeddings (768 dimensions with normalization); account quota/availability unverified. Official pricing and embedding docs inspected by AI. Keep billing disabled; no paid fallback. No API key received or stored in this repository.

Next: learner confirms unused hostnames and creates free-tier API access privately; prepare restricted server secret entry, check DNS/routes/baseline, deploy scoped services, import corpus and collect actual source/representation/query/answer/check evidence. Preserve all existing services. Plan-stage learner/source-review gaps remain as previously recorded.

[Build assignment](https://njit.instructure.com/courses/70733/assignments/769190) · [Provider pricing](https://ai.google.dev/gemini-api/docs/pricing) · [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings).

## Deployment boundary update

Learner approved portfolio.bombayv.com and rag.bombayv.com if unused. No existing file route matched either hostname; both DNS lookups failed during this check. Existing CMS homepage and calculator health returned HTTP 200. No routes/containers changed. DNS A records and private free-tier API-key setup are pending.

## Provider correction

Learner reports Google AI Studio requires billing in their setup. Do not enable billing. Revised implementation uses Groq Free for generation and Jina free-token allowance for embeddings, with no automatic paid fallback. Default candidates: openai/gpt-oss-20b and jina-embeddings-v5-text-nano, 768 normalized dimensions. Model/account eligibility and actual calls remain unverified until private keys are configured. Jina free tokens are finite, not unlimited recurring access. Old Gemini notes above record the earlier candidate and are superseded. Both DNS names still failed a local lookup immediately after learner reported creating records; propagation/configuration must be verified.

Official sources inspected November 8: https://console.groq.com/docs/billing-faqs ; https://console.groq.com/docs/models ; https://console.groq.com/docs/quickstart ; https://jina.ai/embeddings/ .

## Latest infrastructure boundary

Public resolver 1.1.1.1 returned Cloudflare proxy addresses for both agreed hostnames; local system DNS still returned lookup failure. Portfolio archive upload completed. An SSH command to create a new deployment directory, build image is373-portfolio:037256b and start a capped container was sent but returned no output. A bounded follow-up SSH check timed out; the stalled local client was terminated. Remote execution/completion is unknown and must be inspected before retrying. No new Traefik route was installed. Direct-origin CMS HTTPS check timed out; that alone does not establish a public outage because direct access may be restricted. Do not claim hosted completion. No host restart, cleanup or unrelated configuration change performed.

## Runtime capacity finding

SSH recovered. Portfolio image is373-portfolio:037256b built successfully from committed source; base nginx digest sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236. Starting its new container failed while creating a runtime FIFO: /run tmpfs has 97 MB used of 97 MB and 123463/123463 inodes used; root disk still has 17 GB free. New portfolio container is Created, not running; no new route installed. Root-owned runtime directories dominate /run usage. Existing selected ExecIDs counts were zero; this does not establish which runtime files are safe to delete. All five existing services have always/unless-stopped restart policies. Controlled reboot with existing-site recovery checks proposed for explicit learner approval because it affects unrelated services. No reboot, deletion or update performed yet.
