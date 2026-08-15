use std::panic::{catch_unwind, AssertUnwindSafe};

pub fn run_tests<F>(
    func: F,
    test_cases: &[(Vec<&str>, i64)],
) -> i32
where
    F: Fn(&[&str]) -> i64,
{
    for (i, (args, expected)) in test_cases.iter().enumerate() {
        match catch_unwind(AssertUnwindSafe(|| func(args))) {
            Ok(result) if result == *expected => {
                println!("[b]✓[/] test case {}\t[green]... ok[/]", i + 1);
            }

            Ok(result) => {
                println!(
                    "[b]x[/] test case {}\t[red]... FAIL[/]\n\
                     \t[b]args[/]: {:?}\n\
                     \t[b]got[/]: [red]{}[/]\n\
                     \t[b]expected[/]: [green]{}[/]",
                    i + 1,
                    args,
                    result,
                    expected
                );

                return 1;
            }

            Err(error) => {
                println!(
                    "[b]x[/] test case {}\t[red]... ERROR[/]\n\
                     \t[b]error[/]: {}",
                    i + 1,
                    format_panic(error)
                );

                return 1;
            }
        }
    }

    println!("\n{} passed!", test_cases.len());
    0
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
