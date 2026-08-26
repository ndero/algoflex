### Design a hashmap
Design a hashmap, class `MyHashMap` with methods put, get and remove that adds, gets and removes key value pairs.

Implement the MyHashMap class:

- `MyHashMap()` Initializes the object with an empty map.
- `put(int key, int value) -> None` Inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
- `get(int key) -> int` Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- `remove(int key) -> None` Removes the key and its corresponding value if the map contains the mapping for the key.

Don't use the inbuilt hash table libraries, `{}` or `dict`.

### Example
```
hm = MyHashMap()
hm.put(1, 10)  # adds key value pair (1, 10), returns nothing
hm.put(2, 20)
hm.get(1)      # return 10
hm.get(3)      # returns -1, not present
hm.remove(1)   # removes (1, 10) from hashmap, returns nothing
hm.get(1)      # returns -1
```
