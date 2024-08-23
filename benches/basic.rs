fn main() {
    divan::main()
}

#[divan::bench(sample_size = 2000, consts = [23, 50, 100, 200, 300, 500, 1000])]
fn generate<const N: usize>(b: divan::Bencher) {
    let chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-";

    b.with_inputs(|| (chars, N as u32))
        .bench_refs(|(chars, size)| {
            pynanoid::generate(chars, *size).ok();
        });
}

#[divan::bench(sample_size = 2000, consts = [23, 50, 100, 200, 300, 500, 1000])]
fn non_secure_generate<const N: usize>(b: divan::Bencher) {
    let chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-";

    b.with_inputs(|| (chars, N as u32))
        .bench_refs(|(chars, size)| {
            pynanoid::non_secure_generate(chars, *size).ok();
        });
}
