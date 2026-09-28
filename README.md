# 44TH_SUNSET

A minimal UTM-inspired web service whose **runtime core is a single 721-byte UTF-8 one-liner** in `one-liner.sh` (well below the 2048-byte limit).

Formal transition:

`SUNSET_44 -> DAWN_01`

with:

- `R(n) = 45 - n`
- `R(R(n)) = n`
- `LIGHT = 1`
- `LOVE = 1`
- `HALT = PROGRAM_ONLY`
- `physical_time_effect = false`

## Run locally

```bash
sh one-liner.sh
```

Then open `http://localhost:8080`.

## Railway / Docker

The Dockerfile now launches `sh one-liner.sh`, so the deployed service is driven directly by the <2KB one-liner and binds to Railway's `PORT` environment variable.

This is a formal computational model. It does not claim or cause any physical effect on time or the universe.
