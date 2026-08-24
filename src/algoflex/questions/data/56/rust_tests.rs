fn main() {
    let g1 = vec![
        vec!['1', '1', '1', '1'],
        vec!['0', '0', '0', '0'],
        vec!['1', '1', '1', '1'],
    ];
    let g2 = vec![
        vec!['1', '0', '1', '1'],
        vec!['0', '0', '1', '0'],
        vec!['1', '1', '1', '1'],
    ];
    let g3 = vec![vec![]];
    let g4: Vec<Vec<char>> = (0..10_000).map(|_| vec!['1', '0', '1', '0', '1']).collect();
    let g5: Vec<Vec<char>> = (0..10_000).map(|_| vec!['0', '1', '0', '0', '1']).collect();
    let g6 = vec![vec!['1', '0', '1', '0', '1']; 10_000]; // note: this is 1 row repeated 10000 times, equivalent to g6 in Python? Actually Python g6 is [['1','0','1','0','1'] * 10000] which is a single row of length 50000. So we'll replicate that.
    let g6 = vec![vec!['1', '0', '1', '0', '1']; 10_000]
        .into_iter()
        .flatten()
        .collect::<Vec<_>>(); // This would be wrong; we need a single row with 50000 elements. So we'll create one row with 50000 entries.
                              // Let's fix g6 for clarity:
    let g6: Vec<Vec<char>> = vec![{
        let mut row = Vec::with_capacity(50_000);
        for _ in 0..10_000 {
            row.extend_from_slice(&['1', '0', '1', '0', '1']);
        }
        row
    }];
    let g7: Vec<Vec<char>> = (0..4)
        .map(|j| {
            (0..6_000)
                .map(|i| if (i + j) % 2 == 0 { '0' } else { '1' })
                .collect()
        })
        .collect();
    let g8 = vec![vec!['1']];
    let g9 = vec![vec!['0']];
    let g10 = vec![
        vec!['1', '1', '1', '1', '1'],
        vec!['1', '0', '0', '0', '1'],
        vec!['1', '0', '0', '0', '0'],
        vec!['1', '0', '0', '0', '1'],
        vec!['1', '1', '1', '1', '1'],
    ];

    let test_cases: Vec<((Vec<Vec<char>>,), i32)> = vec![
        ((g1,), 2),
        ((g2,), 2),
        ((g3,), 0),
        ((g4,), 3),
        ((g5,), 2),
        ((g6,), 20001),
        ((g7,), 12000),
        ((g8,), 1),
        ((g9,), 0),
        ((g10,), 1),
        ((vec![vec!['1', '1'], vec!['1', '1']],), 1),
        ((vec![vec!['0', '0'], vec!['0', '0']],), 0),
        ((vec![vec!['1', '0'], vec!['0', '1']],), 2),
    ];

    std::process::exit(run_tests!(&test_cases, |input| { count_islands(&input.0) }));
}
