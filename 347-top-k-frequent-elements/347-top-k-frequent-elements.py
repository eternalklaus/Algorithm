class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 
        counter = Counter(nums)
        output = counter.most_common(k)
        return [c[0] for c in output]