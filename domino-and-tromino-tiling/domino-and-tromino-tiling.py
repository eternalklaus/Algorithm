class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def full(k):
            if k == 1: return 1
            if k == 2: return 2
            return (full(k-1) + full(k-2) + 2 * part(k-1)) % MOD
        
        @cache
        def part(k):
            if k == 2: return 1
            return (full(k-2) + part(k-1)) % MOD
        
        return full(n)
            