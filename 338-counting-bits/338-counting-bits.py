class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 1 10 11 100 101 110 111 1000 1001 1010 1011 
        # 0 1. 1  2.  1.  2.  2.  3.   1.   2.   2.   3
        # repeating...
        # 1, 2, 4, 8, 16, ...
        
        
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        output = [0, 1]
        counter, roundnum = 0, 1
        for i in range(2, n+1):
            if counter == 0:
                counter = 2 ** roundnum # reset counter 
                roundnum += 1 
            output.append(1 + output[i- (2**roundnum)])
            counter -= 1
        return output 
            