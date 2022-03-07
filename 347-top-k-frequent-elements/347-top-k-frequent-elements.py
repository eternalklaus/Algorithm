class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = counter.most_common(k)
        return [num for (num, cnt) in freq]