class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: 
            return False
        
        while True:
            n_shift = n >> 1
            if n != 2 * n_shift: break
            
            n = n_shift 
        
        if n_shift == 0:
            return True
        return False
            
            