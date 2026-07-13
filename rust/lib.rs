mod error;
mod nanoid;

pub use nanoid::{generate, non_secure_generate};
use pyo3::{exceptions as exc, prelude::*};

/// Generate a NanoID using a secure random number generator.
///
/// Args:
///     alphabet: The alphabet to use.
///     size: The size of the NanoID.
///
/// Raises:
///     ValueError: raises if alphabet is empty or size is less than 1.
///
/// Returns:
///     str: A NanoID of `size` length.
#[pyfunction]
#[pyo3(name = "generate")]
#[pyo3(signature = (
    alphabet = "_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    size = 21,
))]
fn pygenerate(alphabet: &str, size: u32) -> PyResult<String> {
    generate(alphabet, size).map_err(|e| exc::PyValueError::new_err(e.to_string()))
}

/// Generate a NanoID using non-secure algorithms.
///
/// Since it does not use a cryptographic random number generator, it is not
/// guaranteed to be unique.
///
/// Args:
///     alphabet: The alphabet to use.
///     size: The size of the NanoID.
///
/// Raises:
///     ValueError: raises if alphabet is empty or size is less than 1.
///
/// Returns:
///     A NanoID of `size` length.
#[pyfunction]
#[pyo3(name = "non_secure_generate")]
#[pyo3(signature = (
    alphabet = "_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    size = 21,
))]
fn py_non_secure_generate(alphabet: &str, size: u32) -> PyResult<String> {
    non_secure_generate(alphabet, size).map_err(|e| exc::PyValueError::new_err(e.to_string()))
}

#[pymodule]
#[pyo3(name = "_pynanoid")]
fn my_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(pygenerate, m)?)?;
    m.add_function(wrap_pyfunction!(py_non_secure_generate, m)?)?;
    Ok(())
}
