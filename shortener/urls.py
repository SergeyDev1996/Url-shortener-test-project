from django.urls import path

from shortener.views import ShortenerGetPostView

urlpatterns = [
    path("shorteners/", ShortenerGetPostView.as_view({
        "get": "list", "post": "create"
    }), name="contractor_tender")
]
