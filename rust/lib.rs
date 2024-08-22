mod algo;
mod error;

pub use algo::generate;
use error::Error;
use pyo3::{exceptions as exc, prelude::*};

#[pyfunction]
#[pyo3(name = "method")]
fn pymethod(alphabet: &str, size: u32) -> PyResult<String> {
    let result = algo::generate(alphabet, size).map_err(|e| match e {
        Error::FailedToAllocate => exc::PyMemoryError::new_err(e.to_string()),
        e => exc::PyValueError::new_err(e.to_string()),
    })?;
    Ok(result)
}

#[pymodule]
#[pyo3(name = "_method")]
fn my_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(pymethod, m)?)?;
    Ok(())
}
