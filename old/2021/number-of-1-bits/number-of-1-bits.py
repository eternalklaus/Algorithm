class Solution:
    def hammingWeight(self, n: int) -> int:
        binstr = bin(n)[2:]
        return binstr.count('1')