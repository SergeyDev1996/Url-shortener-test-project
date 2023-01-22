import secrets


def generate_random_url():
    key = "".join(secrets.choice("ABCDEFGHIJKL"
                                 "MNOPQRSTUVWXYZ") for _ in range(5))
    return key
