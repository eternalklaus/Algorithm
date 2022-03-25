class Solution:
    import random
    import bisect
    def __init__(self, w: List[int]):
        # binary search 미쳤나봐 미친놈인가? 
        self.totals = []
        self.total = 0
        
        self.total = 0
        for n in w:
            self.total += n
            self.totals.append(self.total)
        print (self.totals)

    def pickIndex(self) -> int:
        num = random.randrange(self.total)
        return bisect.bisect(self.totals, num)
        
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()