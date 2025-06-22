"""Reddit Content Analysis API - FastAPI + Django hybrid application."""

import os
import django
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles

# ==============================================================================
# DJANGO SETUP
# ==============================================================================
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reddit_content_analysis.settings")
django.setup()

from reddit_content_analysis.wsgi import application as django_application

# ==============================================================================
# FASTAPI APP INITIALIZATION
# ==============================================================================
app = FastAPI(
    title="Reddit Content Analysis API",
    description="Reddit analysis and content generation with Django admin integration.",
    version="1.0.0"
)

# ==============================================================================
# ROOT ENDPOINT
# ==============================================================================
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Reddit Content Analysis API",
        "docs": "/docs",
        "admin": "/admin",
        "version": "1.0.0"
    }

# ==============================================================================
# DJANGO INTEGRATION
# ==============================================================================
app.mount("/admin", WSGIMiddleware(django_application))
app.mount("/static", StaticFiles(directory="staticfiles"), name="static")

# ==============================================================================
# API ROUTES
# ==============================================================================
from analyze.routes.analyze import router as analyze_router
from results.routes.results import router as results_router
from generate.routes.generate import router as generate_router

app.include_router(generate_router, prefix="/v1/generate", tags=["Content Generation"])
app.include_router(analyze_router, prefix="/v1/analyze", tags=["Content Analysis"])
app.include_router(results_router, prefix="/v1/results", tags=["Results Management"])

# ==============================================================================
# DEVELOPMENT SERVER
# ==============================================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)