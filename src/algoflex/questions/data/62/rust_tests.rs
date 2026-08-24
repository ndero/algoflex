fn main() {
    let h1 = vec![3, 1, 2, 7];
    let h2: Vec<i32> = (0..100_000).collect();

    let mut h3 = vec![0; 100_000];
    h3.extend([3, 1, 2, 7]);

    let mut h4 = vec![0; 60_000];
    h4.push(1);

    let mut h5 = vec![100];
    h5.extend(vec![0; 100_000]);
    h5.push(1);

    let h6 = vec![100];

    let mut h7 = vec![1];
    h7.extend(vec![0; 50]);
    h7.extend([3, 1, 2, 7]);

    let h8: Vec<i32> = vec![];

    let test_cases = vec![
        ((h1,), 3),
        ((h2,), 0),
        ((h3,), 3),
        ((h4,), 0),
        ((h5,), 100_000),
        ((h6,), 0),
        ((h7,), 53),
        ((h8,), 0),
        // Edge cases
        ((vec![1],), 0),
        ((vec![1, 2],), 0),
        ((vec![2, 1],), 0),
        ((vec![1, 1, 1, 1],), 0),
        ((vec![0, 0, 0],), 0),
        ((vec![2, 0, 2],), 2),
        ((vec![3, 0, 0, 3],), 6),
        ((vec![5, 0, 0, 0, 5],), 15),
        ((vec![3, 0, 2, 0, 4],), 7),
        ((vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
        ((vec![4, 2, 0, 3, 2, 5],), 9),
    ];

    std::process::exit(run_tests!(&test_cases, |input| { trap_water(&input.0) }));
}
