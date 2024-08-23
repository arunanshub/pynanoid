from hypothesis import given
from hypothesis import strategies as st

from nanoid.method import method
from nanoid.resources import SIZE


def test_generates_random_string():
    sequence = [2, 255, 3, 7, 7, 7, 7, 7, 0, 1]

    def rand(size: int = SIZE) -> bytes:
        random_bytes = []
        for i in range(0, size, len(sequence)):
            random_bytes += sequence[0 : size - i]
        return bytes(random_bytes)

    assert method("abcde", 4, algorithm=rand) == "cdac"


@given(st.text(min_size=1), st.integers(min_value=1, max_value=5000))
def test_same_size(alphabet: str, size: int):
    assert len(method(alphabet, size)) == size
