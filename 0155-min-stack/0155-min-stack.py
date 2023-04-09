class MinStack:

    def __init__(self):
        self.stack = [[float('inf'), float('inf')]] # saves [value, minval]
        
    def push(self, val: int) -> None:
        minval = min(val, self.stack[-1][1])
        self.stack.append([val, minval])

    def pop(self) -> None:
        val, minval = self.stack.pop()

    def top(self) -> int:
        val, minval = self.stack[-1]
        return val

    def getMin(self) -> int:
        val, minval = self.stack[-1]
        return minval


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()