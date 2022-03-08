class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        L = len(nums)
        bucket = [[] for i in range(L+1)]
        counter = Counter(nums)

        for num in counter:
            num, cnt = num, counter[num]
            bucket[cnt].append(num)
        
        output = []
        for i in range(L, -1, -1):
            output += bucket[i]
            if len(output)  >= L: break 
        
        return output[:k]