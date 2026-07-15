---
title: Eleni Syngelaki, Dr.rer.nat.
emoji: 🌸
colorFrom: red
colorTo: pink
sdk: docker
app_port: 7860
pinned: true
---

# Eleni Syngelaki, Dr.rer.nat. — CV & Blog

🌸 Bilingual (English/German) CV and contact site, built as a Streamlit multipage app and served from a Docker image on a [Hugging Face Space](https://huggingface.co/spaces). Every push to `main` rebuilds and redeploys the site via GitHub Actions.

Built from my own [ResumeBlog template](https://github.com/elenamedea/ResumeBlog) — fork that repo if you want a site like this one.

> The YAML block at the top of this file is the [Space configuration](https://huggingface.co/docs/hub/spaces-config-reference); GitHub renders it as a small table, so it does not hurt the repo's README.

---

## Stack

- **App:** Streamlit multipage (EN/DE), content in `utils/context_*.py`
- **Environment:** [uv](https://docs.astral.sh/uv/) — `pyproject.toml` + `uv.lock` are the source of truth
- **Container:** multi-stage Dockerfile, non-root, port 7860
- **Deploy:** GitHub Actions → Hugging Face Docker Space
- **Observability:** [Pydantic Logfire](https://logfire.pydantic.dev/) page-view tracing (active only when `LOGFIRE_TOKEN` is set)

## Local development

- `uv sync` then `uv run streamlit run app.py` — http://localhost:8501
- Docker (dev, hot reload): `docker compose -f docker-compose.dev.yml up --build` — http://localhost:7860
- Docker (production parity): `docker compose -f docker-compose.prod.yml up --build -d`

Copy `.env.example` to `.env` for optional settings; `.env` stays untracked.

## Deployment

The [sync workflow](.github/workflows/sync-to-hf.yml) force-pushes `main` to the Space configured via the repo's Actions settings (secret `HF_TOKEN`, variables `HF_USERNAME` and `HF_SPACE_NAME`); the Space builds the Dockerfile and serves on port 7860.
