fn main() {
    let test_cases = vec![
        // Basic test cases
        (
            (vec![73, 74, 75, 71, 69, 72, 76, 73],),
            vec![1, 1, 4, 2, 1, 1, 0, 0],
        ),
        ((vec![30, 40, 50, 60],), vec![1, 1, 1, 0]),
        ((vec![60, 50, 40, 30],), vec![0, 0, 0, 0]),
        ((vec![70, 70, 70, 70],), vec![0, 0, 0, 0]),
        // Edge cases
        ((vec![30],), vec![0]),
        ((vec![],), vec![]),
        ((vec![30, 31],), vec![1, 0]),
        ((vec![31, 30],), vec![0, 0]),
        // Complex patterns
        (
            (vec![80, 70, 90, 60, 85, 75, 95],),
            vec![2, 1, 4, 1, 2, 1, 0],
        ),
        (
            (vec![73, 72, 71, 70, 74, 73, 72, 75],),
            vec![4, 3, 2, 1, 3, 2, 1, 0],
        ),
        (
            (vec![40, 45, 50, 55, 50, 45, 40],),
            vec![1, 1, 1, 0, 0, 0, 0],
        ),
        (
            (vec![60, 50, 40, 30, 40, 50, 60],),
            vec![0, 5, 3, 1, 1, 1, 0],
        ),
        ((vec![50, 50, 50, 60, 50, 70],), vec![3, 2, 1, 2, 1, 0]),
        // Special scenarios
        ((vec![100, 50, 51, 52, 53, 54],), vec![0, 1, 1, 1, 1, 0]),
        (
            (vec![30, 31, 32, 33, 34, 35, 36, 29],),
            vec![1, 1, 1, 1, 1, 1, 0, 0],
        ),
        ((vec![50, 49, 48, 47, 46, 51],), vec![5, 4, 3, 2, 1, 0]),
        (
            (vec![90, 50, 91, 51, 92, 52, 93],),
            vec![2, 1, 2, 1, 2, 1, 0],
        ),
        ((vec![0, 100, 0, 100],), vec![1, 0, 1, 0]),
        // Stress test 1: strictly increasing
        (((1..=10_000).collect::<Vec<i32>>(),), {
            let mut result = vec![1; 9_999];
            result.push(0);
            result
        }),
        // Stress test 2: strictly decreasing
        (((1..=10_000).rev().collect::<Vec<i32>>(),), vec![0; 10_000]),
        // Stress test 3: constant temperature
        ((vec![70; 10_000],), vec![0; 10_000]),
        // Stress test 4: mountain
        (
            ((1..=5_000).chain((1..=5_000).rev()).collect::<Vec<i32>>(),),
            {
                let mut result = vec![1; 4_999];
                result.extend(vec![0; 5_001]);
                result
            },
        ),
        // Stress test 5: valley
        (
            ((1..=5_000).rev().chain(1..=5_000).collect::<Vec<i32>>(),),
            {
                let mut result = vec![0];
                result.extend((1..=4_999).rev().map(|i| i * 2));
                result.extend(vec![1; 4_999]);
                result.push(0);
                result
            },
        ),
        // Stress test 6: alternating high-low
        (
            ((0..10_000)
                .map(|i| if i % 2 == 0 { 100 } else { 0 })
                .collect::<Vec<i32>>(),),
            (0..9_999)
                .map(|i| if i % 2 == 0 { 0 } else { 1 })
                .chain(std::iter::once(0))
                .collect::<Vec<i32>>(),
        ),
        // Stress test 8: decreasing then one spike
        (
            ((1..=10_000)
                .rev()
                .chain(std::iter::once(100_001))
                .collect::<Vec<i32>>(),),
            (0..=10_000).rev().collect::<Vec<i32>>(),
        ),
        // Stress test 9: one warmer day in the middle
        (
            (vec![1_000_000; 5_000]
                .into_iter()
                .chain(std::iter::once(1_000_001))
                .chain(vec![1_000_000; 4_999])
                .collect::<Vec<i32>>(),),
            {
                let mut result: Vec<i32> = (0..=5_000).rev().collect();
                result.extend(vec![0; 4_999]);
                result
            },
        ),
        // Alternating extreme values
        (
            (vec![1, 1_000_000, 2, 999_999, 3, 999_998],),
            vec![1, 0, 1, 0, 1, 0],
        ),
        // All equal except final warmer day.
        (
            (vec![70; 10]
                .into_iter()
                .chain(std::iter::once(71))
                .collect::<Vec<i32>>(),),
            {
                let mut result: Vec<i32> = (1..=10).rev().collect();
                result.push(0);
                result
            },
        ),
        // Immediate warmer day.
        ((vec![1, 2, 3, 4, 5],), vec![1, 1, 1, 1, 0]),
        // No warmer temperature.
        ((vec![5, 4, 3, 2, 1],), vec![0, 0, 0, 0, 0]),
        // Equal temperatures are not warmer.
        ((vec![5, 5, 6],), vec![2, 1, 0]),
        // Multiple rises after a plateau.
        ((vec![5, 5, 5, 6, 5, 5, 7],), vec![3, 2, 1, 3, 2, 1, 0]),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        daily_temperatures(&input.0)
    }));
}
