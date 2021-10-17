class MyCircularDeque:

    def __init__(self, k: int):
        self.maxsize = k
        self.deque = [0 for _ in range(k)]
        self.front = 0
        self.last  = 0
        self.size  = 0

    def insertFront(self, value: int) -> bool: # move and fill
        if self.size == self.maxsize: return False
        
        self.front = (self.front - 1 + self.maxsize) % self.maxsize
        self.deque[self.front] = value
        self.size += 1
        return True
    
    def insertLast(self, value: int) -> bool: # fill and move
        # print (self.size, self.maxsize)
        if self.size == self.maxsize: return False
        
        self.deque[self.last] = value
        self.last = (self.last + 1) % self.maxsize
        self.size += 1
        return True
        
    def deleteFront(self) -> bool:
        if self.size == 0: return False
        
        self.size -= 1
        self.front = (self.front + 1) % self.maxsize
        return True
    
    def deleteLast(self) -> bool:
        if self.size == 0: return False
        
        self.size -= 1
        self.last = (self.last - 1 + self.maxsize) % self.maxsize
        return True
    
    def getFront(self) -> int:
        if self.size == 0: return -1
        
        return self.deque[self.front]
    
    def getRear(self) -> int:
        if self.size == 0: return -1
        
        return self.deque[(self.last - 1 + self.maxsize) % self.maxsize]
    
    def isEmpty(self) -> bool:
        if self.size == 0: return True
        return False

    def isFull(self) -> bool:
        if self.size == self.maxsize: return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()