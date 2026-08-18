fn main() {
    let test_cases = vec![
        (
            vec![vec![1, 2, 3], vec![2, 3, 4]],
            [1, 4].into_iter().collect(),
        ),
        (
            vec![vec![1, 2, 3, 3, 2]],
            [1, 2, 3].into_iter().collect(),
        ),
        (
            vec![
                vec![1],
                vec![2],
                vec![3],
                vec![4],
                vec![5],
                vec![6],
            ],
            [1, 2, 3, 4, 5, 6].into_iter().collect(),
        ),
        (
            vec![
                vec![1, 2],
                vec![2, 3],
                vec![3, 4],
                vec![4, 5],
                vec![5, 6],
                vec![6, 7],
            ],
            [1, 7].into_iter().collect(),
        ),
        (
            vec![vec![1, 2, 4, 4], vec![0, 1, 6], vec![0, 1]],
            [2, 4, 6].into_iter().collect(),
        ),
        (
            vec![
                vec![0],
                vec![1],
                vec![2],
                vec![3],
                vec![4],
                vec![5],
            ],
            [0, 1, 2, 3, 4, 5].into_iter().collect(),
        ),
        (
            vec![vec![-1], vec![], vec![], vec![0], vec![1]],
            [-1, 0, 1].into_iter().collect(),
        ),
        (
            vec![
                vec![9, -4, 8, 3, 12, 0, -4, 8],
                vec![3, 3, 8, 6, 7, 10],
                vec![11, 12, 10, 13],
                vec![5, 15, 3],
                vec![11, 15, 11, 11, 6, -2],
            ],
            [9, -4, 0, 7, 13, 5, -2].into_iter().collect(),
        ),
        (
            vec![vec![2; 50_000], vec![-2; 50_000]],
            [2, -2].into_iter().collect(),
        ),
        (
            vec![(0..100_000).collect(), (0..100_000).collect()],
            std::collections::HashSet::new(),
        ),
        (
            vec![
                (0..100_000).collect(),
                (10..100_000).collect(),
            ],
            (0..10).collect(),
        ),
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| exclusive_union(input))
    );
}