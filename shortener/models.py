from django.db import models


class URL(models.Model):
    key = models.CharField(unique=True, max_length=255)
    secret_key = models.CharField(unique=True, max_length=255)
    target_url = models.CharField(max_length=400)
    is_active = models.BooleanField(default=True)
    clicks = models.IntegerField(default=0)
    url = models.CharField(max_length=400)