fn main() {
    let network1: Vec<Vec<i32>> = vec![
        vec![0, 4],
        vec![0, 8],
        vec![0, 1],
        vec![0, 2],
        vec![0, 3],
        vec![8, 4],
        vec![4, 5],
        vec![5, 3],
        vec![3, 6],
        vec![6, 7],
        vec![1, 7],
    ];
    let network2: Vec<Vec<i32>> = (0..10).map(|i| vec![i, i + 1]).collect();
    let network3: Vec<Vec<i32>> = {
        let mut v = network2.clone();
        v.push(vec![10, 1]);
        v
    };

    let test_cases: Vec<((i32, Vec<Vec<i32>>), Vec<Vec<i32>>)> = vec![
        (
            (4, vec![vec![0, 1], vec![1, 2], vec![2, 0], vec![1, 3]]),
            vec![vec![1, 3]],
        ),
        (
            (
                7,
                vec![
                    vec![0, 1],
                    vec![1, 2],
                    vec![2, 0],
                    vec![1, 3],
                    vec![1, 4],
                    vec![4, 5],
                    vec![5, 6],
                ],
            ),
            vec![vec![1, 3], vec![1, 4], vec![4, 5], vec![5, 6]],
        ),
        (
            (
                7,
                vec![
                    vec![0, 1],
                    vec![1, 2],
                    vec![2, 0],
                    vec![1, 3],
                    vec![1, 4],
                    vec![4, 5],
                    vec![5, 6],
                    vec![2, 6],
                ],
            ),
            vec![vec![1, 3]],
        ),
        ((9, network1.clone()), vec![vec![0, 2]]),
        (
            (11, network2.clone()),
            (0..10).map(|i| vec![i, i + 1]).collect(),
        ),
        ((11, network3.clone()), vec![vec![0, 1]]),
        // edge cases
        ((1, vec![]), vec![]),
        ((2, vec![vec![0, 1]]), vec![vec![0, 1]]),
        ((3, vec![vec![0, 1], vec![1, 2], vec![2, 0]]), vec![]),
        (
            (4, vec![vec![0, 1], vec![2, 3]]),
            vec![vec![0, 1], vec![2, 3]],
        ),
        (
            (4, vec![vec![0, 1], vec![0, 2], vec![0, 3], vec![1, 2]]),
            vec![vec![0, 3]],
        ),
        (
            (5, vec![vec![0, 1], vec![1, 2], vec![2, 3], vec![3, 4]]),
            vec![vec![0, 1], vec![1, 2], vec![2, 3], vec![3, 4]],
        ),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        critical_connections(input.0, input.1.clone())
    }));
}
