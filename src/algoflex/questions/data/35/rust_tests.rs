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
            Some(6),
            Some(3),
            Some(9),
            None,
            Some(5),
            Some(4),
            Some(9),
        ],
        0,
    );

    let root2 = array_to_tree(
        &[
            Some(6),
            Some(3),
            Some(9),
            None,
            Some(5),
            Some(4),
            Some(9),
        ],
        0,
    );

    let root3 = sorted_to_bst(&(0..100).collect::<Vec<_>>());
    let root4 = sorted_to_bst(&(0..100).collect::<Vec<_>>());

    let root5 = array_to_tree(&[], 0);
    let root6 = array_to_tree(&[], 0);

    let root7 = array_to_tree(&[Some(1), Some(2)], 0);
    let root8 = array_to_tree(&[Some(1), None, Some(2)], 0);

    let root9 = array_to_tree(
        &[
            Some(1),
            Some(2),
            Some(3),
            Some(4),
            Some(5),
            None,
            Some(6),
        ],
        0,
    );

    let root10 = array_to_tree(
        &[
            Some(1),
            Some(2),
            Some(3),
            Some(4),
            Some(5),
            Some(7),
            Some(6),
        ],
        0,
    );

    let root11 = array_to_tree(&[Some(5)], 0);
    let root12 = array_to_tree(&[Some(5)], 0);

    let test_cases = vec![
        ((&root1, &root2), true),
        ((&root3, &root4), true),
        ((&root2, &root3), false),
        ((&root5, &root6), true),
        ((&root4, &root6), false),
        ((&root7, &root8), false),
        ((&root8, &root8), true),
        ((&root9, &root10), false),
        ((&root11, &root12), true),
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| same_binary_tree(input.0, input.1))
    );
}