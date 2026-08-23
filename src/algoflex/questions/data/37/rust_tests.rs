fn main() {
    let arr1 = vec![8, 2, 4, 9, 12, 18, 16, 13];
    let arr2: Vec<i32> = (0..=100_000).rev().collect();
    let arr3: Vec<i32> = (0..10_000).collect();
    let arr4 = vec![8, 1, 5].repeat(100_000);
    let arr5 = vec![3];

    let test_cases = vec![
        ((arr1,), vec![2, 4, 8, 9, 12, 13, 16, 18]),
        ((arr2,), (0..=100_000).collect::<Vec<_>>()),
        ((arr3,), (0..10_000).collect::<Vec<_>>()),
        ((arr4,), {
            let mut expected = Vec::with_capacity(300_000);
            expected.extend(std::iter::repeat_n(1, 100_000));
            expected.extend(std::iter::repeat_n(5, 100_000));
            expected.extend(std::iter::repeat_n(8, 100_000));
            expected
        }),
        ((arr5,), vec![3]),
        // Edge cases
        ((vec![],), vec![]),
        ((vec![1],), vec![1]),
        ((vec![2, 1],), vec![1, 2]),
        ((vec![5, 5, 5, 5],), vec![5, 5, 5, 5]),
        ((vec![-3, 2, -1, 0],), vec![-3, -1, 0, 2]),
    ];

    std::process::exit(run_tests!(&test_cases, |input| merge_sort(&input.0)));
}
