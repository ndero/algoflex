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
    let root1 = array_to_tree(&[Some(5), Some(4), Some(8), Some(11), None, Some(13), Some(4), Some(7), Some(2), None, None, Some(5), Some(1)], 0);
    let root2 = array_to_tree(&[Some(5)], 0);
    let root3 = array_to_tree(&[Some(12), Some(8), Some(16), Some(4), Some(9), Some(13), Some(18), Some(1)], 0);
    let root4 = array_to_tree(&[Some(9), Some(8), Some(16), None, None, None, Some(18), None, None, None, None, None, None, Some(19)], 0);
    let root5 = array_to_tree(&[Some(9), Some(8), Some(16), None, None, None, Some(18), None, None, None, None, None, Some(15), Some(19)], 0);
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
    let root10 = sorted_to_bst(
        &(-100_000..100_000).collect::<Vec<_>>()
    );
    let root11 = array_to_tree(&[Some(5), None, Some(3)], 0);
    let root12 = array_to_tree(&[Some(4), None, Some(9), None, None, None, Some(12)], 0);
    let root13 = array_to_tree(&[Some(9), Some(8), Some(16), None, None, None, Some(18), None, None, None, None, None, None, Some(18)], 0);

    let test_cases = vec![
        ((&root1,), 15),
        ((&root2,), 0),
        ((&root3,), 43),
        ((&root4,), 34),
        ((&root5,), 34),
        ((&root6,), 25),
        ((&root7,), 0),
        ((&root8,), 1655),
        ((&root9,), 1868),
        ((&root10,), 539765),
        ((&root11,), 3),
        ((&root12,), 21),
        ((&root13,), 34),
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| sum_right_nodes(input.0))
    );
}