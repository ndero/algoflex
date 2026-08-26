fn main() {
    // Create caches
    let mut cache = LRUCache::new(3);
    let mut cache1 = LRUCache::new(100_000);

    for i in 1..150_000 {
        cache1.put(i, i * 10);
    }

    // Store caches in a Vec to allow indexing inside closure
    let mut caches = vec![cache, cache1];

    // Test cases: ((obj_idx, op, key, value_or_none), expected)
    // op: 0 = get, 1 = put
    // for get, value_or_none is None; for put it is Some(value)
    let test_cases: Vec<((usize, u8, i32, Option<i32>), Option<i32>)> = vec![
        // cache (idx 0)
        ((0, 1, 1, Some(10)), None),
        ((0, 1, 2, Some(20)), None),
        ((0, 1, 3, Some(30)), None),
        ((0, 0, 3, None), Some(30)),
        ((0, 0, 4, None), Some(-1)),
        ((0, 0, 2, None), Some(20)),
        ((0, 1, 4, Some(20)), None),
        ((0, 0, 1, None), Some(-1)),
        // cache1 (idx 1)
        ((1, 0, 100_000, None), Some(1_000_000)),
        ((1, 0, 49_999, None), Some(-1)),
        ((1, 0, 49_998, None), Some(-1)),
        ((1, 0, 10, None), Some(-1)),
        ((1, 0, 149_999, None), Some(1_499_990)),
        ((1, 1, 2, Some(20)), None),
        ((1, 0, 49_999, None), Some(-1)),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        let (idx, op, key, val) = *input;
        match op {
            0 => Some(caches[idx].get(key)), // get returns i32, wrap in Some
            1 => {
                caches[idx].put(key, val.unwrap());
                None
            }
            _ => unreachable!(),
        }
    }));
}
