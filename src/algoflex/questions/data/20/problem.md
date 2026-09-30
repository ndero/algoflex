### 0/1 knapsack
Given a knapsack `capacity` and two arrays, the first one for `weights` and the second one for `values`. Add items to the knapsack to maximize the sum of the values of the items that can be added so that the sum of the weights is less than or equal to the knapsack capacity.

You can only either include or not include an item. i.e you can't add a portion of it.

Return a tuple of maximum value and selected items.

**Example**

* **Input:** `capacity = 50`, `weights = [10, 20, 30]`, `values = [60, 100, 120]`
* **Output:** `(220, [0, 1, 1])`

**Constraints**

* `0 <= capacity <= 6000`
* `0 <= weights.length <= 3 * 10^4`
* `0 <= values.length <= 3 * 10^4`
* `5 <= weights[i] <= 100`
* `30 <= values[i] < 150`