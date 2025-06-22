"""reddit_content_analysis URL Configuration

This file routes Django admin URLs to the correct views. When Django is mounted at
`/admin` using FastAPI's WSGIMiddleware, this file ensures the admin dashboard is
served directly under `/admin`.

For more info: https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Serve Django admin at root when mounted at /admin in FastAPI
    path("", admin.site.urls),
]

# Serve static files during development (e.g., admin CSS)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
