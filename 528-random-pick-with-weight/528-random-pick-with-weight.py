class Solution:
    def __init__(self, w: List[int]):
        self.totals = [] 
        # [5,3,4] -> [5,8,12] random(12) -> 6 
        total = 0
        for n in w:
            total += n 
            self.totals.append(total)
            
        
    # O(nlogn) 
    def pickIndex(self) -> int:
        # sampling from 0 to totals[-1]
        r = random.randrange(self.totals[-1])
        return bisect.bisect(self.totals, r)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()