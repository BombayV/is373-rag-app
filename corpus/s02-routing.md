# Lab request route

This is a fictional teaching scenario, not a report about any real server.

## Route chain
In the lab design, the entrypoint websecure receives HTTPS requests. Router calc-route matches the hostname calc.example.test and chooses service calc-service. That service forwards requests to http://calculator:8000 on training-proxy. The hostname is illustrative and not a working public URL.

## Relationships
calc-route uses websecure and selects calc-service. calc-service targets calculator. These relations describe this lab design only.
