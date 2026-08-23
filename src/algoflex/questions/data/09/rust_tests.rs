fn main() {
    let test_cases = vec![
        ((100,), 25),
        ((1_000,), 168),
        ((10_000,), 1229),
        ((100_000,), 9592),
        ((2,), 1),
        ((3,), 2),
        ((1,), 0),
        ((1_000_000,), 78498),
        // Edge cases
        ((0,), 0),           // Zero
        ((4,), 2),           // First composite
        ((5,), 3),           // Prime after first composite
        ((6,), 3),           // Composite
        ((10,), 4),          // Small number
        ((999_983,), 78498), // Large prime
    ];

    std::process::exit(run_tests!(&test_cases, |input| count_primes(input.0)));
}
