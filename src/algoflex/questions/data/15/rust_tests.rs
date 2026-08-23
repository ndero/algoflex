fn main() {
    let test_cases = vec![
        ((19,), true),
        ((2,), false),
        ((17,), false),
        ((202,), false),
        ((711,), false),
        ((176,), true),
        ((19_345_672,), false),
        ((345_000_000,), false),
        ((1_703_932,), false),
        ((i32::MAX,), false),
        ((1,), true),
        // Edge cases
        ((7,), true),   // Small happy number
        ((10,), true),  // 1² + 0² = 1
        ((100,), true), // 1² + 0² + 0² = 1
        ((4,), false),  // Small unhappy number
    ];

    std::process::exit(run_tests!(&test_cases, |input| is_happy(input.0)));
}
