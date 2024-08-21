from random import random

from .resources import ALPHABET, SIZE


def non_secure_generate(alphabet: str = ALPHABET, size: int = SIZE):
    alphabet_len = len(alphabet)

    id = ""
    for _ in range(size):
        id += alphabet[int(random() * alphabet_len) | 0]
    return id
