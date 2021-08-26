class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import Counter
        counter = Counter(arr)
        
        for n in sorted(arr, key=abs):
            if n == 0:
                if counter[n] >= 2:
                    counter[n] -= 2
            elif counter[n] > 0 and counter[2*n] > 0:
                counter[n] -= 1
                counter[2*n] -= 1
        
        for v in counter.values():
            if v is not 0: return False 
        return True
            
                
                
                