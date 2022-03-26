class Solution:

    def __init__(self, w: List[int]):
        # ex) w = [3,4,1] -> totals = [3, 7, 8]
        # random 0~8 -> 6
        # 
        self.totals = []
        total = 0 
        for n in w:
            total += n
            self.totals.append(total)
            
    def pickIndex(self) -> int:
        r = random.randrange(self.totals[-1])
        output = bisect.bisect(self.totals, r)
        return output 


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()