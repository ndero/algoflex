fn main() {
    let test_cases = vec![
        ((64,), true),
        ((20,), false),
        ((1024,), true),
        ((2,), true),
        ((0,), false),
        ((1267650600228229401496703205376_i128,), true),
        ((1267650600228229401496703205377_i128,), false),
        ((-64,), false),
        // Edge cases
        ((1,), true),          // 2^0
        ((-2,), false),        // Negative power of 2
        ((i128::MAX,), false), // Large non-power of 2
    ];

    std::process::exit(run_tests!(&test_cases, |input| is_power_of_two(input.0)));
}
