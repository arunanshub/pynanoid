"""Python implementation of NanoID.

This is provided in case the compiled version is not available.
"""

from math import ceil, log
from os import urandom
from random import random as _random
from typing import Callable

from .constants import ALPHABET, SIZE


def generate(alphabet: str = ALPHABET, size: int = SIZE) -> str:
    """Generate a NanoID using a secure random number generator.

    Args:
        alphabet: The alphabet to use.
        size: The size of the NanoID.

    Returns:
        str: A NanoID of `size` length.
    """
    return generate_custom(urandom, alphabet, size)


def non_secure_generate(alphabet: str = ALPHABET, size: int = SIZE) -> str:
    """Generate a NanoID using non-secure algorithms.

    Since it does not use a cryptographic random number generator, it is not
    guaranteed to be unique.

    Args:
        alphabet: The alphabet to use.
        size: The size of the NanoID.

    Raises:
        ValueError: raises if alphabet is empty or size is less than 1.

    Returns:
        A NanoID of `size` length.
    """
    if alphabet == "":  # pragma: no cover
        raise ValueError("Alphabet cannot be empty")
    if size < 1:  # pragma: no cover
        raise ValueError("Size cannot be less than 1")

    alphabet_len = len(alphabet)

    id_ = ""
    for _ in range(size):
        id_ += alphabet[int(_random() * alphabet_len) | 0]  # noqa: S311
    return id_


def generate_custom(
    randgen: Callable[[int], bytes],
    alphabet: str = ALPHABET,
    size: int = SIZE,
) -> str:
    """Use a custom random bytes generator to generate a NanoID.

    Args:
        randgen: A function that generates random bytes.
        alphabet: The alphabet to use.
        size: The size of the NanoID.

    Raises:
        ValueError: raises if alphabet is empty or size is less than 1.

    Returns:
        A NanoID of `size` length.
    """
    if alphabet == "":  # pragma: no cover
        raise ValueError("Alphabet cannot be empty")
    if size < 1:  # pragma: no cover
        raise ValueError("Size cannot be less than 1")

    alphabet_len = len(alphabet)

    mask = 1
    if alphabet_len > 1:
        mask = (2 << int(log(alphabet_len - 1) / log(2))) - 1
    step = int(ceil(1.6 * mask * size / alphabet_len))

    id_ = ""
    while True:
        random_bytes = randgen(step)

        for i in range(step):
            random_byte = random_bytes[i] & mask
            if random_byte < alphabet_len:
                id_ += alphabet[random_byte]

                if len(id_) == size:
                    return id_
