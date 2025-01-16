import os
import django
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from reddit_content_analysis.wsgi import application as django_application
from fastapi_app.routes import analyze, results, generate

os.environ.setdefault('DJANGO_SETTINGS_MODULE','reddit_content_analysis.settings')
django.setup()

app = FastAPI()

app.mount("/admin", WSGIMiddleware(django_application))

app.include_router(analyze.router)
app.include_router(results.router)
app.include_router(generate.router)








