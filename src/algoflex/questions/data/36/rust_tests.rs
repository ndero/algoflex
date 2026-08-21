fn main() {
    let test_cases = vec![
        ((vec![2, 4, 8, 9, 12, 13, 16, 18], 18), true),
        (((0..5_000_000).collect::<Vec<_>>(), 45), true),
        (((0..5_000_000).collect::<Vec<_>>(), 5_000_000), false),
        (((-1_000_000..1_000_000).collect::<Vec<_>>(), 0), true),
        (((-1_000_000..1_000_000).collect::<Vec<_>>(), -223), true),
        (((-1_000_000..1_000_000).step_by(10).collect::<Vec<_>>(), 33), false),
        ((vec![], 1), false),
        ((vec![5], 5), true),
        ((vec![5], 4), false),
        ((vec![1, 2], 1), true),
        ((vec![1, 2], 2), true),
        ((vec![1, 2], 3), false),
        ((vec![-5, -2, 0, 3, 7], -5), true),
        ((vec![-5, -2, 0, 3, 7], 6), false),
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| binary_search(&input.0, input.1))
    );
}