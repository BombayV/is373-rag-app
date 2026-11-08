# Chunk boundary experiment

Executed locally by AI on November 8, 2026 against synthetic S02. Unit: Python Unicode characters, not tokens. No embeddings, database or RAG answers generated.

Source length: 557 characters. Heading-aware split: 3 units. Fixed-length split: 4 units of at most 160 characters; overlap 0.

## Heading-aware output

### S02-H1

```text
# Lab request route

This is a fictional teaching scenario, not a report about any real server.
```

### S02-H2

```text
## Route chain
In the lab design, the entrypoint websecure receives HTTPS requests. Router calc-route matches the hostname calc.example.test and chooses service calc-service. That service forwards requests to http://calculator:8000 on training-proxy. The hostname is illustrative and not a working public URL.
```

### S02-H3

```text
## Relationships
calc-route uses websecure and selects calc-service. calc-service targets calculator. These relations describe this lab design only.
```

## Fixed-length output

### S02-F1 — character offsets [0, 160)

```text
# Lab request route

This is a fictional teaching scenario, not a report about any real server.

## Route chain
In the lab design, the entrypoint websecure rece
```

### S02-F2 — character offsets [160, 320)

```text
ives HTTPS requests. Router calc-route matches the hostname calc.example.test and chooses service calc-service. That service forwards requests to http://calcula
```

### S02-F3 — character offsets [320, 480)

```text
tor:8000 on training-proxy. The hostname is illustrative and not a working public URL.

## Relationships
calc-route uses websecure and selects calc-service. cal
```

### S02-F4 — character offsets [480, 557)

```text
c-service targets calculator. These relations describe this lab design only.

```

## Observation and proposed decision

Fixed offsets cut prose without regard to sentence/relationship boundaries; inspect adjacent F units to reconstruct context. Heading-aware units retain the Route chain and Relationships sections separately. Prefer section-aware units for these tiny fixtures, carrying source ID and section metadata; add bounded splitting only for long sections. This is a boundary inspection, not measured retrieval superiority.
