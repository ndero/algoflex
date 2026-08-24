use std::fmt::Debug;

fn format_value<T: Debug>(value: &T, max_len: usize) -> String {
    let rendered = format!("{value:?}");
    if rendered.len() <= max_len {
        rendered
    } else {
        let truncated: String = rendered.chars().take(max_len).collect();
        format!("{truncated}... [{} chars total]", rendered.len())
    }
}

fn format_panic(error: Box<dyn std::any::Any + Send>) -> String {
    if let Some(message) = error.downcast_ref::<&str>() {
        message.to_string()
    } else if let Some(message) = error.downcast_ref::<String>() {
        message.clone()
    } else {
        "unknown panic".to_string()
    }
}

macro_rules! run_tests {
    ($test_cases:expr, |$input:ident| $call:expr) => {{
        use std::panic::{catch_unwind, AssertUnwindSafe};

        let test_cases = $test_cases;

        'tests: {
            for (i, (input, expected)) in test_cases.iter().enumerate() {
                match catch_unwind(AssertUnwindSafe(|| {
                    let $input = input;
                    $call
                })) {
                    Ok(result) if result == *expected => {
                        println!("[b]✓[/] test case {}\t[green]... ok[/]", i + 1);
                    }

                    Ok(result) => {
                        println!(
                            "[b]x[/] test case {}\t[red]... FAIL[/]\n\
                             \t[b]args[/]: {}\n\
                             \t[b]got[/]: [red]{}[/]\n\
                             \t[b]expected[/]: [green]{}[/]",
                            i + 1,
                            format_value(input, 300),
                            format_value(&result, 300),
                            format_value(expected, 300)
                        );

                        break 'tests 1;
                    }

                    Err(error) => {
                        println!(
                            "[b]x[/] test case {}\t[red]... ERROR[/]\n\
                             \t[b]error[/]: {}",
                            i + 1,
                            format_panic(error)
                        );

                        break 'tests 1;
                    }
                }
            }

            println!("\n{} passed!", test_cases.len());
            0
        }
    }};
}
