class MyCalendar:
    import bisect 
    def __init__(self):
        self.event_start = [0, 10**9+1] # consist of (start, end)
        self.event_end = [0, 10**9+1]

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect(self.event_start, start) # 'i' is later event then 'start'
        
        prev_end = self.event_end[i-1]
        next_start = self.event_start[i]
        if prev_end <= start:
            if next_start >= end:
                self.event_start.insert(i, start)
                self.event_end.insert(i, end)
                return True 
        return False 
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)