fn main() {
    let test_cases = vec![
        ((4,), "IV"),
        ((23,), "XXIII"),
        ((768,), "DCCLXVIII"),
        ((1,), "I"),
        ((3999,), "MMMCMXCIX"),
        ((369,), "CCCLXIX"),
        ((1318,), "MCCCXVIII"),
        ((1089,), "MLXXXIX"),
        ((2424,), "MMCDXXIV"),
        ((999,), "CMXCIX"),
        // Edge cases
        ((3,), "III"),                // Smallest with repetition
        ((9,), "IX"),                 // Subtractive notation
        ((40,), "XL"),                // Tens subtractive
        ((90,), "XC"),                // Tens subtractive
        ((400,), "CD"),               // Hundreds subtractive
        ((900,), "CM"),               // Hundreds subtractive
        ((3888,), "MMMDCCCLXXXVIII"), // Longest roman numeral
    ];

    std::process::exit(run_tests!(&test_cases, |input| int_to_roman(input.0)));
}
