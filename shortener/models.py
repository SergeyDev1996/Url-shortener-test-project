from django.db import models


class URLBase(models.Model):
    target_url = models.CharField(max_length=400)