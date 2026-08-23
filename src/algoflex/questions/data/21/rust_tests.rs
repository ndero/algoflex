fn main() {
    let test_cases = vec![
        ((vec![1, 5, 11, 5],), true),
        ((vec![6],), false),
        (((0..300).collect(),), true),
        ((vec![1, 5, 13, 5],), false),
        ((vec![1, 5, 11, 5].repeat(100),), true),
        ((vec![1, 5, 13, 5, 35, 92, 11, 17, 13, 53],), false),
        (((1..330).step_by(2).collect(),), false),
        // Edge cases
        ((vec![],), true),
        ((vec![0],), true),
        ((vec![0, 0],), true),
        ((vec![1, 1],), true),
        ((vec![1, 1, 1],), false),
        ((vec![1, 2, 3],), true),
        ((vec![1, 2, 3, 4, 5, 6, 7],), true),
        ((vec![1, 2, 5],), false),
        ((vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10],), false),
        ((vec![1, 2, 3, 4, 5, 6, 7, 8, 9],), false),
        ((vec![1; 100],), true),
        ((vec![2; 99],), false),
    ];

    std::process::exit(run_tests!(&test_cases, |input| can_partition(&input.0)));
}
