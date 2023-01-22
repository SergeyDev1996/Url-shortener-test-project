import datetime
import secrets

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from shortener.models import URL
from shortener.serializers import ShortenerSerializer, ShortenerGetSerializer


class ShortenerPostView(viewsets.ModelViewSet):
    serializer_class = ShortenerSerializer


class ShortenerRetrieveView(viewsets.ModelViewSet):
    serializer_class = ShortenerGetSerializer
    queryset = URL.objects.all()

    def get_queryset(self):
        time_now = datetime.datetime.now()
        return URL.objects.filter(expiry__lt=time_now).delete()

    def get_object(self):
        self.get_queryset()
        url = self.kwargs.get("url")
        obj = URL.objects.filter(url=url).first()
        if not obj:
            raise Http404
        return obj
