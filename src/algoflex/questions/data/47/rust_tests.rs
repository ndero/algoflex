fn main() {
    let nums1 = vec![1, 2, 3, 1];
    let nums2 = vec![1, 7, 2, 1, 6];
    let nums3 = vec![1, 2];
    let nums4 = vec![3];
    let nums5 = vec![133, 99, 17, 39, 54, 98, 57, 34, 23, 100];
    let nums6: Vec<i32> = (0..100_000).step_by(100).collect();

    let test_cases = vec![
        ((nums1,), 4),
        ((nums2,), 13),
        ((nums3,), 2),
        ((nums4,), 3),
        ((nums5,), 404),
        ((nums6,), 25_000_000),
        // Edge cases
        ((vec![],), 0),
        ((vec![0],), 0),
        ((vec![1, 1],), 1),
        ((vec![2, 1, 1, 2],), 4),
        ((vec![5, 1, 5, 1, 5],), 15),
    ];

    std::process::exit(run_tests!(&test_cases, |input| max_loot(&input.0)));
}
