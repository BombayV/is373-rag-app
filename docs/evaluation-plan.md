# Evaluation set — expected evidence only

Five synthetic documents in [manifest](../corpus/manifest.json). This tests the fictional lab scenario, not arbitrary production troubleshooting. No retrieval/generation runs yet.

- Q01 exact term: Which network is named training-proxy? Expected S01 / Shared network: proxy and calculator share it.
- Q02 paraphrase: How does a visitor's request reach the lab calculator? Expected S02 / Route chain and S01 / Shared network: entrypoint → router → service → internal calculator address.
- Q03 relationship: Which service does calc-route select and where does it send traffic? Expected S02 / Relationships and Route chain: calc-service → http://calculator:8000.
- Q04 troubleshooting: Why would adding Docker labels alone not change this lab's route? Expected S03 / Selected provider: file provider is the only scenario configuration source. Do not generalize to all real hosts.
- Q05 unanswerable: What is the lab administrator password? Expected S05 / Access and unknowns: not supplied; acknowledge insufficient evidence, do not invent a password.

For actual runs record returned IDs/ranks or graph paths, selected context, answer, claim support, citation target/location and any failure/change/retest. Compare a keyword baseline with vector retrieval on the same documents/questions. Separate retrieval success from answer support. Latency/cost only when measured; tiny-set outcomes do not establish general performance.
