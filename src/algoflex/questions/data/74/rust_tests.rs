fn array_to_list(values: &[i32]) -> Option<Box<ListNode>> {
    values
        .iter()
        .rev()
        .fold(None, |next, &val| Some(Box::new(ListNode { val, next })))
}

fn list_to_array(mut head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut result = Vec::new();

    while let Some(node) = head {
        result.push(node.val);
        head = node.next;
    }

    result
}

fn main() {
    let test_cases = vec![
        (vec![1, 2, 3, 4, 5, 6], vec![6, 5, 4, 3, 2, 1]),
        (
            (0..100_000).collect::<Vec<i32>>(),
            (0..100_000).rev().collect::<Vec<i32>>(),
        ),
        (vec![3; 100_000], vec![3; 100_000]),
        (vec![], vec![]),
        (
            {
                let mut values = Vec::with_capacity(100_001);
                values.push(6);
                values.extend(std::iter::repeat_n(0, 99_999));
                values.push(9);
                values
            },
            {
                let mut expected = Vec::with_capacity(100_001);
                expected.push(9);
                expected.extend(std::iter::repeat_n(0, 99_999));
                expected.push(6);
                expected
            },
        ),
        (
            (-100_000..0).collect::<Vec<i32>>(),
            (-100_000..0).rev().collect::<Vec<i32>>(),
        ),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        let head = array_to_list(&input);
        list_to_array(reverse_list(head))
    }));
}
