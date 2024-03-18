class MyCalendar:

    def __init__(self):
        self.sorted_list = []

    def book(self, start: int, end: int) -> bool:
        n = len(self.sorted_list)
        index = bisect.bisect_left(self.sorted_list, [start, end])

        if index > 0 and self.sorted_list[index - 1][1] > start:
            return False
        
        if index < n and self.sorted_list[index][0] < end:
            return False
        
        
        self.sorted_list.insert(index, [start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
