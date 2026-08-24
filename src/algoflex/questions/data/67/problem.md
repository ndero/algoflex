### Reorder log files
Given a `logs` array containing logs, sort it such that all letter logs come before digit logs and letter logs are sorted by content first then identifier if there is a tie.

Make sure the digit logs stay in their original order (stable sort).

> letter logs - content starts with a letter
> digit logs - content starts with a digit.
> first word of each log is the identifier. i.e each log looks like: 'identifier content...'

### Example
```
logs = ["l2 abc def", "l1 abc def", "d1 1 2"]
output = ["l1 abc def", "l2 abc def", "d1 1 2"]
```
