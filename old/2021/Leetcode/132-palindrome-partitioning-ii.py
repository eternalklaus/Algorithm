class Solution:
    
    def minCut(self, s: str) -> int:
        n = len(s)
        def ispalin(lpivot, rpivot):
            rpivot -= 1
            while lpivot<rpivot:
                if s[lpivot] != s[rpivot]:
                    return False 
                lpivot += 1
                rpivot -= 1
            return True 

        from functools import cache
        @cache 
        def get_mincomponentcount(lpivot):
            if lpivot == n:
                return 0 
            elif ispalin(lpivot, n):
                return 1 
            else:
                mincount = 2000
                for rp in range(lpivot+1, n+1):
                    if ispalin(lpivot, rp):
                        count = 1 + get_mincomponentcount(rp)
                        # mincount = count if count<mincount else mincount
                        mincount = min(count, mincount)
                return mincount
    
        total_cnt = get_mincomponentcount(0)
        return total_cnt-1