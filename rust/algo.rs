use crate::error::Error;

#[inline(always)]
fn get_random_bytes(buffer: &mut [u8]) -> Result<(), Error> {
    getrandom::getrandom(buffer).map_err(|_| Error::FailedToAllocate)?;
    Ok(())
}

pub fn generate(alphabet: impl AsRef<str>, size: u32) -> Result<String, Error> {
    let alphabet = alphabet.as_ref();
    if alphabet.is_empty() {
        return Err(Error::EmptyAlphabet);
    }
    if size == 0 {
        return Err(Error::ZeroSize);
    }
    let alphabet_len = alphabet.chars().count();

    let mask = if alphabet_len <= 1 {
        1
    } else {
        let x = (alphabet_len as f32 - 1.0).ln() / 2.0f32.ln();
        (2 << x as u32) - 1
    };
    let step = (1.6 * mask as f32 * size as f32 / alphabet_len as f32).ceil() as usize;

    let mut result = Vec::with_capacity(size as usize);
    let mut random_bytes = vec![0; step];
    loop {
        get_random_bytes(&mut random_bytes)?;

        for each in random_bytes.iter() {
            let random_byte = each & mask;
            if (random_byte as usize) >= alphabet_len {
                continue;
            }
            if let Some(c) = alphabet.chars().nth(random_byte as usize) {
                result.push(c);
                if result.len() == size as usize {
                    return Ok(result.into_iter().collect());
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use proptest::prelude::*;

    #[test]
    fn test_method() {
        let result = generate("abcdefghijklmnopqrstuvwxyz", 10).unwrap();
        assert_eq!(result.len(), 10);
    }

    #[test]
    fn test_weird_char() {
        let result = generate("¡", 1).unwrap();
        assert_eq!(result.chars().count(), 1);
    }

    #[test]
    fn test_null_char() {
        let result = generate("\0", 1).unwrap();
        assert_eq!(result.chars().count(), 1);
    }

    proptest! {
        #[test]
        fn test_closure(alphabet in ".+", size in 1..5000u32) {
            let result = generate(&alphabet, size).unwrap();
            assert_eq!(result.chars().count(), size as usize);
        }
    }
}
