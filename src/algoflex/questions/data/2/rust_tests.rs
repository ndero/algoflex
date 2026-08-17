fn main() {
    let mut test_cases = vec![
        ("[](){}".to_string(), true),
        ("{{}}[][](()".to_string(), false),
        ("[[[()]]]{}".to_string(), true),
        (
            "[[[(((((((()))))))]]]{[{[{[{{({})}}]}]}]}".to_string(),
            false,
        ),
        (
            "[[[([[[[[[[[[[[[[[[()]]]]]]]]]]]]]]])]]]{}".to_string(),
            true,
        ),
        (
            "[[[()]]]{[](){}()[{[{{]}}]}]}".to_string(),
            false,
        ),
        (
            "[[[()]]]{[](){}()[{[{{[]]}}]}]}{}[]((()))".to_string(),
            false,
        ),
        ("[[[()]]]{}".to_string(), true),
        ("[".to_string(), false),
        (
            "{}".repeat(50_000) + &"()".repeat(50_000) + "[]",
            true,
        ),
        (
            "{{{{{{{{{{{{{{{{{{{{{{{{{{{{[[[[[[[[[[()]]]]]]]]]]}}}}}}}}}}}}}}}}}}}}}}}}}}}}"
                .to_string(),
            true,
        ),
    ];

    test_cases.push((
        "[".to_string() + &"()".repeat(100_000) + ")",
        false,
    ));

    test_cases.push((
        "[".to_string() + &"()".repeat(100_000) + "]",
        true,
    ));

    std::process::exit(run_tests!(&test_cases, |input| is_valid(input)));
}