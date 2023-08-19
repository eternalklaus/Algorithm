class Solution:
    def maxPower(self, s: str) -> int:
        # can s be the empty string? 
        if not s: 
            return 0
        
        bch = '-'
        cnt, maxcnt = 1, 1
        
        for ch in s:
            if ch == bch:
                cnt += 1
            else:
                cnt = 1
            bch = ch
            maxcnt = max(maxcnt, cnt)
        
        return maxcnt
            