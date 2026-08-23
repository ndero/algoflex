fn main() {
    let s1 = "abca".repeat(360);
    let s2 = "bca".repeat(500);
    let s3 = "abc".repeat(400);
    let s4 = "xyz".repeat(300);

    let test_cases = vec![
        (("brain", "drain"), "rain"),
        (("math", "arithmetic"), "th"),
        ((s1.as_str(), s2.as_str()), "abca"),
        ((s3.as_str(), s4.as_str()), ""),
        (("blackmarket", "stagemarket"), "market"),
        (
            ("theoldmanoftheseaissowise", "sowisetheoldmanoftheseais"),
            "theoldmanoftheseais",
        ),
        // Edge cases
        (("", ""), ""),              // Both empty
        (("a", ""), ""),             // One empty
        (("", "b"), ""),             // Other empty
        (("a", "a"), "a"),           // Single character match
        (("a", "b"), ""),            // Single character no match
        (("abc", "abc"), "abc"),     // Identical strings
        (("aaaa", "aa"), "aa"),      // Repeated characters
        (("abcdef", "fedcba"), "a"), // Reversed strings
    ];

    std::process::exit(run_tests!(&test_cases, |input| longest_common_substring(
        input.0, input.1
    )));
}
