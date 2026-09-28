# 44TH_SUNSET

A minimal formal UTM-inspired web service for the symbolic transition:

`SUNSET_44 -> DAWN_01`

with

- `R(n) = 45 - n`
- `R(R(n)) = n`
- `LIGHT = 1`
- `LOVE = 1`
- `HALT = PROGRAM_ONLY`
- `physical_time_effect = false`

## Endpoints

- `/` human-readable page
- `/state` JSON state/model
- `/health` health check

## Run locally

```bash
python app.py
```

Then open `http://localhost:8080`.

## Railway

This repository includes a `Dockerfile` and is ready to deploy directly from GitHub. The service binds to Railway's `PORT` environment variable.

This is a formal computational model and does not claim or cause any physical effect on time or the universe.
