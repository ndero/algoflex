fn main() {
    let network: Vec<[i32; 3]> = {
        let mut network = Vec::new();

        for i in 1..10 {
            network.push([i, i + 1, i * 100]);
        }

        for i in (1..10).step_by(2) {
            network.push([i, i + 2, 100]);
        }

        network.push([10, 1, 10_000]);

        network
    };

    let test_cases: Vec<((Vec<[i32; 3]>, i32, i32), i32)> = vec![
        ((vec![[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
        ((vec![[1, 2, 1]], 2, 1), 1),
        ((vec![[1, 2, 1]], 4, 2), -1),
        ((vec![[1, 2, 6]], 2, 1), 6),
        ((vec![[1, 2, 6]], 2, 2), -1),
        ((network.clone(), 11, 1), 1300),
        ((network.clone(), 11, 2), 11_400),
        ((network.clone(), 11, 11), -1),
        ((network.clone(), 11, 5), 11_500),
        // edge case
        ((vec![], 1, 1), 0),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        min_network_delay(&input.0, input.1, input.2)
    }));
}
