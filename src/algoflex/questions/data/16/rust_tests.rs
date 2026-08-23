fn main() {
    let s1 = "aadsfasf absbs bbab cadsfafs ".repeat(100_000);
    let expected = "a a b c ".repeat(100_000);
    let expected = expected.trim_end();

    let test_cases = vec![
        (
            (
                vec!["cat", "bat", "rat"]
                    .iter()
                    .map(|s| s.to_string())
                    .collect(),
                "the cattle was rattled by the battery",
            ),
            "the cat was rat by the bat",
        ),
        (
            (
                vec!["a", "b", "c"].iter().map(|s| s.to_string()).collect(),
                "aadsfasf absbs bbab cadsfafs",
            ),
            "a a b c",
        ),
        (
            (
                vec!["a", "b", "c"].iter().map(|s| s.to_string()).collect(),
                s1.as_str(),
            ),
            expected,
        ),
        (
            (
                vec![
                    'a', 'c', 'e', 'g', 'h', 'i', 'k', 'm', 'n', 'p', 'r', 's', 'u', 'v', 'w', 'x',
                    'y', 'z',
                ]
                .iter()
                .map(|c| c.to_string())
                .collect(),
                "the quick brown fox jumped over the lazy dog",
            ),
            "the quick brown fox jumped over the lazy dog",
        ),
        (
            (
                ('a'..='z').map(|c| c.to_string()).collect(),
                "the quick brown fox jumped over the lazy dog",
            ),
            "t q b f j o t l d",
        ),
        ((('a'..='z').map(|c| c.to_string()).collect(), ""), ""),
        // Edge cases
        ((vec!["a".to_string()], "a"), "a"), // Single root, single word
        ((vec!["ab".to_string()], "abc"), "ab"), // Root is prefix
        ((vec!["abc".to_string()], "ab"), "ab"), // Word shorter than root
        (
            (vec!["cat".to_string(), "cattle".to_string()], "cattle"),
            "cat",
        ), // Multiple roots, shortest wins
        ((vec![], "hello world"), "hello world"), // No roots
        (
            (
                vec!["pre".to_string(), "post".to_string()],
                "prefix postfix prepare",
            ),
            "pre post pre",
        ), // Non-contiguous matches
    ];

    std::process::exit(run_tests!(&test_cases, |input| replace_words(
        &input.0, input.1
    )));
}
