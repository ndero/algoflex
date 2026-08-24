fn main() {
    let mut network: Vec<Vec<i32>> = Vec::new();
    for i in 1..10 {
        network.push(vec![i, i + 1, i * 100]);
    }
    for i in (1..10).step_by(2) {
        network.push(vec![i, i + 2, 100]);
    }
    network.push(vec![10, 1, 10_000]);

    let test_cases: Vec<((Vec<Vec<i32>>, i32, i32), i32)> = vec![
        ((vec![vec![2, 1, 1], vec![2, 3, 1], vec![3, 4, 1]], 4, 2), 2),
        ((vec![vec![1, 2, 1]], 2, 1), 1),
        ((vec![vec![1, 2, 1]], 4, 2), -1),
        ((vec![vec![1, 2, 6]], 2, 1), 6),
        ((vec![vec![1, 2, 6]], 2, 2), -1),
        ((network.clone(), 11, 1), 1300),
        ((network.clone(), 11, 2), 11400),
        ((network.clone(), 11, 11), -1),
        ((network.clone(), 11, 5), 11500),
        // edge case
        ((vec![], 1, 1), 0),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        min_network_delay(&input.0, input.1, input.2)
    }));
}
