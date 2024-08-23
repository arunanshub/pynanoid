import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from pynanoid._method import method as rust_method
from pynanoid.method import method as python_method
from pynanoid.resources import ALPHABET, SIZE


@pytest.mark.parametrize("size", [SIZE])
def test_rust_method(benchmark: BenchmarkFixture, size: int):
    benchmark(rust_method, ALPHABET, size)


@pytest.mark.parametrize("size", [SIZE])
def test_python_method(benchmark: BenchmarkFixture, size: int):
    benchmark(python_method, ALPHABET, size)
