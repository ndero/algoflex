fn main() {
    let test_cases = vec![
        ((0,), 0_i64),
        ((1,), 1_i64),
        ((2,), 2_i64),
        ((10,), 89_i64),
        ((51,), 32951280099_i64),
        // Edge cases
        ((3,), 3_i64),
        ((4,), 5_i64),
        ((5,), 8_i64),
        ((46,), 2971215073_i64),
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| climb_stairs(input.0))
    );
}