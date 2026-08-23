fn main() {
    let test_cases = vec![
        (10, 4),
        (15, 6),
        (5, 2),
        (55, 60),
        (1_000, 142_511),
        (10_000, 134_235_101),
        // Edge cases
        (0, 1),
        (1, 1),
        (2, 1),
        (4, 1),
        (25, 13),
    ];

    std::process::exit(run_tests!(&test_cases, |input| count_ways(*input)));
}
