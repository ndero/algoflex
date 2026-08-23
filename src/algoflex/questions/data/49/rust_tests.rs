fn main() {
    let test_cases = vec![
        ((4, vec![vec![1, 0], vec![1, 2], vec![1, 3]]), vec![1]),
        (
            (
                6,
                vec![vec![3, 0], vec![3, 1], vec![3, 2], vec![3, 4], vec![5, 4]],
            ),
            vec![3, 4],
        ),
        (
            (
                10,
                vec![
                    vec![6, 5],
                    vec![6, 1],
                    vec![1, 4],
                    vec![1, 7],
                    vec![3, 4],
                    vec![7, 0],
                    vec![4, 8],
                    vec![7, 2],
                    vec![2, 9],
                ],
            ),
            vec![1, 7],
        ),
        ((2, vec![vec![0, 1]]), vec![0, 1]),
        (
            (100_001, (0..100_000).map(|i| vec![i, i + 1]).collect()),
            vec![50_000],
        ),
        (
            (1_000, (0..999).map(|i| vec![i, i + 1]).collect()),
            vec![499, 500],
        ),
        // Edge cases
        ((1, vec![]), vec![0]),
        ((3, vec![vec![0, 1], vec![1, 2]]), vec![1]),
        (
            (5, vec![vec![0, 1], vec![1, 2], vec![1, 3], vec![3, 4]]),
            vec![1, 3],
        ),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        find_min_height_trees(input.0, &input.1)
    }));
}
