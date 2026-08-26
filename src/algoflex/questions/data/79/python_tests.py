import sys

# Create the cache instances
cache = LRUCache(3)  # type: ignore # noqa: F821

cache1 = LRUCache(100_000)  # type: ignore # noqa: F821
for i in range(1, 150_000):
    cache1.put(i, i * 10)

# Store instances for dispatching
caches = [cache, cache1]


def lru_op(obj_idx, op, *args):
    """Dispatch get/put operation to the selected cache object."""
    obj = caches[obj_idx]
    if op == "get":
        return obj.get(args[0])
    else:  # op == "put"
        obj.put(args[0], args[1])
        return None


# Test cases: [(obj_idx, "get", key) or (obj_idx, "put", key, value), expected]
test_cases = [
    # cache (idx 0)
    [(0, "put", 1, 10), None],
    [(0, "put", 2, 20), None],
    [(0, "put", 3, 30), None],
    [(0, "get", 3), 30],
    [(0, "get", 4), -1],
    [(0, "get", 2), 20],
    [(0, "put", 4, 20), None],
    [(0, "get", 1), -1],
    # cache1 (idx 1)
    [(1, "get", 100_000), 1_000_000],
    [(1, "get", 49_999), -1],
    [(1, "get", 49_998), -1],
    [(1, "get", 10), -1],
    [(1, "get", 149_999), 1_499_990],
    [(1, "put", 2, 20), None],
    [(1, "get", 49_999), -1],
]


if __name__ == "__main__":
    sys.exit(run_python_tests(lru_op, test_cases))  # type: ignore # noqa: F821
