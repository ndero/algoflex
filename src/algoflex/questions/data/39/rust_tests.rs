fn main() {
    let g1 = (1, vec![]);
    let g2 = (2, vec![vec![1, 2, 10]]);
    let g3 = (2, vec![vec![]]); // one empty edge, will be filtered out
    let g4 = (4, vec![vec![1, 2, 3], vec![2, 3, 4]]);
    let g5 = (3, vec![vec![1, 2, 10], vec![1, 2, 1], vec![2, 3, 2]]);
    let g6 = (
        4,
        vec![vec![1, 2, 1], vec![2, 3, 1], vec![3, 4, 1], vec![4, 1, 10]],
    );
    let g7 = (
        4,
        vec![
            vec![1, 2, 5],
            vec![1, 3, 6],
            vec![1, 4, 4],
            vec![2, 3, 2],
            vec![2, 4, 3],
            vec![3, 4, 1],
        ],
    );
    let g8 = (3, vec![vec![1, 2, -5], vec![2, 3, 2], vec![1, 3, 10]]);
    let g9 = (
        5,
        vec![vec![1, 2, 1], vec![1, 3, 1], vec![1, 4, 1], vec![1, 5, 1]],
    );
    let g10 = (
        6,
        vec![
            vec![1, 2, 1],
            vec![2, 3, 1],
            vec![3, 4, 1],
            vec![4, 5, 1],
            vec![5, 6, 1],
        ],
    );
    let g11 = (
        4,
        vec![vec![1, 2, 1], vec![2, 3, 100], vec![1, 3, 2], vec![3, 4, 1]],
    );

    let g12 = (1, vec![]);
    let g13 = (3, vec![vec![1, 2, 0], vec![2, 3, 0]]);
    let g14 = (3, vec![vec![1, 2, -4], vec![2, 3, -2], vec![1, 3, 5]]);

    let test_cases = vec![
        (g1, 0),
        (g2, 10),
        (g3, -1),
        (g4, -1),
        (g5, 3),
        (g6, 3),
        (g7, 7),
        (g8, -3),
        (g9, 4),
        (g10, 5),
        (g11, 4),
        (g12, 0),
        (g13, 0),
        (g14, -6),
    ];

    std::process::exit(run_tests!(&test_cases, |input| min_connection_cost(
        input.0, &input.1
    )));
}
