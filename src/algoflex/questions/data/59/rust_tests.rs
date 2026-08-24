fn main() {
    let s1 = "ab".repeat(100);
    let s2 = "a".repeat(100);
    let s3 = "abcdefghijklmnopqrstuvwxyz".to_string();
    let s4 = format!("{}b{}", "a".repeat(1000), "a".repeat(1000));
    let s5 = format!("{}b{}", "a".repeat(1000), "a".repeat(50));

    let test_cases: Vec<((String,), String)> = vec![
        (("babad".to_string(),), "bab".to_string()),
        (("abcde".to_string(),), "a".to_string()),
        ((s1.clone(),), format!("a{}", "ba".repeat(99))),
        ((s2.clone(),), s2.clone()),
        ((s3.clone(),), "a".to_string()),
        ((s4.clone(),), s4.clone()),
        ((s5.clone(),), "a".repeat(1000)),
        (("".to_string(),), "".to_string()),
        (("cbbd".to_string(),), "bb".to_string()),
        (("a".to_string(),), "a".to_string()),
        (("aa".to_string(),), "aa".to_string()),
        (("aaa".to_string(),), "aaa".to_string()),
        (("abcba".to_string(),), "abcba".to_string()),
    ];

    std::process::exit(run_tests!(&test_cases, |input| lps(&input.0)));
}
