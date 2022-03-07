class MedianFinder:

    def __init__(self):
        self.lo_maxheap = []
        self.hi_minheap = []

    def addNum(self, num: int) -> None:
        heappush(self.hi_minheap, num)
        minval = heappop(self.hi_minheap)
        heappush(self.lo_maxheap, -minval)
        
        if len(self.lo_maxheap) > len(self.hi_minheap): # 맥스가 넘 커졋삼ㅋ
            maxval = -heappop(self.lo_maxheap)
            heappush(self.hi_minheap, maxval)
            
    def findMedian(self) -> float:
        if len(self.hi_minheap) == len(self.lo_maxheap):
            return (self.hi_minheap[0] - self.lo_maxheap[0]) / 2
        return self.hi_minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()