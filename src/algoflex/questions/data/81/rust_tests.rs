fn main() {
    let test_cases = vec![
        // Single digits
        ((0,), true),
        ((1,), true),
        ((7,), true),
        ((9,), true),
        // Basic palindromes
        ((11,), true),
        ((22,), true),
        ((121,), true),
        ((1221,), true),
        ((-12321,), false),
        ((123321,), true),
        ((-1234321,), false),
        ((-12344321,), false),
        ((123454321,), true),
        // Basic non-palindromes
        ((10,), false),
        ((12,), false),
        ((123,), false),
        ((1234,), false),
        ((12345,), false),
        ((123456,), false),
        ((12021,), true),
        ((123451,), false),
        // Numbers with zeros
        ((100,), false),
        ((101,), true),
        ((1001,), true),
        ((10001,), true),
        ((10010,), false),
        ((100001,), true),
        ((1000001,), true),
        ((1000000,), false),
        // Negative numbers
        ((-1,), false),
        ((-11,), false),
        ((-121,), false),
        ((-1221,), false),
        ((-12321,), false),
        // Numbers containing zeros in the middle
        ((10201,), true),
        ((10301,), true),
        ((10501,), true),
        ((1002001,), true),
        ((10020001,), false),
        ((102030201,), true),
        ((102030401,), false),
        // i32 boundary values
        ((2_147_483_647,), false),
        ((-2_147_483_648,), false),
        // Repeated digits
        ((111,), true),
        ((1111,), true),
        ((11111,), true),
        ((-222222,), false),
        ((-999999,), false),
        // Almost-palindromes
        ((11211,), true),
        ((12131,), false),
        ((-12331,), false),
        ((12341,), false),
        ((-123451,), false),
        ((1234322,), false),
    ];

    std::process::exit(run_tests!(&test_cases, |input| is_palindrome(input.0)));
}
