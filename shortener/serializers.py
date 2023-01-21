import secrets
from functools import partial
from typing import OrderedDict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField

from shortener.models import URL
import validators


class ShortenerSerializer(serializers.ModelSerializer):

    def generate_key():
        key = "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(5))
        return key

    def generate_secret_key():
        secret_key = "".join(secrets.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(8))
        return secret_key

    key = serializers.CharField(default=partial(generate_key))
    secret_key = serializers.CharField(default=partial(generate_secret_key))
    url = serializers.CharField(default=partial(generate_key))

    def validate(self, attrs: OrderedDict) -> OrderedDict:
        if not validators.url(
            target_url := attrs.get(
                "target_url"
            )
        ):
           raise ValidationError("The URL you provided is not valid")
        return attrs

    class Meta:
        model = URL
        read_only_fields = ("clicks", "is_active", "url")
        fields = read_only_fields + (
            "target_url",
            "key",
            "secret_key",
            # "admin_url"
        )