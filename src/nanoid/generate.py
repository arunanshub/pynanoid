try:
    # try to load the optimized cython version
    from ._method import method  # type: ignore[import-untyped]
except ImportError:  # pragma: no cover
    from .method import method
from .resources import ALPHABET, SIZE


def generate(alphabet: str = ALPHABET, size: int = SIZE) -> str:
    return method(alphabet, size)
