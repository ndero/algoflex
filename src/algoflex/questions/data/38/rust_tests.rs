fn _generate_parentheses(n: usize) -> Vec<String> {
    let mut res = Vec::new();
    let mut path = String::with_capacity(2 * n);

    fn backtrack(
        n: usize,
        open: usize,
        close: usize,
        path: &mut String,
        res: &mut Vec<String>,
    ) {
        if path.len() == 2 * n {
            res.push(path.clone());
            return;
        }

        if open < n {
            path.push('(');
            backtrack(n, open + 1, close, path, res);
            path.pop();
        }

        if close < open {
            path.push(')');
            backtrack(n, open, close + 1, path, res);
            path.pop();
        }
    }

    backtrack(n, 0, 0, &mut path, &mut res);
    res
}

fn main() {
    let test_cases = vec![
        ((3,), _generate_parentheses(3)),
        ((1,), _generate_parentheses(1)),
        ((2,), _generate_parentheses(2)),
        ((0,), _generate_parentheses(0)),
        ((12,), _generate_parentheses(12)),
        ((5,), _generate_parentheses(5)),
    ];

    std::process::exit(
        run_tests!(&test_cases, |input| generate_parentheses(input.0))
    );
}