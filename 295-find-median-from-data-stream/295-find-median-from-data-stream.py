class MedianFinder:
    import heapq
    def __init__(self):
        # lo -1,-2,-3,-4 // hi 5,6,7,8
        self.hi_minheap = [] 
        self.lo_maxheap = [] 
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.hi_minheap, num)
        minvalue = heapq.heappop(self.hi_minheap)
        heapq.heappush(self.lo_maxheap, -minvalue)
        
        if len(self.lo_maxheap) > len(self.hi_minheap):
            maxvalue = heapq.heappop(self.lo_maxheap)
            heapq.heappush(self.hi_minheap, -maxvalue)
    
    # O(1)
    def findMedian(self) -> float:
        # even 
        if len(self.hi_minheap) == len(self.lo_maxheap):
            return (self.hi_minheap[0] - self.lo_maxheap[0]) / 2 
        else: # odd
            return self.hi_minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()