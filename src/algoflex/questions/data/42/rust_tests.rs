fn main() {
    let prices1 = vec![7, 1, 5, 3, 6, 4];
    let prices2 = vec![7, 6, 4, 3, 1];
    let prices3 = vec![0, 0, 0, 0];

    let mut prices4 = vec![4; 2_000];
    prices4.extend(std::iter::repeat_n(15, 1_000));

    let mut prices5 = vec![90; 10_000];
    prices5.extend(std::iter::repeat_n(50, 20_000));

    let prices6 = vec![];
    let prices7: Vec<i32> = (1..100_000).collect();

    let test_cases = vec![
        ((prices1,), 5),
        ((prices2,), 0),
        ((prices3,), 0),
        ((prices4,), 11),
        ((prices5,), 0),
        ((prices6,), 0),
        ((prices7,), 99_998),
        ((vec![1],), 0),
        ((vec![1, 2],), 1),
        ((vec![2, 1],), 0),
        ((vec![5, 5],), 0),
    ];

    std::process::exit(run_tests!(&test_cases, |input| max_profit(&input.0)));
}
