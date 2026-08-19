fn main() {
    let test_cases = vec![
        ((50, vec![10, 20, 30], vec![60, 100, 120]), 240.0),
        ((60, vec![10, 20, 30], vec![60, 100, 120]), 280.0),
        ((9, vec![10, 20, 30], vec![60, 100, 120]), 54.0),
        ((0, vec![10, 20, 30], vec![60, 100, 120]), 0.0),
        ((9, vec![10, 20, 30], vec![60, 100, 120]), 54.0),
        ((5, vec![], vec![]), 0.0),
        ((6000, vec![10, 20, 30], vec![60, 100, 120]), 280.0),
        ((5, vec![10, 20, 30].repeat(1000), vec![60, 100, 120].repeat(1000)), 30.0),
        ((5000, vec![10, 20, 30].repeat(100_000), vec![60, 100, 120].repeat(100_000)), 30_000.0),
        // Edge cases
        ((10, vec![5], vec![10]), 10.0),                            // Single item, exact fit
        ((12, vec![15], vec![10]), 8.0),                            // Single item, fractional
        ((100, vec![100, 100], vec![50, 50]), 50.0),                // Equal weights, pick best value
        ((50, vec![25, 25, 25], vec![30, 30, 30]), 60.0),           // All items fit
        ((1, vec![100], vec![50]), 0.5),                            // Tiny capacity
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| fractional_knapsack(input.0, &input.1, &input.2))
    );
}