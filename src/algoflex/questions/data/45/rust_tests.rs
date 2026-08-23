fn main() {
    let nums1 = vec![2, 3, 1, 1, 4];
    let nums2 = vec![1];
    let nums3 = vec![1, 5];
    let nums4 = vec![1; 200_000];

    let mut nums5 = vec![200_000];
    nums5.extend(std::iter::repeat_n(0, 200_000));

    let nums6: Vec<i32> = (1..100_000).collect();

    let test_cases = vec![
        ((nums1,), 2),
        ((nums2,), 0),
        ((nums3,), 1),
        ((nums4,), 199_999),
        ((nums5,), 1),
        ((nums6,), 17),
        // Edge cases
        ((vec![2, 1],), 1),
        ((vec![1, 1, 1],), 2),
        ((vec![3, 1, 1, 1],), 1),
        ((vec![1, 2, 1, 1],), 2),
    ];

    std::process::exit(run_tests!(&test_cases, |input| min_jumps(&input.0)));
}
