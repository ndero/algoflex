fn array_to_tree(arr: &[Option<i32>], index: usize) -> Option<Box<TreeNode>> {
    let val = arr.get(index)?.as_ref()?;

    Some(Box::new(TreeNode {
        val: *val,
        left: array_to_tree(arr, index * 2 + 1),
        right: array_to_tree(arr, index * 2 + 2),
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

    // Edge cases
    let root6 = array_to_tree(&[Some(5)], 0);
    let root7 = array_to_tree(&[Some(0), Some(0), Some(0)], 0);
    let root8 = array_to_tree(&[Some(-2), Some(-3), None, Some(-4)], 0);
    let root9 = array_to_tree(
        &[
            Some(1),
            Some(2),
            Some(3),
            Some(4),
            Some(5),
            Some(6),
            Some(7),
        ],
        0,
    );

    let test_cases = vec![
        ((&root1, 8), 3),
        ((&root2, 22), 3),
        ((&root2, 20), 1),
        ((&root4, 0), 0),
        ((&root5, 195), 1),
        ((&root5, 1000), 1),
        ((&root5, 40), 0),
        ((&root6, 5), 1),
        ((&root6, 0), 0),
        ((&root7, 0), 5),
        ((&root8, -5), 1),
        ((&root8, -7), 1),
        ((&root9, 7), 3),
    ];

    std::process::exit(run_tests!(&test_cases, |input| count_paths(
        &input.0, input.1
    )));
}
