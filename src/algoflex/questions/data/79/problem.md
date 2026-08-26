### LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache:
- `LRUCache(capacity: int)` - initialize LRU cache with capacity
- `put(key: int, value: int)` - add key value pair to cache or update value if key exists. If number of keys exceeds capacity, evict the least recently used key.
- `get(key: int)` - return value of key if key exists, else return -1

`get` and `put` must run in constant time **O(1)**

### Example
```python
cache = LRUCache(3)
cache.put(1, 10)  # {1:10}
cache.put(2, 20)  # {2:20, 1:10}
cache.put(3, 30)  # {3:30, 2:20, 1:10}
cache.get(3)  # return 30 {3:30, 2:20, 1:10}
cache.get(4)  # return -1 {3:30, 2:20, 1:10}
cache.get(2)  # return 20 {2:20, 3:30, 1:10}
cache.put(4, 40)  # evict LRU key 1:10 {4:40, 2:20, 3:30}
cache.get(1)  # return -1 {4:40, 2:20, 3:30}
```
