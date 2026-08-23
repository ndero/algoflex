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
    let root2 = array_to_tree(&[Some(5)], 0);
    let root3 = array_to_tree(
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
    let root4 = array_to_tree(&[Some(9), Some(8), Some(16)], 0);
    let root5 = array_to_tree(
        &[
            Some(9),
            Some(8),
            Some(16),
            None,
            None,
            None,
            Some(6),
            None,
            None,
            None,
            None,
            None,
            None,
            Some(7),
        ],
        0,
    );
    let root6 = array_to_tree(&[Some(12), Some(3), Some(20), None, Some(5)], 0);
    let root7 = array_to_tree(&[], 0);
    let root8 = array_to_tree(
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
    let root9 = sorted_to_bst(&(0..100).collect::<Vec<_>>());
    let root10 = sorted_to_bst(&(-100_000..100_000).collect::<Vec<_>>());
    let root11 = array_to_tree(&[Some(5), None, Some(3)], 0);
    let root12 = array_to_tree(&[Some(4), None, Some(9), None, None, None, Some(12)], 0);

    let test_cases = vec![
        ((&root1,), vec![7, 11, 2, 4, 5, 5, 13, 1, 8, 4]),
        ((&root2,), vec![5]),
        ((&root3,), vec![7, 11, 2, 4, 5, 13, 8, 4, 1]),
        ((&root4,), vec![8, 9, 16]),
        ((&root5,), vec![8, 9, 16, 7, 6]),
        ((&root6,), vec![3, 5, 12, 20]),
        ((&root7,), vec![]),
        ((&root8,), vec![45, 50, 55, 100, 500, 600, 1000]),
        ((&root9,), (0..100).collect::<Vec<_>>()),
        ((&root10,), (-100_000..100_000).collect::<Vec<_>>()),
        ((&root11,), vec![5, 3]),
        ((&root12,), vec![4, 9, 12]),
    ];

    std::process::exit(run_tests!(&test_cases, |input| in_order(input.0)));
}
