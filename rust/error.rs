use std::string::FromUtf8Error;

#[derive(Debug, thiserror::Error)]
pub enum Error {
    #[error("Failed to get random bytes")]
    FailedToAllocate,

    #[error("alphabet cannot be empty")]
    EmptyAlphabet,

    #[error("size cannot be zero")]
    ZeroSize,

    #[error("string is not UTF-8")]
    NotUtf8(#[from] FromUtf8Error),
}
