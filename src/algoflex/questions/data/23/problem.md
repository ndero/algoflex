### Ways to make change
Write an algorithm to determine how many ways there are to make change for a given input, `cents` of US currency.

There are four types of common coins in US currency:
  - quarters (25 cents)
  - dimes (10 cents)
  - nickels (5 cents)
  - pennies (1 cent)

**Example**

* **Input:** `cents = 15`
* **Output:** `6`
* **How:** There are 6 ways to make change for 15 cents:
  1. A dime and a nickel
  2. A dime and 5 pennies
  3. 3 nickels
  4. 2 nickels and 5 pennies
  5. A nickel and 10 pennies
  6. 15 pennies

**Constraints**

* `0 <= cents <= 10^4`