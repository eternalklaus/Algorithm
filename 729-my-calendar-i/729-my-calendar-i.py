MAX = 10**9+1
class MyCalendar:
    import bisect 
    def __init__(self):
        self.starts = [-1, MAX]
        self.ends = [-1, MAX]

    def book(self, start: int, end: int) -> bool:
        # 근데 bisect 는 한번에 하나밖에 못찾아..!
        idx = bisect.bisect(self.starts, start)

        next_start = self.starts[idx]
        before_end = self.ends[idx-1]

        if before_end <= start and end <= next_start:
            self.starts.insert(idx, start)
            self.ends.insert(idx, end)
            return True 
        return False 
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)