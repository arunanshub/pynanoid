from os import urandom


def algorithm_generate(random_bytes: int) -> bytes:
    return urandom(random_bytes)
