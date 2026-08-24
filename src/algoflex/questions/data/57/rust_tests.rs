fn main() {
    let intervals1 = vec![
        vec![1, 10],
        vec![2, 3],
        vec![4, 8],
        vec![9, 12],
        vec![11, 15],
        vec![16, 18],
        vec![17, 20],
    ];
    let intervals2 = vec![
        vec![5, 7],
        vec![1, 3],
        vec![2, 6],
        vec![8, 10],
        vec![9, 12],
        vec![15, 18],
        vec![17, 20],
        vec![19, 22],
    ];
    let intervals3 = vec![
        vec![1, 2],
        vec![2, 3],
        vec![3, 4],
        vec![5, 6],
        vec![6, 8],
        vec![8, 10],
        vec![10, 12],
    ];
    let intervals4 = vec![
        vec![0, 5],
        vec![1, 4],
        vec![2, 3],
        vec![10, 15],
        vec![12, 18],
        vec![14, 16],
        vec![30, 35],
        vec![32, 40],
        vec![41, 45],
    ];
    let intervals5 = vec![
        vec![1, 4],
        vec![3, 5],
        vec![6, 8],
        vec![7, 9],
        vec![10, 14],
        vec![12, 15],
        vec![16, 18],
        vec![17, 19],
        vec![20, 25],
        vec![22, 30],
        vec![28, 35],
        vec![36, 40],
    ];
    let intervals6: Vec<Vec<i32>> = (0..100_000).map(|i| vec![i, i + 1]).collect();

    let test_cases: Vec<((Vec<Vec<i32>>,), Vec<Vec<i32>>)> = vec![
        (
            (vec![vec![1, 3], vec![2, 6], vec![8, 10], vec![15, 18]],),
            vec![vec![1, 6], vec![8, 10], vec![15, 18]],
        ),
        ((vec![vec![1, 5], vec![5, 10]],), vec![vec![1, 10]]),
        ((vec![vec![3, 11], vec![2, 6]],), vec![vec![2, 11]]),
        ((intervals1,), vec![vec![1, 15], vec![16, 20]]),
        ((intervals2,), vec![vec![1, 7], vec![8, 12], vec![15, 22]]),
        ((intervals3,), vec![vec![1, 4], vec![5, 12]]),
        (
            (intervals4,),
            vec![vec![0, 5], vec![10, 18], vec![30, 40], vec![41, 45]],
        ),
        (
            (intervals5,),
            vec![
                vec![1, 5],
                vec![6, 9],
                vec![10, 15],
                vec![16, 19],
                vec![20, 35],
                vec![36, 40],
            ],
        ),
        ((intervals6,), vec![vec![0, 100_000]]),
        ((vec![],), vec![]),
        ((vec![vec![1, 4]],), vec![vec![1, 4]]),
        ((vec![vec![1, 4], vec![2, 3]],), vec![vec![1, 4]]),
        (
            (vec![vec![1, 4], vec![0, 2], vec![3, 5]],),
            vec![vec![0, 5]],
        ),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        merge_intervals(input.0.clone())
    }));
}
