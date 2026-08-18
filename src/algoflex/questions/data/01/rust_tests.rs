fn main() {
let test_cases = vec![
    (
        "abcdddeeeeaabbbb".to_string(),
        vec![[3, 5], [6, 9], [12, 15]],
    ),
    (
        "xxxcyyyyydkkkkkk".to_string(),
        vec![[0, 2], [4, 8], [10, 15]],
    ),
    (
        "abcdddeeeeaabbbb".repeat(6),
        vec![
            [3, 5],
            [6, 9],
            [12, 15],
            [19, 21],
            [22, 25],
            [28, 31],
            [35, 37],
            [38, 41],
            [44, 47],
            [51, 53],
            [54, 57],
            [60, 63],
            [67, 69],
            [70, 73],
            [76, 79],
            [83, 85],
            [86, 89],
            [92, 95],
        ],
    ),
    ("abcd".to_string(), vec![]),
    ("aabbccdd".to_string(), vec![]),
    ("".to_string(), vec![]),
    ("abcdefffghijkl".to_string(), vec![[5, 7]]),
    ("abcdeffghijkl".repeat(100_000), vec![]),
    (
        format!("{}kkk", "abcdeffghijkl".repeat(100_000)),
        vec![[1_300_000, 1_300_002]],
    ),
    (
        format!("kkk{}", "abcdeffghijkl".repeat(100_000)),
        vec![[0, 2]],
    ),
    (
        "abcdefffghijkl".repeat(100_000),
        (0..100_000)
            .map(|i| [5 + i * 14, 7 + i * 14])
            .collect(),
    ),
];
    std::process::exit(run_tests!(&test_cases, |input| repeated(input)));
}