fn main() {
    // Create the hash map instance
    let mut hm = MyHashMap::new();

    // Test cases: ((op, key, value), expected)
    // op: 0 = put, 1 = get, 2 = remove
    // value is ignored for get/remove
    let test_cases: Vec<((u8, i32, i32), Option<i32>)> = vec![
        // Basic put/get
        ((0, 1, 10), None),
        ((0, 2, 20), None),
        ((1, 1, 0), Some(10)),
        ((1, 2, 0), Some(20)),
        ((1, 3, 0), Some(-1)),
        // Overwrite value
        ((0, 1, 100), None),
        ((1, 1, 0), Some(100)),
        // Remove key
        ((2, 1, 0), None),
        ((1, 1, 0), Some(-1)),
        // Remove non-existing
        ((2, 999, 0), None),
        ((1, 999, 0), Some(-1)),
        // Key = 0 edge case
        ((0, 0, 5), None),
        ((1, 0, 0), Some(5)),
        ((2, 0, 0), None),
        ((1, 0, 0), Some(-1)),
        // Max key boundary
        ((0, 1_000_000, 123), None),
        ((1, 1_000_000, 0), Some(123)),
        ((0, 1_000_000, 456), None),
        ((1, 1_000_000, 0), Some(456)),
        ((2, 1_000_000, 0), None),
        ((1, 1_000_000, 0), Some(-1)),
        // Value = 0 edge case
        ((0, 50, 0), None),
        ((1, 50, 0), Some(0)),
        // Multiple inserts
        ((0, 10, 1), None),
        ((0, 20, 2), None),
        ((0, 30, 3), None),
        ((1, 10, 0), Some(1)),
        ((1, 20, 0), Some(2)),
        ((1, 30, 0), Some(3)),
        // Interleaving remove
        ((2, 20, 0), None),
        ((1, 20, 0), Some(-1)),
        ((1, 10, 0), Some(1)),
        ((1, 30, 0), Some(3)),
        // Reinsert removed key
        ((0, 20, 200), None),
        ((1, 20, 0), Some(200)),
        // Many sequential inserts
        ((0, 1001, 1), None),
        ((0, 2001, 2), None),
        ((0, 3001, 3), None),
        ((1, 1001, 0), Some(1)),
        ((1, 2001, 0), Some(2)),
        ((1, 3001, 0), Some(3)),
        // Overwrite after many ops
        ((0, 10, 999), None),
        ((1, 10, 0), Some(999)),
        // Additional edge cases
        ((0, -1, 42), None),
        ((1, -1, 0), Some(42)),
        ((0, -1, -42), None),
        ((1, -1, 0), Some(-42)),
        ((2, -1, 0), None),
        ((1, -1, 0), Some(-1)),
        ((0, 1_000_001, 7), None),
        ((1, 1_000_001, 0), Some(7)),
        ((2, 1_000_001, 0), None),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        let (op, key, value) = *input;
        match op {
            0 => {
                hm.put(key, value);
                None
            }
            1 => Some(hm.get(key)),
            2 => {
                hm.remove(key);
                None
            }
            _ => unreachable!(),
        }
    }));
}
