import secrets
from datetime import datetime, timedelta


def generate_random_url():
    key = "".join(secrets.choice("ABCDEFGHIJKL"
                                 "MNOPQRSTUVWXYZ") for _ in range(5))
    return key


def now_plus_90():
    return datetime.now() + timedelta(days=90)

