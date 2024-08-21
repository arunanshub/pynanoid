from .method import method
from .resources import ALPHABET, SIZE


def generate(alphabet: str = ALPHABET, size: int = SIZE) -> str:
    return method(alphabet, size)
