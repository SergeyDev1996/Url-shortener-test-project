from django.urls import path

from shortener.views import ShortenerPostView, ShortenerRetrieveView

urlpatterns = [
    path("shorteners/", ShortenerPostView.as_view({
        "post": "create"
    }), name="create_link"),
    path("shortener/<str:url>/", ShortenerRetrieveView.as_view(
        {
            "get": "retrieve"
        }
    ), name="retrieve_link")
]
