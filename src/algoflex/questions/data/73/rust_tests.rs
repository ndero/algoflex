fn main() {
    let test_cases = vec![
        // ===== Minimal Edge Cases =====
        (("a", "a"), "a"),
        (("a", "b"), ""),
        (("ab", "a"), "a"),
        (("ab", "b"), "b"),
        (("aa", "aa"), "aa"),
        (("aa", "aaa"), ""),
        // ===== Classic Example =====
        (("ADOBECODEBANC", "ABC"), "BANC"),
        // ===== Case Sensitivity =====
        (("aAaAaA", "Aa"), "aA"),
        (("aAaAaA", "aa"), "aAa"),
        (("ABC", "abc"), ""),
        // ===== Window At Beginning =====
        (("ABCXYZ", "ABC"), "ABC"),
        (("AABCXYZ", "AABC"), "AABC"),
        // ===== Window At End =====
        (("XYZABC", "ABC"), "ABC"),
        (("XYZAAABC", "AABC"), "AABC"),
        // ===== Window In Middle =====
        (("XYZABCXYZ", "ABC"), "ABC"),
        (("ZZZABCZZZ", "ABC"), "ABC"),
        // ===== Repeated Characters In T =====
        (("AAABBC", "AABC"), "AABBC"),
        (("ABAACBAB", "ABC"), "ACB"),
        (("ABAACBAB", "AABC"), "BAAC"),
        // ===== All Characters Same =====
        (("aaaaaaa", "aaa"), "aaa"),
        (("aaaaaaa", "aaaaaa"), "aaaaaa"),
        (("aaaaaaa", "aaaaaaaa"), ""),
        // ===== No Possible Window =====
        (("abcdef", "gh"), ""),
        (("short", "longer"), ""),
        // ===== Tight Windows =====
        (("abc", "ac"), "abc"),
        (("cab", "ab"), "ab"),
        (("bba", "ab"), "ba"),
        // ===== Many Extra Characters =====
        (("aaaaaaaaaabbbbbcdd", "abcdd"), "abbbbbcdd"),
        (("xyyzyzyx", "xyz"), "zyx"),
        // ===== Multiple Possible Windows =====
        (("aaflslflsldkalskaaa", "aaa"), "aaa"),
        (("abdabca", "abc"), "abc"),
        // ===== Large Duplicate Stress =====
        (("ABABABABABABABABAB", "AABB"), "ABAB"),
        (("AAABBBCCC", "ABC"), "ABBBC"),
        // ===== Exact Full Coverage =====
        (("abc", "abc"), "abc"),
        // ===== Additional Edge Cases =====
        (("aaaaab", "ab"), "ab"),
        (("aabbcc", "abc"), "abbc"),
        (("aabbcc", "aabc"), "aabbc"),
        (("abaaca", "aaa"), "abaa"),
        (("xxabxcax", "abc"), "abxc"),
        (("abcdefg", "d"), "d"),
        (("xxxyyyxxx", "xxx"), "xxx"),
        (("bbbaaaaccc", "aaa"), "aaa"),
        (("abcxxxxxxxxxxd", "ad"), "abcxxxxxxxxxxd"),
        (("zzzaaaabzzz", "aab"), "aab"),
        (("cabwefgewcwaefgcf", "cae"), "cwae"),
        (("aAbBAa", "AB"), "BA"),
        (("aabc", "aabcaa"), ""),
        (("abc", "aabc"), ""),
        (("xabcx", "xabx"), "xabcx"),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        min_window(input.0, input.1)
    }));
}
