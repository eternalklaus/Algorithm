class MedianFinder:
    import bisect
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        idx = bisect.bisect(self.nums, num)
        self.nums.insert(idx,num)
        
    def findMedian(self) -> float:
        total = len(self.nums) 
        if total % 2:
            return self.nums[total//2] # 3 --> 1(ok)
        else: # 4 --> 2 + 1
            return (self.nums[total//2] + self.nums[total//2-1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()