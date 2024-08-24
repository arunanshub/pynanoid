from .constants import ALPHABET, SIZE
from .nanoid import generate_custom

try:
    # prioritize using the compiled versions if available
    from ._pynanoid import generate, non_secure_generate
except ImportError:  # pragma: no cover
    from .nanoid import generate, non_secure_generate


__all__ = [
    "generate",
    "non_secure_generate",
    "generate_custom",
    "ALPHABET",
    "SIZE",
]
