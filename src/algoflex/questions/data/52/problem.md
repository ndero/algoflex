### Network delay time
Given a network of `n` nodes, labelled 1 to n and a list of travel `times` as directed edges where times[i] = (u, v, w) with u being the source, v the target and w the time it takes for a signal to travel from u to v.

Find the minimum time it takes for a signal from a source node `k` to reach all the other nodes.

Return -1 if it's impossible for all the nodes to receive the signal.

### Example
```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
output = 2
```
