class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        counter, result = Counter(stones), 0
        
        for j in jewels:
            result += counter[j]
        return result