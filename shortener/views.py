import secrets

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from shortener.models import URL
from shortener.serializers import ShortenerSerializer


class ShortenerGetPostView(viewsets.ModelViewSet):
    serializer_class = ShortenerSerializer
    queryset = URL.objects.all()
    # if not validators.url(url.target_url):
    #     raise_bad_request(message="Your provided URL is not valid")

    # chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # key = "".join(secrets.choice(chars) for _ in range(5))
    # secret_key = "".join(secrets.choice(chars) for _ in range(8))
