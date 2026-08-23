fn main() {
    let nums1 = vec![3, 2, 3];
    let nums2 = vec![6; 20];

    let mut nums3 = vec![9; 21];
    nums3.extend(std::iter::repeat_n(7, 20));

    let nums4 = vec![2];

    let mut nums6 = vec![6; 100_000];
    nums6.extend(std::iter::repeat_n(9, 100_001));

    let nums7 = vec![-2, -2, -4, -2, -4, -4, -4];

    let test_cases = vec![
        ((nums1,), 3),
        ((nums2,), 6),
        ((nums3,), 9),
        ((nums4,), 2),
        ((nums6,), 9),
        ((nums7,), -4),
        // Edge cases
        ((vec![1, 1, 2],), 1),
        ((vec![1, 2, 1, 1, 2, 1, 1],), 1),
        ((vec![-1, -1, 2, -1],), -1),
    ];

    std::process::exit(run_tests!(&test_cases, |input| majority(&input.0)));
}
