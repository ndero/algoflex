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
            Some(10),
            Some(5),
            Some(-3),
            Some(3),
            Some(2),
            None,
            Some(11),
            Some(3),
            Some(-2),
            None,
            Some(1),
        ],
        0,
    );

    let root2 = array_to_tree(
        &[
            Some(5),
            Some(4),
            Some(8),
            Some(11),
            None,
            Some(13),
            Some(4),
            Some(7),
            Some(2),
            None,
            None,
            Some(5),
            Some(1),
        ],
        0,
    );

    let root4 = array_to_tree(&[], 0);

    let root5 = array_to_tree(
        &[
            Some(5),
            Some(4),
            Some(8),
            Some(11),
            None,
            Some(13),
            Some(4),
            Some(7),
            Some(2),
            None,
            None,
            None,
            None,
            None,
            Some(1),
        ],
        0,
    );

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

    let root10 = array_to_tree(&[Some(-2), Some(-3), None, Some(-4)], 0);

    let root11 = array_to_tree(&[Some(0), Some(0), Some(0)], 0);

    let test_cases = vec![
        ((&root1, 18), true),
        ((&root2, 17), true),
        ((&root2, 26), false),
        ((&root2, 22), true),
        ((&root2, 27), true),
        ((&root4, 0), false),
        ((&root5, 26), true),
        ((&root6, 1000), false),
        ((&root6, 205), true),
        ((&root7, 577), true),
        ((&root7, 411), false),
        ((&root8, -99996), true),
        // Edge cases
        ((&root9, 5), true),
        ((&root9, 0), false),
        ((&root10, -9), true),
        ((&root10, -2), false),
        ((&root11, 0), true),
        ((&root11, 1), false),
    ];

    std::process::exit(run_tests!(&test_cases, |input| has_path_sum(
        input.0, input.1
    )));
}
