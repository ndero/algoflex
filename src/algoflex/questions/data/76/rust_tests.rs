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
    // Test cases: ((list1, list2), expected_merged_list)
    let test_cases: Vec<((Vec<i32>, Vec<i32>), Vec<i32>)> = vec![
        // Basic merging
        (
            (vec![2, 4, 6, 6, 12, 22], vec![3, 7, 8, 9]),
            vec![2, 3, 4, 6, 6, 7, 8, 9, 12, 22],
        ),
        // Both empty
        ((vec![], vec![]), vec![]),
        // One empty, one non-empty
        ((vec![], vec![0]), vec![0]),
        ((vec![1, 2, 3], vec![]), vec![1, 2, 3]),
        // Single element each, equal values
        ((vec![2], vec![2]), vec![2, 2]),
        ((vec![1], vec![2]), vec![1, 2]),
        ((vec![5], vec![3]), vec![3, 5]),
        // Large range merging
        (
            ((0..60_000).collect(), (-100..0).collect()),
            (-100..60_000).collect(),
        ),
        // Many duplicates
        (
            (vec![1; 1_000], vec![2; 2_000]),
            vec![1; 1_000]
                .into_iter()
                .chain(vec![2; 2_000].into_iter())
                .collect(),
        ),
        ((vec![0; 500], vec![0; 500]), vec![0; 1000]),
        // Negative numbers and mixed
        (
            (vec![-5, -3, 1, 4], vec![-4, -1, 0, 2]),
            vec![-5, -4, -3, -1, 0, 1, 2, 4],
        ),
        // Alternating values
        (
            (vec![1, 3, 5, 7], vec![2, 4, 6, 8]),
            vec![1, 2, 3, 4, 5, 6, 7, 8],
        ),
        ((vec![1, 4, 7], vec![2, 5, 8]), vec![1, 2, 4, 5, 7, 8]),
        // Uneven lengths
        ((vec![1, 2, 3, 4, 5], vec![6]), vec![1, 2, 3, 4, 5, 6]),
        ((vec![10, 20], vec![1, 2, 3, 30]), vec![1, 2, 3, 10, 20, 30]),
        // Large lists with overlap
        (
            ((0..100).step_by(2).collect(), (1..100).step_by(2).collect()),
            (0..100).collect(),
        ),
        // Duplicate values interleaved
        (
            (vec![1, 1, 2, 3], vec![1, 2, 2, 3]),
            vec![1, 1, 1, 2, 2, 2, 3, 3],
        ),
        // Very large lists (10^5 each) to test performance
        (
            (
                (0..100_000).step_by(2).collect(),
                (1..100_000).step_by(2).collect(),
            ),
            (0..100_000).collect(),
        ),
        // Mixed positive and negative large
        (
            ((-50_000..0).collect(), (0..50_000).collect()),
            (-50_000..50_000).collect(),
        ),
        // Single elements repeated
        ((vec![5; 10_000], vec![5; 10_000]), vec![5; 20_000]),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        let (arr1, arr2) = input;
        let l1 = array_to_list(arr1);
        let l2 = array_to_list(arr2);
        let merged = merge_list(l1, l2);
        list_to_array(merged)
    }));
}
