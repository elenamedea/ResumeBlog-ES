# Eleni Syngelaki, Dr.rer.nat. — CV & Blog

**Live site: [resumeblog-es.onrender.com](https://resumeblog-es.onrender.com/)**

🌸 Bilingual (English/German) CV and contact site, built as a Streamlit multipage app and served from a Docker image on [Render](https://render.com). Every push to `main` rebuilds and redeploys the site.

Built from my own [ResumeBlog template](https://github.com/elenamedea/ResumeBlog) — fork that repo if you want a site like this one.

---

## Stack

- **App:** Streamlit multipage (EN/DE), content in `utils/context_*.py`
- **Environment:** [uv](https://docs.astral.sh/uv/) — `pyproject.toml` + `uv.lock` are the source of truth
- **Container:** multi-stage Dockerfile, non-root, port 7860
- **Deploy:** Render Docker web service, defined in [`render.yaml`](render.yaml), auto-deploy on push to `main`
- **Observability:** [Pydantic Logfire](https://logfire.pydantic.dev/) page-view tracing (active only when `LOGFIRE_TOKEN` is set)

## Local development

- `uv sync` then `uv run streamlit run app.py` — http://localhost:8501
- Docker (dev, hot reload): `docker compose -f docker-compose.dev.yml up --build` — http://localhost:7860
- Docker (production parity): `docker compose -f docker-compose.prod.yml up --build -d`

Copy `.env.example` to `.env` for optional settings; `.env` stays untracked.

## Deployment

[`render.yaml`](render.yaml) defines the service as a blueprint: Docker runtime, free plan, health-checked on `/_stcore/health`. Render builds the repo's Dockerfile and redeploys on every push to `main`. The optional `LOGFIRE_TOKEN` environment variable is set in the Render dashboard, never in the repo.

Note: free-plan instances spin down after ~15 minutes without traffic; the next visitor triggers a cold start (~30–60 s).
