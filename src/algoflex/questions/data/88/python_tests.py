import sys

test_cases = [
    # Zero / single digit
    [(0,), 0],
    [(1,), 1],
    [(-1,), -1],
    [(5,), 5],
    [(-9,), -9],
    # Basic positive integers
    [(12,), 21],
    [(123,), 321],
    [(1234,), 4321],
    [(100,), 1],
    [(120,), 21],
    # Basic negative integers
    [(-12,), -21],
    [(-123,), -321],
    [(-1234,), -4321],
    [(-100,), -1],
    [(-120,), -21],
    # Repeated digits
    [(11,), 11],
    [(111,), 111],
    [(1221,), 1221],
    [(1001,), 1001],
    [(12321,), 12321],
    # Zeros in the middle / trailing zeros
    [(10,), 1],
    [(101,), 101],
    [(1000,), 1],
    [(10500,), 501],
    [(-10500,), -501],
    # Larger values
    [(123456789,), 987654321],
    [(-123456789,), -987654321],
    [(1534236469,), 0],  # Reversed value overflows int32
    [(-1534236469,), 0],  # Reversed value overflows int32
    # 32-bit boundaries
    [(2147483647,), 0],  # Reversed value overflows
    [(-2147483648,), 0],  # Reversed value overflows
]

if __name__ == "__main__":
    sys.exit(run_python_tests(reverse_integer, test_cases))  # noqa: F821 #type: ignore
