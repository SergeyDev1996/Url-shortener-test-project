import datetime
from functools import partial
from typing import OrderedDict

from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from shortener.methods import generate_random_url
from shortener.models import URL
import validators


class ShortenerSerializer(serializers.ModelSerializer):

    url = serializers.CharField(default=partial(generate_random_url))

    def validate(self, attrs: OrderedDict) -> OrderedDict:
        if not validators.url(
            target_url := attrs.get(
                "target_url"
            )
        ):
            raise ValidationError("The URL you provided is not valid.")
        max_expire = timezone.now() + datetime.timedelta(days=365)
        min_expire = timezone.now() + datetime.timedelta(days=1)
        expiration = attrs.get("expiry")
        if expiration:
            if expiration < timezone.now():
                raise ValidationError({"expiry": "The expiration time"
                                                 " can not be in the past."})
            if expiration > max_expire or \
                    expiration < min_expire:
                raise ValidationError({"expiry": "The maximum expiration time"
                                                 " for the link is 1 year,"
                                                 " the minimum - 1 day."})

        return attrs

    class Meta:
        model = URL
        read_only_fields = (
            "url",
                            )
        fields = read_only_fields + (
            "target_url",
            "expiry",
            "creation_time"
        )


class ShortenerGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = URL
        fields = (
            "target_url",
            "expiry"
                  )
