from math import ceil, log
from typing import Callable

from .algorithm import algorithm_generate


def method(
    alphabet: str,
    size: int,
    *,
    algorithm: Callable[[int], bytes] = algorithm_generate,
) -> str:
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
        random_bytes = algorithm(step)

        for i in range(step):
            random_byte = random_bytes[i] & mask
            if random_byte < alphabet_len:
                id_ += alphabet[random_byte]

                if len(id_) == size:
                    return id_
