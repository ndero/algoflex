fn main() {
    let test_cases = vec![
        // Minimal cases
        (vec![vec![0]], 0),
        (vec![vec![1]], -1),
        (vec![vec![2]], 0),
        (vec![vec![2, 1]], 1),
        (vec![vec![1, 2]], 1),
        // Simple small grids
        (vec![vec![2, 1, 1], vec![1, 1, 0], vec![0, 1, 1]], 4),
        (vec![vec![2, 1, 1], vec![0, 1, 1], vec![1, 0, 1]], -1),
        (vec![vec![0, 2]], 0),
        (vec![vec![1, 1, 1]], -1),
        (vec![vec![2, 2, 2]], 0),
        // All fresh
        (vec![vec![1, 1], vec![1, 1]], -1),
        (vec![vec![1, 1, 1], vec![1, 1, 1], vec![1, 1, 1]], -1),
        // All rotten
        (vec![vec![2, 2], vec![2, 2]], 0),
        (vec![vec![2, 2, 2], vec![2, 2, 2]], 0),
        // No oranges
        (vec![vec![0, 0], vec![0, 0]], 0),
        // Single row propagation
        (vec![vec![2, 1, 1, 1, 1]], 4),
        (vec![vec![1, 1, 1, 1, 2]], 4),
        (vec![vec![2, 0, 1, 1, 1]], -1),
        // Single column propagation
        (vec![vec![2], vec![1], vec![1], vec![1]], 3),
        (vec![vec![1], vec![1], vec![1], vec![2]], 3),
        (vec![vec![2], vec![0], vec![1], vec![1]], -1),
        // Multiple rotten sources
        (vec![vec![2, 1, 1], vec![1, 2, 1], vec![1, 1, 2]], 2),
        (vec![vec![2, 1, 1, 1], vec![1, 1, 1, 2]], 2),
        (vec![vec![2, 1, 1, 1, 2]], 2),
        // Barriers
        (vec![vec![2, 0, 1]], -1),
        (vec![vec![2, 1, 0, 1]], -1),
        (vec![vec![2, 1, 0, 1, 2]], 1),
        (vec![vec![2, 1, 0, 1, 1, 1]], -1),
        // Complex medium grids
        (
            vec![vec![2, 1, 1, 0], vec![1, 1, 0, 1], vec![0, 1, 1, 1]],
            6,
        ),
        (
            vec![vec![2, 1, 0, 2], vec![1, 0, 1, 1], vec![1, 1, 1, 0]],
            3,
        ),
        (vec![vec![2, 1, 1], vec![1, 0, 1], vec![1, 1, 1]], 4),
        // Diagonal isolation
        (vec![vec![2, 0, 0], vec![0, 1, 0], vec![0, 0, 1]], -1),
        // Center source
        (vec![vec![1, 1, 1], vec![1, 2, 1], vec![1, 1, 1]], 2),
        // Corners only
        (vec![vec![2, 1, 1, 1, 2]], 2),
        // Long snake path
        (
            vec![
                vec![2, 1, 0, 0, 0],
                vec![0, 1, 1, 1, 0],
                vec![0, 0, 0, 1, 0],
                vec![0, 0, 0, 1, 1],
            ],
            7,
        ),
        // Larger stress-style grids
        (
            {
                let mut grid = vec![vec![2]];
                grid[0].extend(vec![1; 9]);
                grid.extend((0..9).map(|_| vec![1; 10]));
                grid
            },
            18,
        ),
        (vec![vec![1; 10]; 10], -1),
        (vec![vec![2; 10]; 10], 0),
        // 20x20 stress
        (
            {
                let mut grid = vec![vec![2]];
                grid[0].extend(vec![1; 19]);
                grid.extend((0..19).map(|_| vec![1; 20]));
                grid
            },
            38,
        ),
        // 20x20 with isolated fresh orange
        (
            {
                let mut grid = vec![vec![2]];
                grid[0].extend(vec![1; 18]);
                grid[0].push(0);
                grid.extend((0..18).map(|_| vec![1; 20]));
                let mut last = vec![0; 19];
                last.push(1);
                grid.push(last);
                grid
            },
            38,
        ),
        // Multiple sources far apart
        (
            {
                let mut grid = vec![vec![2]];
                grid[0].extend(vec![1; 18]);
                grid[0].push(2);

                grid.extend((0..18).map(|_| vec![1; 20]));

                let mut last = vec![2];
                last.extend(vec![1; 18]);
                last.push(2);
                grid.push(last);
                grid
            },
            18,
        ),
        // Additional edge cases
        (vec![vec![]], 0),
        (vec![vec![0, 0, 0]], 0),
        (vec![vec![2, 0, 2]], 0),
        (vec![vec![1, 0, 1]], -1),
        (vec![vec![2, 1, 2]], 1),
        (vec![vec![2, 1, 1, 2]], 1),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        oranges_rotting(input.clone())
    }));
}
