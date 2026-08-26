fn main() {
    // Create instances
    let arr1 = vec![1, 3, 7, 7, 7, 3, 4, 1, 7];
    let rf1 = RangeFreq::new(&arr1);

    let arr2: Vec<i32> = (0..100_000).collect();
    let rf2 = RangeFreq::new(&arr2);

    let mut arr3: Vec<i32> = (1..100_000).collect();
    arr3.extend(vec![22; 50_000]);
    arr3.extend(vec![-15; 100_000]);
    let rf3 = RangeFreq::new(&arr3);

    // Store instances in a Vec
    let objects = vec![rf1, rf2, rf3];

    // Test cases: ((object_index, left, right, value), expected)
    let test_cases: Vec<((usize, usize, usize, i32), i32)> = vec![
        ((0, 2, 4, 7), 3),
        ((0, 0, 8, 1), 2),
        ((0, 4, 7, 4), 1),
        ((0, 2, 4, 9), 0),
        ((0, 8, 8, 7), 1),
        ((1, 0, 100_000, 897), 1),
        ((1, 0, 100_000, 0), 1),
        ((1, 0, 100_000, 99_999), 1),
        ((1, 0, 10, 7), 1),
        ((1, 50_000, 50_000, 50_000), 1),
        ((2, 0, 250_000, 0), 0),
        ((2, 0, 250_000, 22), 50_001),
        ((2, 0, 250_000, -15), 100_000),
        ((2, 100_000, 150_000, 22), 49_999),
        ((2, 100_000, 150_005, -15), 7),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        let (idx, left, right, value) = *input;
        objects[idx].query(left, right, value)
    }));
}
