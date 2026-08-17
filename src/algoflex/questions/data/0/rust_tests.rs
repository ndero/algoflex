fn main() {
    let mut test_cases = vec![
        (vec!["5", "2", "C", "D", "+", "+", "C"], 30),
        (vec!["9", "C", "6", "D", "C", "C"], 0),
        (vec!["3", "4", "9", "8"], 24),
        (vec!["4", "D", "+", "C", "D"], 28),
        (vec!["1", "C"], 0),
        (
            vec!["1", "1", "+", "+", "+", "+", "+", "+", "+", "+"],
            143,
        ),
        (vec!["1", "D", "D", "D", "D", "D"], 63),
    ];

    test_cases.push((
        ["1", "1"]
            .into_iter()
            .chain(std::iter::repeat_n("+", 27))
            .collect(),
        1_346_268,
    ));

    test_cases.push((
        ["1", "0"]
            .into_iter()
            .chain(std::iter::repeat_n("D", 1_000_000))
            .collect(),
        1,
    ));

    test_cases.push((
        ["1", "1"]
            .into_iter()
            .chain(std::iter::repeat_n("D", 10_000))
            .chain(std::iter::repeat_n("C", 10_001))
            .collect(),
        1,
    ));

    test_cases.push((
        ["1", "1"]
            .into_iter()
            .chain(std::iter::repeat_n("+", 22))
            .chain(std::iter::repeat_n("C", 20))
            .chain(std::iter::repeat_n("+", 20))
            .collect(),
        121_392,
    ));

    test_cases.push((
        ["1", "1", "C", "D", "D", "+"]
            .into_iter()
            .cycle()
            .take(6_000)
            .collect(),
        13_000,
    ));

    std::process::exit(run_tests!(&test_cases, |input| total_score(input)));
}