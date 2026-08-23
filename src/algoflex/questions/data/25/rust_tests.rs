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
    let root1 = array_to_tree(&[Some(9), Some(8), Some(16)], 0);

    let root2 = array_to_tree(&[Some(9), Some(8), Some(16), Some(4)], 0);

    let root3 = array_to_tree(&[Some(12), Some(3), Some(20), None, Some(5)], 0);

    let root5 = array_to_tree(&[], 0);

    let root6 = array_to_tree(
        &[
            Some(100),
            Some(50),
            Some(600),
            Some(45),
            Some(55),
            Some(500),
            Some(1000),
        ],
        0,
    );

    let root7 = sorted_to_bst(&(0..100).collect::<Vec<_>>());

    let root8 = sorted_to_bst(&(-100_000..100_000).collect::<Vec<_>>());

    // Edge cases
    let root9 = array_to_tree(&[Some(5)], 0);

    let test_cases = vec![
        ((&root1, 5), false),
        ((&root2, 9), true),
        ((&root3, 5), true),
        ((&root5, 4), false),
        ((&root6, 600), true),
        ((&root7, 100), false),
        ((&root8, 1), true),
        // Edge cases
        ((&root9, 5), true),
        ((&root9, 4), false),
    ];

    std::process::exit(run_tests!(&test_cases, |input| bst_contains(
        input.0, input.1
    )));
}
