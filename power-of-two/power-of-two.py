class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        quo = n
        rem = 0
        if quo == 0: return False # corner case
        
        while True:
            if quo == 1 and rem == 0: 
                return True 
            if rem == 1:
                return False 
            quo, rem = quo//2, quo%2
        
            