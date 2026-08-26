use std::panic;

fn main() {
    let mut calendar = MyCalendar::new();

    let test_cases: Vec<((i32, i32), bool)> = vec![
        ((10, 20), true),
        ((10, 20), false),
        ((15, 25), false),
        ((20, 30), true),
        ((30, 31), true),
        ((100, 2000), true),
        ((2_000, 6_000_000), true),
        ((3_000, 50_000), false),
        ((10_000, 20_000), false),
        ((0, 6_000_000), false),
        ((55_556, 3_000_000), false),
        ((2000, 2020), false),
        ((5_999_999, 6_000_001), false),
        ((100_000, 200_000), false),
        ((31, 41), true),
        ((42, 50), true),
        ((50, 60), true),
        ((60, 70), true),
        ((70, 80), true),
        ((80, 90), true),
        ((90, 100), true),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        let (start, end) = *input;
        calendar.book(start, end)
    }));
}
