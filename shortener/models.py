from django.db import models

from shortener.methods import now_plus_90


class URL(models.Model):
    target_url = models.CharField(max_length=400)
    url = models.CharField(max_length=400)
    creation_time = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(default=now_plus_90)
