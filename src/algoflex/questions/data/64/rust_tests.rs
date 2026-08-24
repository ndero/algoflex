fn main() {
    let test_cases = vec![
        // Basic test cases
        ((vec![1],), 1),
        ((vec![3, 1, 2, 5, 4, 1],), 8),
        ((vec![2, 4],), 4),
        // Empty and edge cases
        ((vec![],), 0),
        ((vec![0],), 0),
        ((vec![0, 0, 0],), 0),
        ((vec![0, 1, 0],), 1),
        ((vec![1, 0, 1],), 1),
        // Increasing heights
        ((vec![1, 2, 3, 4, 5],), 9),
        ((vec![1, 2, 3, 4, 5, 6],), 12),
        // Decreasing heights
        ((vec![5, 4, 3, 2, 1],), 9),
        ((vec![6, 5, 4, 3, 2, 1],), 12),
        // Plateau
        ((vec![5, 5, 5, 5],), 20),
        ((vec![3, 3, 3, 3, 3],), 15),
        // Valley shapes
        ((vec![5, 4, 1, 4, 5],), 8),
        ((vec![6, 5, 2, 5, 6],), 10),
        // Peak shapes
        ((vec![1, 3, 5, 3, 1],), 9),
        ((vec![2, 4, 6, 4, 2],), 12),
        // Single tall bar
        ((vec![1, 2, 10, 2, 1],), 10),
        ((vec![1, 2, 3, 10, 3, 2, 1],), 10),
        // Multiple valleys
        ((vec![2, 1, 4, 5, 1, 3, 3],), 8),
        ((vec![3, 2, 5, 4, 2, 3, 4],), 14),
        // Alternating heights
        ((vec![1, 3, 2, 4, 3, 5],), 10),
        ((vec![2, 1, 3, 2, 4, 3],), 8),
        // Large differences
        ((vec![100, 1, 100],), 100),
        ((vec![1000, 1, 1000, 1, 1000],), 1000),
        // Zero in middle
        ((vec![3, 2, 0, 2, 3],), 4),
        ((vec![4, 3, 2, 0, 2, 3, 4],), 6),
        // Very large arrays
        (((1..=10_000).collect::<Vec<i32>>(),), 25_005_000),
        (((1..=10_000).rev().collect::<Vec<i32>>(),), 25_005_000),
        // Random combinations
        ((vec![2, 1, 2, 3, 1, 2, 3, 2],), 8),
        ((vec![4, 2, 0, 3, 2, 5, 4, 3],), 10),
        // Boundary tests
        ((vec![1; 10_000],), 10_000),
        ((vec![100_000; 100],), 10_000_000),
        // Mountain shape
        ((vec![1, 2, 3, 4, 5, 4, 3, 2, 1],), 15),
        // Staircase pattern
        ((vec![1, 2, 3, 4, 5, 6, 7, 8],), 20),
        ((vec![8, 7, 6, 5, 4, 3, 2, 1],), 20),
        // Complex patterns
        ((vec![6, 2, 5, 4, 5, 1, 6],), 12),
        ((vec![3, 6, 5, 7, 4, 8, 1, 0],), 20),
        // Single element with zero
        ((vec![5, 0, 5, 0, 5],), 5),
        // Long increasing then decreasing
        (
            ((1..=5_000).chain((1..=5_000).rev()).collect::<Vec<i32>>(),),
            12_505_000,
        ),
        // Checkerboard pattern
        ((vec![10, 1, 10, 1, 10, 1, 10],), 10),
        // All same except one dip
        (
            (vec![5; 100]
                .into_iter()
                .chain(std::iter::once(1))
                .chain(vec![5; 100])
                .collect(),),
            500,
        ),
        // Maximum values with constraints
        ((vec![100_000; 10_000],), 1_000_000_000),
        // Extra edge cases

        // Two equal bars
        ((vec![7, 7],), 14),
        // Tall bar at either boundary
        ((vec![10, 1, 1, 1],), 10),
        ((vec![1, 1, 1, 10],), 10),
        // Zero at the boundary
        ((vec![0, 5, 5],), 10),
        ((vec![5, 5, 0],), 10),
        // Multiple equal minima
        ((vec![4, 2, 2, 2, 4],), 10),
        // Best rectangle spans the entire histogram
        ((vec![3, 3, 3, 3],), 12),
        // Best rectangle is strictly in the middle
        ((vec![1, 5, 5, 5, 1],), 15),
        // Large spike surrounded by equal bars
        ((vec![2, 2, 10, 2, 2],), 10),
        // Several competing rectangles
        ((vec![2, 6, 6, 5, 5, 5, 2],), 25),
        // Zeros split the histogram into independent regions
        ((vec![2, 4, 3, 0, 5, 5, 1],), 10),
    ];

    std::process::exit(run_tests!(&test_cases, |input| { max_rectangle(&input.0) }));
}
