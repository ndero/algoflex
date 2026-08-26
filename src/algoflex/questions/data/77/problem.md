### Calendar add event
Design `MyCalendar` with a method `book(start: int, end: int) -> bool` that can add an event to the calendar. The book method should return true if an event can be successfully added or false otherwise.

### Example
```python
calendar = MyCalendar()
calendar.book(10, 20)  # True
calendar.book(10, 20)  # False - already booked
calendar.book(15, 25)  # False - overlapping with [10, 20)
calendar.book(20, 30)  # True  - new event can start at the end time of another
```
