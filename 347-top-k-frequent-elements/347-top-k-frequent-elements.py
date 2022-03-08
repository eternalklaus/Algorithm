class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        L = len(nums)
        bucket = [[] for i in range(L+1)] ### size = L+1!
        counter = Counter(nums)

        for num, cnt in counter.items():
            bucket[cnt].append(num)
        
        output = [n for b in bucket for n in b]
        return output[-k:]