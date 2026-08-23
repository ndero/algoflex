fn main() {
    let nums1 = vec![4, 2, 3, 0, 3, 1, 2];
    let nums2 = vec![3, 0, 2, 1, 2];
    let nums3 = vec![4, 2, 3, 0, 3, 1, 2];
    let nums4 = {
        let mut nums = vec![1; 200_000];
        nums.push(0);
        nums
    };
    let nums5 = vec![0];
    let nums6 = vec![2, 4, 0, 1, 1, 1, 0, 2, 1];

    let test_cases = vec![
        ((nums1, 0), true),
        ((nums2, 2), false),
        ((nums3, 5), true),
        ((nums4, 567), true),
        ((nums5, 0), true),
        ((nums6, 8), true),
        ((vec![0, 1], 0), true),
        ((vec![0, 1], 1), true),
        ((vec![1, 0], 0), true),
        ((vec![1, 0], 1), true),
        ((vec![2, 1, 1], 0), false),
        ((vec![2, 1, 1], 1), false),
        ((vec![1, 1, 1], 0), false),
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| {
            can_reach_zero(&input.0, input.1)
        })
    );
}