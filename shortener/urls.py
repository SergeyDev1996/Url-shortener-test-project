from django.urls import path

from shortener.views import ShortenerGet

urlpatterns = [
    path("shorteners/", ShortenerGet.as_view({
        "get": "list"
    }), name="contractor_tender")
]
