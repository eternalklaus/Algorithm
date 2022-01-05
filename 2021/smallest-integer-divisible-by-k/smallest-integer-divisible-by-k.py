class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        n = 1
        output = 1 # length
        
        while n < float('inf'): 
            if n % k == 0:
                return output 
            output += 1
            n = n * 10 + 1
        return -1 
        