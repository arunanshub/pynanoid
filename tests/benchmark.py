import pytest
from pytest_benchmark.fixture import (  # type: ignore[import-untyped]
    BenchmarkFixture,
)

from pynanoid import (
    generate as rust_generate,
)
from pynanoid import (
    non_secure_generate as rust_non_secure_generate,
)
from pynanoid.constants import ALPHABET
from pynanoid.nanoid import (
    generate as python_generate,
)
from pynanoid.nanoid import (
    non_secure_generate as python_non_secure_generate,
)


@pytest.mark.parametrize("size", [300])
def test_rust_generate(benchmark: BenchmarkFixture, size: int):
    benchmark(rust_generate, ALPHABET, size)


@pytest.mark.parametrize("size", [300])
def test_python_generate(benchmark: BenchmarkFixture, size: int):
    benchmark(python_generate, ALPHABET, size)


@pytest.mark.parametrize("size", [300])
def test_rust_non_secure_generate(benchmark: BenchmarkFixture, size: int):
    benchmark(rust_non_secure_generate, ALPHABET, size)


@pytest.mark.parametrize("size", [300])
def test_python_non_secure_generate(benchmark: BenchmarkFixture, size: int):
    benchmark(python_non_secure_generate, ALPHABET, size)
