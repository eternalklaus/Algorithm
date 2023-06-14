class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        output, L = 0, len(s)
        
        li = 0
        while li < L:
            ri = li + 1
            while ri <= L and int(s[li:ri+1]) <= k:
                ri += 1
            
            if int(s[li:ri]) > k: 
                return -1    
            li = ri
            output += 1
        return output