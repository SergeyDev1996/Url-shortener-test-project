from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
import requests

from shortener.models import URL


def redirect_view(request, url):
    instance = URL.objects.filter(url=url).first()
    if not instance:
        return HttpResponseNotFound("This URL does not exist.")
    return HttpResponseRedirect(redirect_to=instance.target_url)