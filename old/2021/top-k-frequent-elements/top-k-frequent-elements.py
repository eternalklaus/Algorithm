class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        '''
        keys.sort(key = cnt.get, reverse=True)
        return keys[:k]
        '''
        nlargest = heapq.nlargest(k, cnt.keys(), key=cnt.get)
        return nlargest
        
        