class MedianFinder:
    import bisect
    def __init__(self):
        self.nums = []
     
    def addNum(self, num: int) -> None:
        idx = bisect.bisect(self.nums, num)
        self.nums.insert(idx, num)

    def findMedian(self) -> float:
        L = len(self.nums)
        if len(self.nums) % 2: # 1,2,3 // idx = 1
            return self.nums[L//2]
        else: # 1,2,3,4 // idx 1, 2
            return (self.nums[L//2] + self.nums[L//2-1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()