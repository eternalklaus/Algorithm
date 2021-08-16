class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        total = 2**p
        if p==1: return 1
        return pow((2**p-2), (total//2-1), (10**9 + 7)) * ((2**p)-1) % (10**9 + 7)