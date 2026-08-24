fn main() {
    let test_cases = vec![
        // Minimal edge cases
        ((vec![1],), vec![]),
        ((vec![1, 1],), vec![2]),
        // Small basic cases
        ((vec![1, 2, 3, 4],), vec![]),
        ((vec![4, 3, 2, 7, 8, 2, 3, 1],), vec![5, 6]),
        ((vec![1, 1],), vec![2]),
        ((vec![2, 2],), vec![1]),
        // Single missing
        ((vec![1, 2, 2, 4],), vec![3]),
        ((vec![2, 3, 4, 4, 5],), vec![1]),
        ((vec![1, 2, 3, 3, 5],), vec![4]),
        ((vec![1, 1, 2, 3, 4],), vec![5]),
        // Multiple missing
        ((vec![2, 2, 3, 3],), vec![1, 4]),
        ((vec![4, 4, 4, 4],), vec![1, 2, 3]),
        ((vec![1, 3, 3, 5, 5],), vec![2, 4]),
        ((vec![2, 2, 2, 2, 5, 5],), vec![1, 3, 4, 6]),
        // Missing at boundaries
        ((vec![2, 3, 4, 5, 5],), vec![1]),
        ((vec![1, 1, 2, 3, 4],), vec![5]),
        ((vec![5, 4, 3, 2, 2],), vec![1]),
        // All same number
        ((vec![3, 3, 3],), vec![1, 2]),
        ((vec![1, 1, 1, 1],), vec![2, 3, 4]),
        // Sorted with gaps
        ((vec![1, 2, 4, 6, 6, 6, 7],), vec![3, 5]),
        ((vec![1, 3, 5, 7, 7, 7, 7],), vec![2, 4, 6]),
        // Reverse order with duplicates
        ((vec![5, 4, 3, 2, 2],), vec![1]),
        ((vec![6, 5, 4, 3, 2, 2],), vec![1]),
        // Random distributions
        ((vec![3, 1, 2, 5, 3],), vec![4]),
        ((vec![6, 1, 1, 2, 4, 6],), vec![3, 5]),
        ((vec![7, 3, 2, 1, 8, 2, 3, 1],), vec![4, 5, 6]),
        // Stress: large n, no missing
        (((1..=100_000).collect::<Vec<i32>>(),), vec![]),
        // Stress: large n, one missing
        (
            ((1..=100_000)
                .take(99_999)
                .chain(std::iter::once(99_999))
                .collect::<Vec<i32>>(),),
            vec![100_000],
        ),
        // Stress: large n, missing first
        (
            ((2..=100_000)
                .chain(std::iter::once(100_000))
                .collect::<Vec<i32>>(),),
            vec![1],
        ),
        // Stress: half missing
        (
            ((1..=50_000).chain(1..=50_000).collect::<Vec<i32>>(),),
            (50_001..=100_000).collect::<Vec<i32>>(),
        ),
        // Stress: heavy duplication
        (
            (vec![50_000; 100_000],),
            (1..=100_000).filter(|&i| i != 50_000).collect::<Vec<i32>>(),
        ),
        // Long gap in middle
        (
            ((1..=40_000)
                .chain(vec![40_000; 20_000])
                .chain(60_001..=100_000)
                .collect::<Vec<i32>>(),),
            (40_001..=60_000).collect::<Vec<i32>>(),
        ),
        // Patterned duplicates
        (
            ((1..=20)
                .map(|i| if i % 2 == 0 { i } else { 2 })
                .collect::<Vec<i32>>(),),
            (1..=20)
                .filter(|i| i % 2 != 0 && *i != 2)
                .collect::<Vec<i32>>(),
        ),
        // Repeated small subset
        (
            ((0..20_000)
                .flat_map(|_| [1, 2, 3, 4, 5])
                .collect::<Vec<i32>>(),),
            (6..=100_000).collect::<Vec<i32>>(),
        ),
        // Sparse unique values
        (
            (vec![100_000; 99_999]
                .into_iter()
                .chain(std::iter::once(1))
                .collect::<Vec<i32>>(),),
            (2..=99_999).collect::<Vec<i32>>(),
        ),
        // Extra edge cases

        // Only first value repeated.
        ((vec![1, 1, 1, 1, 1],), vec![2, 3, 4, 5]),
        // Only last value repeated.
        ((vec![5, 5, 5, 5, 5],), vec![1, 2, 3, 4]),
        // Two values duplicated.
        ((vec![1, 5, 1, 5, 1],), vec![2, 3, 4]),
        // Alternating duplicates.
        ((vec![1, 2, 1, 2, 1, 2],), vec![3, 4, 5, 6]),
        // Missing values spread throughout.
        ((vec![1, 3, 5, 7, 9, 9, 9, 9, 9],), vec![2, 4, 6, 8]),
        // Different ordering.
        ((vec![5, 1, 4, 2, 5],), vec![3]),
        // No missing values despite duplicates.
        ((vec![1, 2, 3, 3, 3, 4, 4, 5],), vec![6, 7, 8]),
        // Only one distinct value present.
        ((vec![7, 7, 7, 7, 7, 7, 7],), vec![1, 2, 3, 4, 5, 6]),
    ];

    std::process::exit(run_tests!(&test_cases, |input| { find_missing(&input.0) }));
}
