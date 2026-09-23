import sys

test_cases = [
    # Single symbols
    [("I",), 1],
    [("V",), 5],
    [("X",), 10],
    [("L",), 50],
    [("C",), 100],
    [("D",), 500],
    [("M",), 1000],
    # Basic additive numerals
    [("II",), 2],
    [("III",), 3],
    [("VI",), 6],
    [("VII",), 7],
    [("VIII",), 8],
    # Subtractive notation
    [("IV",), 4],
    [("IX",), 9],
    [("XL",), 40],
    [("XC",), 90],
    [("CD",), 400],
    [("CM",), 900],
    # Common combinations
    [("XIV",), 14],
    [("XIX",), 19],
    [("XLII",), 42],
    [("XLIX",), 49],
    [("XCIX",), 99],
    [("CDXLIV",), 444],
    # Larger / complex numerals
    [("LVIII",), 58],
    [("MCMXCIV",), 1994],
    [("MMXXIV",), 2024],
    [("MMXXVI",), 2026],
    # Boundary values
    [("I",), 1],
    [("MMMCMXCIX",), 3999],
]

if __name__ == "__main__":
    sys.exit(run_python_tests(roman_to_int, test_cases))  # noqa: F821 # type: ignore
