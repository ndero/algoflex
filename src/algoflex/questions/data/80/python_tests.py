import sys

hm = MyHashMap()  # type: ignore # noqa: F821


def hashmap_op(op: str, key: int, value: int = 0):
    """Dispatch operation to the shared hash map object."""
    if op == "put":
        hm.put(key, value)
        return None
    elif op == "get":
        return hm.get(key)
    elif op == "remove":
        hm.remove(key)
        return None


# Test cases: [(op, key, value), expected]
# value is ignored for get/remove
test_cases = [
    # Basic put/get
    [("put", 1, 10), None],
    [("put", 2, 20), None],
    [("get", 1, 0), 10],
    [("get", 2, 0), 20],
    [("get", 3, 0), -1],
    # Overwrite value
    [("put", 1, 100), None],
    [("get", 1, 0), 100],
    # Remove key
    [("remove", 1, 0), None],
    [("get", 1, 0), -1],
    # Remove non-existing
    [("remove", 999, 0), None],
    [("get", 999, 0), -1],
    # Key = 0 edge case
    [("put", 0, 5), None],
    [("get", 0, 0), 5],
    [("remove", 0, 0), None],
    [("get", 0, 0), -1],
    # Max key boundary
    [("put", 10**6, 123), None],
    [("get", 10**6, 0), 123],
    [("put", 10**6, 456), None],
    [("get", 10**6, 0), 456],
    [("remove", 10**6, 0), None],
    [("get", 10**6, 0), -1],
    # Value = 0 edge case
    [("put", 50, 0), None],
    [("get", 50, 0), 0],
    # Multiple inserts
    [("put", 10, 1), None],
    [("put", 20, 2), None],
    [("put", 30, 3), None],
    [("get", 10, 0), 1],
    [("get", 20, 0), 2],
    [("get", 30, 0), 3],
    # Interleaving remove
    [("remove", 20, 0), None],
    [("get", 20, 0), -1],
    [("get", 10, 0), 1],
    [("get", 30, 0), 3],
    # Reinsert removed key
    [("put", 20, 200), None],
    [("get", 20, 0), 200],
    # Many sequential inserts (collision-like)
    [("put", 1001, 1), None],
    [("put", 2001, 2), None],
    [("put", 3001, 3), None],
    [("get", 1001, 0), 1],
    [("get", 2001, 0), 2],
    [("get", 3001, 0), 3],
    # Overwrite after many ops
    [("put", 10, 999), None],
    [("get", 10, 0), 999],
    # Additional edge cases
    [("put", -1, 42), None],
    [("get", -1, 0), 42],
    [("put", -1, -42), None],
    [("get", -1, 0), -42],
    [("remove", -1, 0), None],
    [("get", -1, 0), -1],
    [("put", 10**6 + 1, 7), None],
    [("get", 10**6 + 1, 0), 7],
    [("remove", 10**6 + 1, 0), None],
]


if __name__ == "__main__":
    sys.exit(run_python_tests(hashmap_op, test_cases))  # type: ignore # noqa: F821
