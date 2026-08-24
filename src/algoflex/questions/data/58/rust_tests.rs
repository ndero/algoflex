fn main() {
    let nums1: Vec<i32> = (0..10_000).collect();
    let nums2: Vec<i32> = vec![1; 10_000];
    let nums3 = vec![10, 9, 2, 5, 3, 7, 101, 18];
    let nums4 = vec![0, 1, 0, 3, 2, 3];

    let test_cases: Vec<((Vec<i32>,), i32)> = vec![
        ((vec![0, 1, 0, 3, 2, 3],), 4),
        ((vec![6; 8],), 1),
        ((nums3.clone(),), 4),
        ((nums1,), 10_000),
        ((nums2,), 1),
        ((nums3,), 4),
        ((nums4,), 4),
        ((Vec::new(),), 0),
        ((vec![5],), 1),
        ((vec![5, 4, 3, 2, 1],), 1),
        ((vec![1, 2, 3, 1, 2, 3, 1, 2, 3],), 3),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        longest_increasing_subsequence(&input.0)
    }));
}
