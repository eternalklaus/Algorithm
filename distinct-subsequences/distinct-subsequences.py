class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # subset sized n
        
        @cache
        def subset(sidx, tidx):
            count = 0
            
            if tidx == len(t): 
                return 1
            
            if sidx >= len(s): 
                return 0
            
            '''
            for i in range(sidx, len(s)):
                if s[i] == t[tidx]:
                    count += subset(i+1, tidx+1)
            return count
            '''
            count = subset(sidx+1, tidx)
            if s[sidx] == t[tidx]:
                count += subset(sidx+1, tidx+1)
            return count
        
        count = subset(0, 0)
        return count