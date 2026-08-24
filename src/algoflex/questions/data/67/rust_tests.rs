fn main() {
    fn strs(v: &[&str]) -> Vec<String> {
        v.iter().map(|s| s.to_string()).collect()
    }

    let test_cases = vec![
        // Minimal / edge cases
        ((strs(&["a1 9 2 3 1"]),), strs(&["a1 9 2 3 1"])),
        ((strs(&["a1 act car"]),), strs(&["a1 act car"])),
        ((Vec::<String>::new(),), Vec::<String>::new()),
        // Standard example
        (
            (strs(&[
                "dig1 8 1 5 1",
                "let1 art can",
                "dig2 3 6",
                "let2 own kit dig",
                "let3 art zero",
            ]),),
            strs(&[
                "let1 art can",
                "let3 art zero",
                "let2 own kit dig",
                "dig1 8 1 5 1",
                "dig2 3 6",
            ]),
        ),
        // All digit logs
        (
            (strs(&["d1 1 2 3", "d2 4 5 6", "d3 7 8 9"]),),
            strs(&["d1 1 2 3", "d2 4 5 6", "d3 7 8 9"]),
        ),
        // All letter logs
        (
            (strs(&["l1 abc def", "l2 abc deg", "l3 bcd efg"]),),
            strs(&["l1 abc def", "l2 abc deg", "l3 bcd efg"]),
        ),
        // Same content, different identifiers
        (
            (strs(&["l2 abc def", "l1 abc def", "d1 1 2"]),),
            strs(&["l1 abc def", "l2 abc def", "d1 1 2"]),
        ),
        // Content tie-break by identifier
        (
            (strs(&["a2 same content", "a1 same content", "d1 4 5"]),),
            strs(&["a1 same content", "a2 same content", "d1 4 5"]),
        ),
        // Digit logs maintain original order
        (
            (strs(&["d1 3 4", "d2 1 2", "l1 abc def"]),),
            strs(&["l1 abc def", "d1 3 4", "d2 1 2"]),
        ),
        // Letter content sorting
        (
            (strs(&["l1 zoo alpha", "l2 apple pie", "l3 zoo beta"]),),
            strs(&["l2 apple pie", "l1 zoo alpha", "l3 zoo beta"]),
        ),
        // Mixed with similar prefixes
        (
            (strs(&[
                "let1 art zero",
                "let2 art can",
                "let3 art apple",
                "dig1 3 6",
            ]),),
            strs(&[
                "let3 art apple",
                "let2 art can",
                "let1 art zero",
                "dig1 3 6",
            ]),
        ),
        // Single-word content
        (
            (strs(&["l1 apple", "l2 banana", "d1 5"]),),
            strs(&["l1 apple", "l2 banana", "d1 5"]),
        ),
        // Long content
        (
            (strs(&[
                "l1 this is a long log message",
                "l2 another long log message",
                "d1 9 8 7",
            ]),),
            strs(&[
                "l2 another long log message",
                "l1 this is a long log message",
                "d1 9 8 7",
            ]),
        ),
        // Mixed ordering
        (
            (strs(&["d1 4 2", "l1 abc def", "l2 abc deg", "d2 0 1"]),),
            strs(&["l1 abc def", "l2 abc deg", "d1 4 2", "d2 0 1"]),
        ),
        // Many digit logs at end
        (
            (strs(&["l1 aa bb", "d1 1 1", "d2 2 2", "d3 3 3"]),),
            strs(&["l1 aa bb", "d1 1 1", "d2 2 2", "d3 3 3"]),
        ),
        // Identifier tie-break
        (
            (strs(&["x9 alpha beta", "x1 alpha beta", "x3 alpha beta"]),),
            strs(&["x1 alpha beta", "x3 alpha beta", "x9 alpha beta"]),
        ),
        // Extra edge cases

        // Digit logs interspersed among letter logs.
        (
            (strs(&[
                "d1 9 9",
                "l3 cat dog",
                "d2 1 2",
                "l1 apple pie",
                "d3 5 6",
                "l2 banana split",
                "d4 0 0",
            ]),),
            strs(&[
                "l1 apple pie",
                "l2 banana split",
                "l3 cat dog",
                "d1 9 9",
                "d2 1 2",
                "d3 5 6",
                "d4 0 0",
            ]),
        ),
        // Equal content, identifiers decide.
        (
            (strs(&[
                "id3 hello world",
                "id1 hello world",
                "id2 hello world",
            ]),),
            strs(&["id1 hello world", "id2 hello world", "id3 hello world"]),
        ),
        // Content differs after the first word.
        (
            (strs(&["a1 abc z", "a2 abc a", "a3 abc m"]),),
            strs(&["a2 abc a", "a3 abc m", "a1 abc z"]),
        ),
        // Content outranks identifier.
        (
            (strs(&[
                "z9 apple z",
                "a1 banana a",
                "m5 apple a",
                "b2 banana z",
            ]),),
            strs(&["m5 apple a", "z9 apple z", "a1 banana a", "b2 banana z"]),
        ),
        // Duplicate digit identifiers: stable ordering is required.
        (
            (strs(&["d1 9 9", "d1 1 1", "d1 5 5", "l1 alpha beta"]),),
            strs(&["l1 alpha beta", "d1 9 9", "d1 1 1", "d1 5 5"]),
        ),
        // Mixed single-word content.
        (
            (strs(&["d1 5", "l2 banana", "d2 1", "l1 apple", "d3 9"]),),
            strs(&["l1 apple", "l2 banana", "d1 5", "d2 1", "d3 9"]),
        ),
        // All logs have one content word.
        (
            (strs(&["x3 zebra", "x1 apple", "x2 banana", "d1 3", "d2 1"]),),
            strs(&["x1 apple", "x2 banana", "x3 zebra", "d1 3", "d2 1"]),
        ),
        // Case-sensitive string ordering.
        (
            (strs(&["a1 apple", "a2 Apple", "a3 banana"]),),
            strs(&["a2 Apple", "a1 apple", "a3 banana"]),
        ),
        // Digit logs must remain in exact input order.
        (
            (strs(&["z9 1 1", "a1 2 2", "m5 3 3", "b2 apple pie"]),),
            strs(&["b2 apple pie", "z9 1 1", "a1 2 2", "m5 3 3"]),
        ),
    ];

    std::process::exit(run_tests!(&test_cases, |input| { reorder_logs(&input.0) }));
}
