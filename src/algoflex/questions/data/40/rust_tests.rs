fn main() {
    let arr1 = vec![5, 2, 2, 6, 1];
    let arr2 = vec![0];
    let arr3 = vec![];
    let arr4 = vec![8, 2, 4, 9, 12, 18, 16];
    let arr5: Vec<i32> = (0..100_000).collect();
    let arr6: Vec<i32> = (1..=100_000).rev().collect();

    let test_cases = vec![
        ((arr1,), vec![3, 1, 1, 1, 0]),
        ((arr2,), vec![0]),
        ((arr3,), vec![]),
        ((arr4,), vec![2, 0, 0, 0, 0, 1, 0]),
        ((arr5,), vec![0; 100_000]),
        (
            (arr6,),
            (0..=99_999).rev().collect::<Vec<_>>(),
        ),

        // Edge cases
        ((vec![1, 1, 1, 1],), vec![0, 0, 0, 0]),
        ((vec![3, 2, 1],), vec![2, 1, 0]),
        ((vec![1, 2, 3],), vec![0, 0, 0]),
        ((vec![-2, -5, -1, -3],), vec![2, 0, 1, 0]),
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| smaller_to_the_right(&input.0))
    );
}