class Solution:
    def minSwaps(self, s: str) -> int:
        cnt, maxcnt = 0, 0
        for c in s:
            if c == ']': cnt += 1
            else: cnt -= 1
            maxcnt = max(maxcnt, cnt)
        return (maxcnt+1)//2