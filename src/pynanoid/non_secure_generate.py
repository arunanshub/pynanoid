from random import random

from .resources import ALPHABET, SIZE


def non_secure_generate(alphabet: str = ALPHABET, size: int = SIZE) -> str:
    alphabet_len = len(alphabet)

    id_ = ""
    for _ in range(size):
        id_ += alphabet[int(random() * alphabet_len) | 0]  # noqa: S311
    return id_
