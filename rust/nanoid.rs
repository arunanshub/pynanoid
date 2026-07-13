use crate::error::Error;
use rand::{Rng, RngCore};

pub fn generate(alphabet: impl AsRef<str>, size: u32) -> Result<String, Error> {
    let alphabet = alphabet.as_ref();
    if alphabet.is_empty() {
        return Err(Error::EmptyAlphabet);
    }
    if size == 0 {
        return Err(Error::ZeroSize);
    }

    // Collect the alphabet once so that symbol lookup is an O(1) index instead
    // of walking the string with `chars().nth()` on every generated symbol.
    let alphabet: Vec<char> = alphabet.chars().collect();
    let alphabet_len = alphabet.len();

    let mask = if alphabet_len <= 1 {
        1
    } else {
        let bits = ((alphabet_len - 1) as f64).ln() / 2.0f64.ln();
        (2usize << bits as usize) - 1
    };
    let step = (1.6 * mask as f64 * size as f64 / alphabet_len as f64).ceil() as usize;

    let mut rng = rand::rng();
    let mut result = String::with_capacity(size as usize);
    // `String::len()` counts bytes, not characters, so track the symbol count
    // separately to stay correct for multi-byte alphabets.
    let mut count = 0usize;
    let mut random_bytes = vec![0u8; step];
    loop {
        rng.fill_bytes(&mut random_bytes);

        for &byte in random_bytes.iter() {
            let index = (byte as usize) & mask;
            if index >= alphabet_len {
                continue;
            }
            result.push(alphabet[index]);
            count += 1;
            if count == size as usize {
                return Ok(result);
            }
        }
    }
}

pub fn non_secure_generate(alphabet: impl AsRef<str>, size: u32) -> Result<String, Error> {
    let alphabet = alphabet.as_ref();
    if alphabet.is_empty() {
        return Err(Error::EmptyAlphabet);
    }
    if size == 0 {
        return Err(Error::ZeroSize);
    }

    let alphabet: Vec<char> = alphabet.chars().collect();
    let alphabet_len = alphabet.len();
    let mut rng = rand::rng();

    let mut result = String::with_capacity(size as usize);
    for _ in 0..size {
        // `random::<f32>()` is in [0, 1), so the index is always < alphabet_len.
        let index = (rng.random::<f32>() * alphabet_len as f32) as usize;
        result.push(alphabet[index.min(alphabet_len - 1)]);
    }
    Ok(result)
}

#[cfg(test)]
mod tests {
    use super::*;
    use proptest::prelude::*;

    #[test]
    fn test_weird_char() {
        let result = generate("¡", 1).unwrap();
        assert_eq!(result.chars().count(), 1);
    }

    #[test]
    fn test_weird_char_non_secure() {
        let result = non_secure_generate("¡", 1).unwrap();
        assert_eq!(result.chars().count(), 1);
    }

    #[test]
    fn test_null_char() {
        let result = generate("\0", 1).unwrap();
        assert_eq!(result.chars().count(), 1);
    }

    #[test]
    fn test_null_char_non_secure() {
        let result = non_secure_generate("\0", 1).unwrap();
        assert_eq!(result.chars().count(), 1);
    }

    #[test]
    fn test_empty_alphabet_errors() {
        assert!(matches!(generate("", 1), Err(Error::EmptyAlphabet)));
        assert!(matches!(
            non_secure_generate("", 1),
            Err(Error::EmptyAlphabet)
        ));
    }

    #[test]
    fn test_zero_size_errors() {
        assert!(matches!(generate("abc", 0), Err(Error::ZeroSize)));
        assert!(matches!(
            non_secure_generate("abc", 0),
            Err(Error::ZeroSize)
        ));
    }

    proptest! {
        #[test]
        fn test_closure(alphabet in ".+", size in 1..5000u32) {
            let result = generate(&alphabet, size).unwrap();
            assert_eq!(result.chars().count(), size as usize);
        }

        #[test]
        fn test_closure_non_secure(alphabet in ".+", size in 1..5000u32) {
            let result = non_secure_generate(&alphabet, size).unwrap();
            assert_eq!(result.chars().count(), size as usize);
        }
    }
}
