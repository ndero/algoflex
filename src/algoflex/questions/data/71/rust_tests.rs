fn main() {
    let test_cases = vec![
        // Minimal cases
        ((2, vec![vec![0, 1]]), 2),
        ((2, vec![vec![0, 1], vec![1, 0]]), 1),
        ((1, vec![]), 1),
        ((2, vec![]), 2),
        // Small simple cycles
        ((3, vec![vec![0, 1], vec![1, 2], vec![2, 0]]), 1),
        ((3, vec![vec![0, 1], vec![1, 2]]), 3),
        ((3, vec![vec![0, 1], vec![1, 0], vec![1, 2]]), 2),
        ((4, vec![vec![0, 1], vec![1, 2], vec![2, 3], vec![3, 0]]), 1),
        // Disconnected graphs
        ((4, vec![]), 4),
        ((5, vec![vec![0, 1], vec![1, 0], vec![3, 4], vec![4, 3]]), 3),
        (
            (
                6,
                vec![vec![0, 1], vec![1, 0], vec![2, 3], vec![3, 2], vec![4, 5]],
            ),
            4,
        ),
        // Self loops
        ((3, vec![vec![0, 0], vec![1, 1], vec![2, 2]]), 3),
        ((3, vec![vec![0, 1], vec![1, 0], vec![2, 2]]), 2),
        // Chain graph
        ((5, vec![vec![0, 1], vec![1, 2], vec![2, 3], vec![3, 4]]), 5),
        ((10, (0..9).map(|i| vec![i, i + 1]).collect()), 10),
        // Reverse chain
        ((5, vec![vec![4, 3], vec![3, 2], vec![2, 1], vec![1, 0]]), 5),
        // Two separate cycles
        (
            (
                6,
                vec![
                    vec![0, 1],
                    vec![1, 2],
                    vec![2, 0],
                    vec![3, 4],
                    vec![4, 5],
                    vec![5, 3],
                ],
            ),
            2,
        ),
        // Cycle with tail
        (
            (
                5,
                vec![vec![0, 1], vec![1, 2], vec![2, 0], vec![2, 3], vec![3, 4]],
            ),
            3,
        ),
        // Star patterns
        ((5, vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![0, 4]]), 5),
        ((5, vec![vec![1, 0], vec![2, 0], vec![3, 0], vec![4, 0]]), 5),
        // Complete digraph
        (
            (
                4,
                (0..4)
                    .flat_map(|i| (0..4).filter(move |&j| j != i).map(move |j| vec![i, j]))
                    .collect(),
            ),
            1,
        ),
        // Diamond DAG
        ((4, vec![vec![0, 1], vec![0, 2], vec![1, 3], vec![2, 3]]), 4),
        // Bidirectional components
        (
            (
                5,
                vec![
                    vec![0, 1],
                    vec![1, 0],
                    vec![2, 3],
                    vec![3, 2],
                    vec![3, 4],
                    vec![4, 3],
                ],
            ),
            2,
        ),
        // Large single SCC
        ((10, (0..10).map(|i| vec![i, (i + 1) % 10]).collect()), 1),
        // Two SCC blocks
        (
            (
                10,
                (0..5)
                    .map(|i| vec![i, (i + 1) % 5])
                    .chain((5..10).map(|i| vec![i, 5 + ((i - 5 + 1) % 5)]))
                    .collect(),
            ),
            2,
        ),
        // Bridge between cycles
        (
            (
                6,
                vec![
                    vec![0, 1],
                    vec![1, 2],
                    vec![2, 0],
                    vec![3, 4],
                    vec![4, 5],
                    vec![5, 3],
                    vec![2, 3],
                ],
            ),
            2,
        ),
        // Long chain with back edge
        (
            (
                20,
                (0..19)
                    .map(|i| vec![i, i + 1])
                    .chain(std::iter::once(vec![19, 0]))
                    .collect(),
            ),
            1,
        ),
        // Many tiny SCCs
        ((20, (0..20).map(|i| vec![i, i]).collect()), 20),
        // Large sparse chain
        ((50, (0..49).map(|i| vec![i, i + 1]).collect()), 50),
        // Large cycle
        ((50, (0..50).map(|i| vec![i, (i + 1) % 50]).collect()), 1),
        // Two large cycles connected one way
        (
            (
                20,
                (0..10)
                    .map(|i| vec![i, (i + 1) % 10])
                    .chain((10..20).map(|i| vec![i, 10 + ((i - 10 + 1) % 10)]))
                    .chain(std::iter::once(vec![5, 15]))
                    .collect(),
            ),
            2,
        ),
        // Many isolated vertices plus one cycle
        ((10, vec![vec![0, 1], vec![1, 2], vec![2, 0]]), 8),
        // Bidirectional line
        (
            (
                6,
                (0..5)
                    .map(|i| vec![i, i + 1])
                    .chain((0..5).map(|i| vec![i + 1, i]))
                    .collect(),
            ),
            1,
        ),
        // Dense complete graph
        (
            (
                15,
                (0..15)
                    .flat_map(|i| (0..15).filter(move |&j| j != i).map(move |j| vec![i, j]))
                    .collect(),
            ),
            1,
        ),
        // Large DAG
        (
            (
                30,
                (0..30)
                    .flat_map(|i| ((i + 1)..30).map(move |j| vec![i, j]))
                    .collect(),
            ),
            30,
        ),
        // Additional edge cases
        ((1, vec![vec![0, 0]]), 1),
        ((3, vec![vec![0, 1], vec![1, 2], vec![2, 1]]), 2),
        (
            (
                4,
                vec![vec![0, 1], vec![1, 0], vec![1, 2], vec![2, 3], vec![3, 2]],
            ),
            2,
        ),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        count_scc(input.0, &input.1)
    }));
}
