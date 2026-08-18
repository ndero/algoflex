fn main() {
    let test_cases = vec![
        ((vec!["2", "1", "+", "3", "*"].iter().map(|s| s.to_string()).collect(),), 9),
        ((vec!["4", "13", "5", "/", "+"].iter().map(|s| s.to_string()).collect(),), 6),
        ((vec!["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"].iter().map(|s| s.to_string()).collect(),), 22),
        ((vec!["10", "6", "9", "3", "+", "-11", "/", "*", "*", "17", "+", "5", "+"].iter().map(|s| s.to_string()).collect(),), -38),
        (({
            let mut v = vec!["1".to_string()];
            for _ in 0..100_000 {
                v.push("2".to_string());
                v.push("+".to_string());
            }
            v
        },), 200_001),
        (({
            let mut v = vec!["2".to_string()];
            for _ in 0..100_000 {
                v.push("1".to_string());
                v.push("*".to_string());
            }
            v
        },), 2),
        // Edge cases
        ((vec!["5".to_string()],), 5),                              // Single operand
        ((vec!["3", "4", "-"].iter().map(|s| s.to_string()).collect(),), -1),  // Negative result
        ((vec!["7", "2", "/"].iter().map(|s| s.to_string()).collect(),), 3),   // Truncate toward zero
        ((vec!["-7", "2", "/"].iter().map(|s| s.to_string()).collect(),), -3), // Negative truncation
        ((vec!["0", "5", "*"].iter().map(|s| s.to_string()).collect(),), 0),   // Zero result
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| eval_rpn(&input.0))
    );
}