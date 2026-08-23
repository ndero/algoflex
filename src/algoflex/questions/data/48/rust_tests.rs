fn main() {
    let test_cases = vec![
        ((2, vec![vec![1, 0], vec![0, 1]]), vec![]),
        (
            (4, vec![vec![1, 0], vec![2, 0], vec![3, 1], vec![3, 2]]),
            vec![0, 1, 2, 3],
        ),
        ((1, vec![]), vec![0]),
        ((10, vec![vec![0, 9]]), vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
        (
            (10, vec![vec![0, 9], vec![8, 5]]),
            vec![1, 2, 3, 4, 5, 6, 7, 9, 8, 0],
        ),
        ((10, vec![vec![0, 9], vec![8, 5], vec![5, 8]]), vec![]),
        (
            (10, vec![vec![2, 3], vec![2, 4], vec![4, 3]]),
            vec![0, 1, 3, 5, 6, 7, 8, 9, 4, 2],
        ),
        // Edge cases
        ((0, vec![]), vec![]),
        ((2, vec![]), vec![0, 1]),
        ((3, vec![vec![1, 0], vec![2, 1]]), vec![0, 1, 2]),
        (
            (
                4,
                vec![vec![1, 0], vec![2, 0], vec![3, 1], vec![3, 2], vec![2, 3]],
            ),
            vec![],
        ),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        find_order(input.0, &input.1)
    }));
}
