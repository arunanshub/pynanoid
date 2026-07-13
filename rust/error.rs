#[derive(Debug, thiserror::Error)]
pub enum Error {
    #[error("alphabet cannot be empty")]
    EmptyAlphabet,

    #[error("size cannot be zero")]
    ZeroSize,
}
