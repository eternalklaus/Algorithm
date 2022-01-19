class Solution:
    def reverseBits(self, n: int) -> int:
        from math import log
        # 5 -> 101 so log2(4) + 1
        output, rounds = 0, 0
        
        for rounds in range(32): # 32!32!
            lowermostbit = n % 2
            output |= (lowermostbit << (32-rounds-1))
            
            n = n // 2
            rounds += 1
        return output 
            