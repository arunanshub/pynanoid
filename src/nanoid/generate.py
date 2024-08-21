from .algorithm import algorithm_generate
from .method import method
from .resources import ALPHABET, SIZE


def generate(alphabet: str = ALPHABET, size: int = SIZE):
    return method(algorithm_generate, alphabet, size)
