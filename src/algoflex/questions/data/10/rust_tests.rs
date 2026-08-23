fn main() {
    let test_cases = vec![
        ((vec![4, 1, 2, 1, 2],), 4),
        ((vec![2],), 2),
        (
            ({
                let mut v: Vec<i32> = (1..500_000).collect();
                v.extend(0..500_000);
                v
            },),
            0,
        ),
        (
            ({
                let mut v: Vec<i32> = (0..500_000).collect();
                v.extend([-2, -3]);
                v.extend(0..500_000);
                v.push(-2);
                v
            },),
            -3,
        ),
        (
            ({
                let mut v: Vec<i32> = (1..500_000).collect();
                v.extend(1..500_000);
                v.push(-4);
                v
            },),
            -4,
        ),
        (
            ({
                let mut v = vec![500_001];
                v.extend((-500_000..500_000).collect::<Vec<i32>>());
                v.extend((-500_000..500_000).collect::<Vec<i32>>());
                v
            },),
            500_001,
        ),
        // Edge cases
        ((vec![0],), 0),                                   // Single zero
        ((vec![-1],), -1),                                 // Single negative
        ((vec![1, 2, 3, 2, 1],), 3),                       // Middle element
        ((vec![-2, -1, -2],), -1),                         // Negative numbers
        ((vec![0, 0, 1],), 1),                             // Zero pairs
        ((vec![i32::MAX, i32::MIN, i32::MAX],), i32::MIN), // Extreme values
    ];

    std::process::exit(run_tests!(&test_cases, |input| single_number(&input.0)));
}
