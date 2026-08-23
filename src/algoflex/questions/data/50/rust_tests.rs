fn main() {
    let test_cases = vec![
        (
            vec![
                "flower".to_string(),
                "flow".to_string(),
                "flight".to_string(),
            ],
            "fl".to_string(),
        ),
        (
            vec!["dog".to_string(), "racecar".to_string(), "car".to_string()],
            "".to_string(),
        ),
        (
            vec![
                "algology".to_string(),
                "algologies".to_string(),
                "algologists".to_string(),
                "algometer".to_string(),
                "algometric".to_string(),
                "algometry".to_string(),
                "algophobia".to_string(),
                "algologically".to_string(),
                "algorithm".to_string(),
                "algorism".to_string(),
            ],
            "algo".to_string(),
        ),
        (
            vec![
                "ORGANOMETALLICS".to_string(),
                "ORGANOPHOSPHATE".to_string(),
                "ORGANOTHERAPY ".to_string(),
            ],
            "ORGANO".to_string(),
        ),
        (
            vec!["lower".to_string(), "low".to_string(), "light".to_string()],
            "l".to_string(),
        ),
        (
            vec![
                "SYSTEMATISE".to_string(),
                "SYSTEMATISED".to_string(),
                "SYSTEMATISER".to_string(),
                "SYSTEMATISERS".to_string(),
                "SYSTEMATISES".to_string(),
                "SYSTEMATISING".to_string(),
                "SYSTEMATISM".to_string(),
                "SYSTEMATISMS".to_string(),
                "SYSTEMATIST".to_string(),
            ],
            "SYSTEMATIS".to_string(),
        ),
        (
            vec![
                "garden".to_string(),
                "gardener".to_string(),
                "gardened".to_string(),
                "gardenful".to_string(),
                "gardenia".to_string(),
            ],
            "garden".to_string(),
        ),
        (
            vec![
                "flytrap".to_string(),
                "flyway".to_string(),
                "flyweight".to_string(),
                "flywheel".to_string(),
            ],
            "fly".to_string(),
        ),
        (
            vec!["flower".to_string(), "flow".to_string(), "".to_string()],
            "".to_string(),
        ),
        // Edge cases
        (Vec::<String>::new(), "".to_string()),
        (vec!["hello".to_string()], "hello".to_string()),
        (
            vec!["a".to_string(), "a".to_string(), "a".to_string()],
            "a".to_string(),
        ),
        (
            vec!["abc".to_string(), "ab".to_string(), "a".to_string()],
            "a".to_string(),
        ),
        (vec!["".to_string(), "".to_string()], "".to_string()),
        (
            vec!["same".to_string(), "same".to_string()],
            "same".to_string(),
        ),
    ];

    std::process::exit(run_tests!(&test_cases, |input| longest_common_prefix(
        &input
    )));
}
