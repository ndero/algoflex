### Calendar add event
Design `MyCalendar` class with a method `book(start: int, end: int) -> bool` that can add an event to the calendar. The book method should return `true` if an event can be successfully added or `false` otherwise.

**Example**

```python
calendar = MyCalendar()
calendar.book(10, 20)  # true
calendar.book(10, 20)  # false - already booked
calendar.book(15, 25)  # false - overlapping with [10, 20)
calendar.book(20, 30)  # true  - new event can start at the end time of another
```

**Constraints**

* `0 <= start, end <= 6 * 10^6` with `start <= end` for every call to `book`. 