def format_arg(value, max_length=80, max_items=10):
    if isinstance(value, str):
        if len(value) > max_length:
            return repr(value[:max_length]) + "..."
        return repr(value)

    if isinstance(value, (list, tuple, set)):
        if len(value) > max_items:
            items = ", ".join(
                format_arg(item, max_length, max_items) for item in list(value)[:3]
            )
            return f"[{items}, ... ({len(value)} items)]"

        return repr(value)

    return repr(value)


def format_result(value, max_length=100, max_items=10):
    if isinstance(value, str):
        if len(value) > max_length:
            return repr(value[:max_length]) + "..."
        return repr(value)

    if isinstance(value, (list, tuple, set)):
        if len(value) > max_items:
            items = ", ".join(
                format_result(item, max_length, max_items) for item in list(value)[:3]
            )
            return f"[{items}, ... ({len(value)} items)]"

        return repr(value)

    if isinstance(value, dict):
        if len(value) > max_items:
            items = ", ".join(
                f"{format_result(k)}: {format_result(v)}"
                for k, v in list(value.items())[:3]
            )
            return f"{{{items}, ... ({len(value)} items)}}"

        return repr(value)

    return repr(value)


def run_python_tests(func, test_cases) -> int:
    for i, [args, expected] in enumerate(test_cases):
        try:
            result = func(*args)
            if result == expected:
                print(f"[green][b]✓[/][/] test case {i + 1} \tPASS")
            else:
                parameters = ", ".join(format_arg(arg) for arg in args)
                print(
                    f"[red][b]✗[/][/] test case {i + 1} \tFAIL\n"
                    f"\t[b]args[/]: {parameters}\n"
                    f"\t[b]got[/]: [red]{format_result(result)}[/]\n"
                    f"\t[b]expected[/]: [green]{format_result(expected)}[/]"
                )
                return 1
        except Exception as e:  # noqa: BLE001
            print(
                f"[red][b]✗[/][/] test case {i + 1} \tERROR\n\t[b][red]error[/][/]: {e}"
            )
            return 1
    print(f"\n{len(test_cases)} passed!")
    return 0
