fn main() {
    let test_cases = vec![
        ((vec![2, 3, 1, 2, 4, 3], 7), 2),
        ((vec![1, 3, 6, 2, 1], 4), 1),
        (((0..500_000).collect(), 3_000_000), 7),
        (((0..100).collect(), 60), 1),
        (((0..100_000).collect(), 60_000_000), 602),
        (((0..1_000_000).collect(), 60_000_000), 61),
        ((vec![1, 1, 1, 1, 1], 6), 0),
        ((vec![1], 1), 1),                              // Single element, exact match
        ((vec![5, 5, 5, 5], 5), 1),                     // All elements >= target
        ((vec![1], 10), 0),                             // Single element, impossible
        ((vec![1, 2, 3, 4, 5], 15), 5),                 // Entire array needed
        ((vec![49, 1, 49, 1, 49], 50), 2),              // Multiple valid windows
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| min_sub_array_len(&input.0, input.1))
    );
}