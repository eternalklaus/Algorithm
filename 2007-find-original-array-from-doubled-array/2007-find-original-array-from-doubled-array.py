class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter, output = Counter(changed), []
        keys = sorted(list(counter.keys()))
        
        removed = 0
        
        for val in keys:
            if val == 0:
                if counter[val] % 2: return []
                counter[val] -= counter[val]//2
            else:
                counter[val * 2] -= counter[val]
                if counter[val * 2] < 0: return []
        return counter.elements()