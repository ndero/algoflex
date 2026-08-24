fn main() {
    let n1 = 1;
    let e1: Vec<Vec<i32>> = vec![];
    let k1 = 0;

    let n2 = 2;
    let e2 = vec![vec![0, 1, 3]];
    let k2 = 5;

    let n3 = 2;
    let e3 = vec![vec![0, 1, 10]];
    let k3 = 5;

    let n4 = 5;
    let e4 = vec![vec![0, 1, 1], vec![1, 2, 1], vec![2, 3, 1], vec![3, 4, 1]];
    let k4 = 1;

    let n5 = 5;
    let e5 = vec![vec![0, 1, 1], vec![0, 2, 1], vec![0, 3, 1], vec![0, 4, 1]];
    let k5 = 1;

    let n6 = 6;
    let e6 = vec![vec![0, 1, 1], vec![1, 2, 1], vec![3, 4, 1]];
    let k6 = 2;

    let n7 = 4;
    let e7 = vec![
        vec![0, 1, 1],
        vec![0, 2, 1],
        vec![0, 3, 1],
        vec![1, 2, 1],
        vec![1, 3, 1],
        vec![2, 3, 1],
    ];
    let k7 = 2;

    let n8 = 4;
    let e8 = vec![vec![0, 1, 10], vec![0, 2, 1], vec![2, 1, 1], vec![1, 3, 1]];
    let k8 = 2;

    let n9 = 3;
    let e9 = vec![
        vec![0, 1, 10],
        vec![0, 1, 1], // multiple edges, shortest is 1
        vec![1, 2, 1],
    ];
    let k9 = 2;

    let n10 = 5;
    let e10 = vec![vec![0, 1, 5], vec![1, 2, 5], vec![2, 3, 5], vec![3, 4, 5]];
    let k10 = 100;

    // The `cities` edges (used in the first three test cases)
    let cities = vec![
        vec![0, 4, 10],
        vec![0, 8, 25],
        vec![0, 1, 10],
        vec![0, 2, 30],
        vec![0, 3, 20],
        vec![8, 4, 60],
        vec![4, 5, 60],
        vec![5, 3, 70],
        vec![3, 6, 10],
        vec![6, 7, 5],
        vec![1, 7, 50],
    ];

    let test_cases = vec![
        ((9, cities.clone(), 5), 8),
        ((9, cities.clone(), 70), 5),
        ((9, cities.clone(), 1), 8),
        ((n1, e1, k1), 0),
        ((n2, e2, k2), 1),
        ((n3, e3, k3), 1),
        ((n4, e4, k4), 4),
        ((n5, e5, k5), 4),
        ((n6, e6, k6), 5),
        ((n7, e7, k7), 3),
        ((n8, e8, k8), 3),
        ((n9, e9, k9), 2),
        ((n10, e10, k10), 4),
        // Edge cases
        ((5, vec![], 100), 4),
        ((4, vec![vec![0, 1, 1], vec![1, 2, 1], vec![2, 3, 1]], 0), 3),
        (
            (
                4,
                vec![vec![0, 1, 10], vec![0, 2, 2], vec![2, 1, 2], vec![1, 3, 2]],
                4,
            ),
            3,
        ),
        ((4, vec![vec![0, 1, 1], vec![2, 3, 1]], 1), 3),
        (
            (3, vec![vec![0, 1, 100], vec![0, 1, 2], vec![1, 2, 2]], 4),
            2,
        ),
    ];

    std::process::exit(run_tests!(&test_cases, |input| {
        reachable_cities(input.0, &input.1, input.2)
    }));
}
