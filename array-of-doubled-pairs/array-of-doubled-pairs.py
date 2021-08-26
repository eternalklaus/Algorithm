class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import Counter
        cnt, total = Counter(arr), len(arr)
        for n in sorted(arr, key=abs):
            if cnt[n] == 0: continue
            if cnt[2*n] < cnt[n]: return False
            
            if total == 0: break
            total -= 2*cnt[n]
            cnt[2*n] -= cnt[n]
            cnt[n] = 0
        
        return True
            
                
            