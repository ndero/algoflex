fn main() {
    let test_cases = vec![
        ((1,), 1),
        ((2,), 0),
        ((3,), 0),
        ((4,), 2),
        ((5,), 10),
        ((6,), 4),
        ((7,), 40),
        ((8,), 92),
        ((9,), 352),
        ((0,), 1),
    ];

    std::process::exit(run_tests!(&test_cases, |input| { n_queens(input.0) }));
}
