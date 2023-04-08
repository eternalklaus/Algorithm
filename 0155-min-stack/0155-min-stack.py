class MinStack:
    import bisect 
    from collections import Counter 
    
    def __init__(self):
        self.stack = []
        self.counter = Counter()
        self.sorted = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.counter[val] += 1
        idx = bisect.bisect(self.sorted, val) 
        self.sorted.insert(idx, val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.counter[val] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        for val in self.sorted:
            if self.counter[val]: 
                return val
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()