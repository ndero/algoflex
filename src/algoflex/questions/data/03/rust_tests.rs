fn main() {
    let test_cases = vec![
        (vec![-2, 0, -1], 0),
        (vec![-2, 0, -1].into_iter().cycle().take(3_000).collect(), 0),
        (vec![2, 3, -2, 4], 7),
        (vec![2, 3, -2, 4].repeat(100_000), 700_000),
        (vec![-2], -2),
        ((0..100_000).collect(), 4_999_950_000),
        ([vec![2; 50_000], vec![-2; 50_000]].concat(), 100_000),
        (vec![2, -4, 8, 6, 9, -1, 3, -4, 12], 33),
        (vec![2, -4, 8, 0, 9, -1, 0, -4, 12], 24),
        (vec![2, -4, 8, 0, 9, -1, 0, -4, 12].repeat(10_000), 220_002),
    ];

    std::process::exit(run_tests!(&test_cases, |input| max_sum(input)));
}
