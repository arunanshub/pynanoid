from os import urandom


def algorithm_generate(random_bytes: int) -> bytearray:
    return bytearray(urandom(random_bytes))
