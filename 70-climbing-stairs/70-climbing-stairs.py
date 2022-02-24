class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def ways(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return ways(n-2) + ways(n-1)
        
        return ways(n)