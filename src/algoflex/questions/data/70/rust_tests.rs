fn main() {
    let test_cases = vec![
        // Empty
        ((vec![], 1), vec![-1, -1]),
        // Single element
        ((vec![1], 1), vec![0, 0]),
        ((vec![1], 0), vec![-1, -1]),
        // Two elements
        ((vec![1, 2], 1), vec![0, 0]),
        ((vec![1, 2], 2), vec![1, 1]),
        ((vec![1, 2], 3), vec![-1, -1]),
        // All same
        ((vec![2, 2, 2, 2], 2), vec![0, 3]),
        ((vec![2, 2, 2, 2], 3), vec![-1, -1]),
        // Basic examples
        ((vec![5, 7, 7, 8, 8, 10], 8), vec![3, 4]),
        ((vec![5, 7, 7, 8, 8, 10], 6), vec![-1, -1]),
        // Target at beginning
        ((vec![1, 1, 2, 3, 4], 1), vec![0, 1]),
        ((vec![1, 2, 3, 4], 1), vec![0, 0]),
        // Target at end
        ((vec![1, 2, 3, 4, 4], 4), vec![3, 4]),
        ((vec![1, 2, 3, 4], 4), vec![3, 3]),
        // Middle large block
        ((vec![1, 2, 3, 3, 3, 3, 4, 5], 3), vec![2, 5]),
        // No occurrence
        ((vec![1, 3, 5, 7], 4), vec![-1, -1]),
        // Negative numbers
        ((vec![-5, -4, -4, -4, -3, -1], -4), vec![1, 3]),
        ((vec![-5, -4, -4, -4, -3, -1], -2), vec![-1, -1]),
        // Mixed negative and positive
        ((vec![-10, -5, 0, 0, 0, 5, 10], 0), vec![2, 4]),
        ((vec![-10, -5, 0, 0, 0, 5, 10], -10), vec![0, 0]),
        // Extreme values
        (
            (vec![-1_000_000_000, 0, 1_000_000_000], -1_000_000_000),
            vec![0, 0],
        ),
        (
            (vec![-1_000_000_000, 0, 1_000_000_000], 1_000_000_000),
            vec![2, 2],
        ),
        ((vec![-1_000_000_000, 0, 1_000_000_000], 1), vec![-1, -1]),
        // Large duplicate block
        ((vec![1; 1_000], 1), vec![0, 999]),
        ((vec![1; 1_000], 2), vec![-1, -1]),
        // Increasing sequence
        (((0..1_000).collect(), 500), vec![500, 500]),
        (((0..1_000).collect(), 1_001), vec![-1, -1]),
        // Large middle block
        (
            (
                (0..500)
                    .chain(std::iter::repeat_n(500, 1_000))
                    .chain(501..1_000)
                    .collect(),
                500,
            ),
            vec![500, 1_499],
        ),
        // Stress near 10^5
        (
            (
                std::iter::repeat_n(1, 50_000)
                    .chain(std::iter::repeat_n(2, 50_000))
                    .collect(),
                2,
            ),
            vec![50_000, 99_999],
        ),
        (
            (
                std::iter::repeat_n(1, 50_000)
                    .chain(std::iter::repeat_n(2, 50_000))
                    .collect(),
                1,
            ),
            vec![0, 49_999],
        ),
        // Target outside range
        ((vec![5, 6, 7, 8], 1), vec![-1, -1]),
        ((vec![5, 6, 7, 8], 10), vec![-1, -1]),
        // Small duplicate blocks
        ((vec![1, 1, 2, 2, 3, 3, 4, 4], 3), vec![4, 5]),
        // Large sparse
        (
            ((0..200_000).step_by(2).collect(), 100_000),
            vec![50_000, 50_000],
        ),
        (((0..200_000).step_by(2).collect(), 99_999), vec![-1, -1]),
        // Single large block in center
        (
            (
                std::iter::repeat_n(0, 10_000)
                    .chain(std::iter::repeat_n(1, 80_000))
                    .chain(std::iter::repeat_n(2, 10_000))
                    .collect(),
                1,
            ),
            vec![10_000, 89_999],
        ),
        // Edge binary-search traps
        ((vec![2, 2, 2, 3, 4, 5], 2), vec![0, 2]),
        ((vec![1, 2, 3, 4, 4, 4], 4), vec![3, 5]),
        // Very large values
        (
            (vec![1_000_000_000; 100_000], 1_000_000_000),
            vec![0, 99_999],
        ),
        // Additional edge cases
        ((vec![0, 0], 0), vec![0, 1]),
        ((vec![-1, -1, 0, 0, 1, 1], -1), vec![0, 1]),
        ((vec![-1, -1, 0, 0, 1, 1], 1), vec![4, 5]),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        first_last(&input.0, input.1)
    }));
}
