fn array_to_tree(arr: &[Option<i32>], index: usize) -> Option<Box<TreeNode>> {
    let val = arr.get(index)?.as_ref()?;

    Some(Box::new(TreeNode {
        val: *val,
        left: array_to_tree(arr, index * 2 + 1),
        right: array_to_tree(arr, index * 2 + 2),
    }))
}

fn sorted_to_bst(nums: &[i32]) -> Option<Box<TreeNode>> {
    if nums.is_empty() {
        return None;
    }

    let mid = nums.len() / 2;

    Some(Box::new(TreeNode {
        val: nums[mid],
        left: sorted_to_bst(&nums[..mid]),
        right: sorted_to_bst(&nums[mid + 1..]),
    }))
}

fn main() {
    let root1 = array_to_tree(
        &[
            Some(3),
            Some(5),
            Some(1),
            Some(6),
            Some(2),
            Some(0),
            Some(8),
            None,
            None,
            Some(7),
            Some(4),
        ],
        0,
    );

    let root2 = array_to_tree(&[Some(1), Some(2)], 0);

    let root3 = sorted_to_bst(&(0..10).collect::<Vec<_>>());

    let root4 = array_to_tree(&[Some(5)], 0);

    let root5 = array_to_tree(&[Some(5), Some(3), Some(7)], 0);
    let root6 = sorted_to_bst(&(0..10_000).collect::<Vec<_>>());

    let test_cases = vec![
        ((&root1, 6, 8), 3),
        ((&root1, 5, 2), 5),
        ((&root2, 2, 1), 1),
        ((&root3, 1, 3), 2),
        ((&root3, 3, 6), 5),
        ((&root3, 0, 9), 5),
        ((&root6, 3, 6), 4),
        ((&root6, 3, 6), 4),
        ((&root6, 500, 5), 312),
        ((&root6, 6700, 9800), 7500),
        ((&root6, 1234, 5678), 5000),
        ((&root6, 111, 999), 625),
        ((&root6, 0, 9999), 5000),
        // Edge cases
        ((&root4, 5, 5), 5),
        ((&root5, 3, 7), 5),
        ((&root5, 5, 7), 5),
        ((&root5, 3, 5), 5),
    ];

    std::process::exit(run_tests!(&test_cases, |input| lowest_common_ancestor(
        input.0, input.1, input.2,
    )));
}
