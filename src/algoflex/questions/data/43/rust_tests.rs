fn main() {
    let test_cases = vec![
        (("math", "arithmetic"), "ath".to_string()),
        (("original", "origin"), "origin".to_string()),
        (("foo", "bar"), "".to_string()),
        (("", "arithmetic"), "".to_string()),
        (
            ("shesellsseashellsatthesea", "isawyouyesterday"),
            "saestea".to_string(),
        ),
        (("@work3r", "m@rxkd35rt"), "@rk3r".to_string()),
    ];

    std::process::exit(run_tests!(&test_cases, |input| longest_common_subsequence(
        input.0, input.1
    )));
}
