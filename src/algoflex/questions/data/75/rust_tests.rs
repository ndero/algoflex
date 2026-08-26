fn create_cycle_list(values: &[i32], pos: isize) -> Option<Rc<RefCell<ListNode>>> {
    if values.is_empty() {
        return None;
    }

    let nodes: Vec<Rc<RefCell<ListNode>>> = values
        .iter()
        .map(|&val| Rc::new(RefCell::new(ListNode { val, next: None })))
        .collect();

    // Link consecutive nodes.
    for i in 0..nodes.len() - 1 {
        nodes[i].borrow_mut().next = Some(Rc::clone(&nodes[i + 1]));
    }

    // Connect the tail to the requested node.
    if pos >= 0 && (pos as usize) < nodes.len() {
        nodes[nodes.len() - 1].borrow_mut().next = Some(Rc::clone(&nodes[pos as usize]));
    }

    Some(Rc::clone(&nodes[0]))
}

fn main() {
    let test_cases: Vec<((Vec<i32>, isize), bool)> = vec![
        // ===== Basic: no cycle =====
        ((vec![], -1), false),
        ((vec![1], -1), false),
        ((vec![1, 2], -1), false),
        ((vec![1, 2, 3], -1), false),
        ((vec![1, 2, 3, 4, 5], -1), false),
        // ===== Basic: with cycle =====
        ((vec![1], 0), true),
        ((vec![1, 2], 0), true),
        ((vec![1, 2], 1), true),
        ((vec![3, 2, 0, -4], 1), true),
        ((vec![1, 2, 3, 4, 5], 2), true),
        // ===== Cycle positions =====
        ((vec![1, 2, 3, 4, 5], 0), true),
        ((vec![1, 2, 3, 4, 5], 4), true),
        ((vec![1, 2, 3, 4, 5], 3), true),
        ((vec![1, 2, 3, 4, 5], 1), true),
        ((vec![1], -1), false),
        // ===== Duplicate values =====
        ((vec![1, 1, 1, 1, 1], -1), false),
        ((vec![1, 1, 1, 1, 1], 2), true),
        ((vec![1, 2, 2, 3, 3], -1), false),
        ((vec![1, 2, 2, 3, 3], 1), true),
        // ===== Large lists =====
        (((0..1_000).collect(), -1), false),
        (((0..1_000).collect(), 500), true),
        (((0..10_000).collect(), 0), true),
        (((0..10_000).collect(), 9_999), true),
        // ===== Special patterns =====
        ((vec![-1, -2, -3, -4], 2), true),
        ((vec![0, 0, 0, 0], 1), true),
        ((vec![1_000_000, 1_000_000, 1_000_000], 0), true),
        ((vec![1], 0), true),
        ((vec![1, 2, 3, 4, 5], -1), false),
        // ===== Cycle lengths =====
        ((vec![1, 2, 3, 4], 3), true),
        ((vec![1, 2, 3, 4, 5], 3), true),
        ((vec![1, 2, 3, 4, 5], 1), true),
        // ===== Longer patterns =====
        ((vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), true),
        (((0..100).collect(), 1), true),
        ((vec![1, -1, 2, -2, 3, -3], 2), true),
        // ===== 100k nodes =====
        (((0..100_000).collect(), -1), false),
        (((0..100_000).collect(), 0), true),
        (((0..100_000).collect(), 50_000), true),
        (((0..100_000).collect(), 99_999), true),
        // ===== Large repeated values =====
        ((vec![10_000; 10_000], 5_000), true),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        let head = create_cycle_list(&input.0, input.1);
        has_cycle(head)
    }));
}
