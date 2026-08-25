fn main() {
    let test_cases = vec![
        // ===== Minimal Cases =====
        ((vec![vec![[1, 2]]]), vec![]),
        (vec![vec![[1, 2]], vec![[3, 4]]], vec![[2, 3]]),
        (vec![vec![[1, 3]], vec![[2, 4]]], vec![]),
        (vec![vec![[1, 5]], vec![[2, 3]]], vec![]),
        // ===== Simple Gaps =====
        (
            vec![vec![[1, 2], [5, 6]], vec![[1, 3]], vec![[4, 10]]],
            vec![[3, 4]],
        ),
        (
            vec![vec![[1, 3], [6, 7]], vec![[2, 4]], vec![[2, 5], [9, 12]]],
            vec![[5, 6], [7, 9]],
        ),
        (
            vec![vec![[1, 3], [6, 9]], vec![[2, 5]], vec![[5, 7]]],
            vec![],
        ),
        (vec![vec![[1, 2], [3, 4]], vec![[2, 3]]], vec![]),
        // ===== Touching Boundaries =====
        (vec![vec![[1, 2]], vec![[2, 3]], vec![[3, 4]]], vec![]),
        (vec![vec![[1, 2], [3, 5]], vec![[2, 3]]], vec![]),
        (vec![vec![[1, 2], [5, 6]], vec![[2, 5]]], vec![]),
        // ===== Multiple Free Slots =====
        (
            vec![
                vec![[1, 2], [5, 6], [9, 10]],
                vec![[2, 3], [6, 7]],
                vec![[3, 5], [7, 9]],
            ],
            vec![],
        ),
        (
            vec![
                vec![[1, 2], [4, 5], [7, 8]],
                vec![[2, 3], [5, 6]],
                vec![[3, 4], [6, 7]],
            ],
            vec![],
        ),
        // ===== One Large Gap =====
        (vec![vec![[1, 2]], vec![[5, 6]]], vec![[2, 5]]),
        (vec![vec![[1, 3]], vec![[6, 8]], vec![[2, 4]]], vec![[4, 6]]),
        // ===== Nested Intervals =====
        (
            vec![vec![[1, 10]], vec![[2, 3]], vec![[4, 5]], vec![[6, 7]]],
            vec![],
        ),
        (
            vec![vec![[1, 4], [6, 10]], vec![[2, 3], [5, 7]]],
            vec![[4, 5]],
        ),
        // ===== Staggered Intervals =====
        (
            vec![vec![[1, 4], [7, 9]], vec![[2, 5]], vec![[3, 6]]],
            vec![[6, 7]],
        ),
        (
            vec![vec![[1, 3], [8, 10]], vec![[2, 6]], vec![[4, 7]]],
            vec![[7, 8]],
        ),
        // ===== Multiple Employees =====
        (vec![vec![[1, 2]], vec![[1, 2]], vec![[1, 2]]], vec![]),
        (
            vec![vec![[1, 2], [4, 6]], vec![[2, 4]], vec![[6, 8]]],
            vec![],
        ),
        (
            vec![vec![[1, 3], [6, 8]], vec![[2, 4], [7, 9]], vec![[5, 6]]],
            vec![[4, 5]],
        ),
        // ===== Large Gap In Middle =====
        (
            vec![
                vec![[1, 2], [10, 12]],
                vec![[2, 3], [8, 9]],
                vec![[3, 4], [6, 7]],
            ],
            vec![[4, 6], [7, 8], [9, 10]],
        ),
        // ===== Edge Time Distribution =====
        (
            vec![vec![[0, 1], [3, 4]], vec![[1, 2]], vec![[2, 3]]],
            vec![],
        ),
        (vec![vec![[0, 2], [5, 7]], vec![[2, 5]]], vec![]),
        // ===== Complex Overlaps =====
        (
            vec![
                vec![[1, 5], [10, 14]],
                vec![[2, 6], [8, 10]],
                vec![[3, 4], [7, 8]],
            ],
            vec![[6, 7]],
        ),
        (
            vec![vec![[1, 3], [9, 12]], vec![[2, 4], [6, 8]], vec![[5, 6]]],
            vec![[4, 5], [8, 9]],
        ),
        // ===== Large Values =====
        (
            vec![vec![[1, 1_000_000]], vec![[2_000_000, 3_000_000]]],
            vec![[1_000_000, 2_000_000]],
        ),
        // ===== Many Small Gaps =====
        (
            vec![vec![[1, 2], [3, 4], [5, 6]], vec![[2, 3], [4, 5]]],
            vec![],
        ),
        // ===== Disconnected Blocks =====
        (
            vec![vec![[1, 2], [8, 9]], vec![[3, 4], [6, 7]]],
            vec![[2, 3], [4, 6], [7, 8]],
        ),
        // ===== Large Pattern =====
        (
            vec![
                (0..20)
                    .step_by(4)
                    .map(|i| [i, i + 2])
                    .collect::<Vec<[i32; 2]>>(),
                (0..20)
                    .step_by(4)
                    .map(|i| [i + 1, i + 3])
                    .collect::<Vec<[i32; 2]>>(),
            ],
            vec![[3, 4], [7, 8], [11, 12], [15, 16]],
        ),
        // ===== Single Employee With Multiple Internal Gaps =====
        (
            vec![(0..20)
                .step_by(2)
                .map(|i| [i, i + 1])
                .collect::<Vec<[i32; 2]>>()],
            (1..18)
                .step_by(2)
                .map(|i| [i, i + 1])
                .collect::<Vec<[i32; 2]>>(),
        ),
        // ===== Maximum Overlap =====
        (vec![vec![[1, 100]], vec![[1, 100]], vec![[1, 100]]], vec![]),
        // ===== Additional Edge Cases =====
        (vec![], vec![]),
        (vec![vec![], vec![]], vec![]),
        (vec![vec![], vec![[1, 2], [4, 5]]], vec![[2, 4]]),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        common_free_time(&input)
    }));
}
