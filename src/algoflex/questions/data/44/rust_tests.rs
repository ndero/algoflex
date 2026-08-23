fn main() {
    let nums1 = vec![2, 3, 1, 1, 4];
    let nums2 = vec![0];
    let nums3 = vec![2, 1, 1, 0, 4];
    let nums4: Vec<i32> = (0..200_000).collect();
    let nums5 = vec![1; 200_000];
    let nums6 = vec![0, 0];

    let mut nums7 = vec![200_000];
    nums7.extend(std::iter::repeat_n(0, 200_000));

    let test_cases = vec![
        ((nums1,), true),
        ((nums2,), true),
        ((nums3,), false),
        ((nums4,), false),
        ((nums5,), true),
        ((nums6,), false),
        ((nums7,), true),
        // Edge cases
        ((vec![1],), true),
        ((vec![1, 0],), true),
        ((vec![0, 1],), false),
        ((vec![1, 1, 0],), true),
        ((vec![2, 0, 0],), true),
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| can_reach_end(&input.0))
    );
}