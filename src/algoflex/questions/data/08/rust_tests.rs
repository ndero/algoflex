fn main() {
    let test_cases = vec![
        ((vec![4, 5, 6, 7, 0, 1, 2],), 0),
        ((vec![16, 23, 43, 55, -7, -4, 3, 5, 9, 15],), -7),
        (((36..1_000_000).step_by(10).collect(),), 36),
        (
            ({
                let mut v: Vec<i32> = (-10..1_000_000).step_by(10).collect();
                v.extend((-1_000_000..-10).step_by(10));
                v
            },),
            -1_000_000,
        ),
        ((vec![2],), 2),
        (
            (vec![
                134, 140, 147, 156, 160, 164, 166, 166, 170, 183, 184, 192, -9, -4, 1, 20, 51, 54,
                54, 56, 67, 75, 80, 88, 92, 93, 96, 105, 115, 127,
            ],),
            -9,
        ),
        // Edge cases
        ((vec![1],), 1),             // Single element
        ((vec![1, 2],), 1),          // Two elements, not rotated
        ((vec![2, 1],), 1),          // Two elements, rotated
        ((vec![1, 2, 3, 4, 5],), 1), // Not rotated
        ((vec![5, 1, 2, 3, 4],), 1), // Rotated once
        ((vec![3, 3, 3, 1, 3],), 1), // Duplicates with min
        ((vec![3, 1, 3, 3, 3],), 1), // Duplicates with min at start
    ];

    std::process::exit(run_tests!(&test_cases, |input| min_rotated_arr(&input.0)));
}
