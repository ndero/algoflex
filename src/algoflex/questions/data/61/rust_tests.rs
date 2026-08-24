fn main() {
    let h1 = vec![3, 1, 2, 7];
    let h2: Vec<i32> = (0..1_000).collect();
    let h3 = vec![0; 100_000];
    let h4 = vec![0; 60_000];
    let h5 = vec![1; 100_000];
    let h6 = vec![100];
    let h7 = {
        let mut v = vec![1];
        v.extend(vec![0; 50]);
        v.extend([3, 1, 2, 7]);
        v
    };

    let mut h3_full = h3;
    h3_full.extend([3, 1, 2, 7]);

    let mut h4_full = h4;
    h4_full.push(1);

    let test_cases = vec![
        ((h1,), 9),
        ((h2,), 249_500),
        ((h3_full,), 9),
        ((h4_full,), 0),
        ((h5,), 99_999),
        ((h6,), 0),
        ((h7,), 54),
        // Edge cases
        ((vec![],), 0),
        ((vec![1],), 0),
        ((vec![1, 1],), 1),
        ((vec![0, 0],), 0),
        ((vec![0, 5, 0],), 0),
        ((vec![5, 0, 5],), 10),
        ((vec![2, 2, 2, 2],), 6),
        ((vec![1, 2, 1],), 2),
        ((vec![1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
    ];

    std::process::exit(run_tests!(&test_cases, |input| { max_water(&input.0) }));
}
