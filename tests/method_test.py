from hypothesis import given
from hypothesis import strategies as st

from pynanoid import generate
from pynanoid.constants import SIZE
from pynanoid.nanoid import generate_custom


def test_generates_random_string():
    sequence = [2, 255, 3, 7, 7, 7, 7, 7, 0, 1]

    def rand(size: int = SIZE) -> bytes:
        random_bytes = []
        for i in range(0, size, len(sequence)):
            random_bytes += sequence[0 : size - i]
        return bytes(random_bytes)

    assert generate_custom(rand, "abcde", 4) == "cdac"


@given(st.text(min_size=1), st.integers(min_value=1, max_value=5000))
def test_same_size(alphabet: str, size: int):
    assert len(generate(alphabet, size)) == size
