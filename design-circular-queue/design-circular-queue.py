class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0 for _ in range(self.capacity)] 
        self.front = 0
        self.rear  = -1
        self.total = 0
        # self.size = 0
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False 
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = value 
            self.total += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 
        else:
            self.front = (self.front + 1 + self.capacity) % self.capacity
            self.total -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.total == 0: return True
        return False

    def isFull(self) -> bool:
        if self.total == self.capacity: return True
        return False
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()