from nanoid.method import method
from nanoid.resources import SIZE


def test_generates_random_string():
    sequence = [2, 255, 3, 7, 7, 7, 7, 7, 0, 1]

    def rand(size=SIZE):
        random_bytes = []
        for i in range(0, size, len(sequence)):
            random_bytes += sequence[0 : size - i]
        return random_bytes

    assert method("abcde", 4, algorithm=rand) == "cdac"  # type: ignore
