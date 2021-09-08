class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        
        keys = list(cnt.keys())
        keys.sort(key = lambda x:cnt[x], reverse = True)
        
        return keys[:k]
        