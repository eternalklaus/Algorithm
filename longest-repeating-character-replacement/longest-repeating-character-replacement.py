class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        # sliding window 
        starti, output, life, counter = 0, 0, k, Counter()
        for endi in range(1, len(s)+1):
            counter[s[endi-1]] += 1 # not including endi
            (ch, chcnt) = counter.most_common(1)[0]
            
            if endi - starti - chcnt <= life:
                
                output = max(output, endi - starti)
            else: # not enough life
                counter[s[starti]] -= 1 
                starti += 1 # move slide forward
                
        
        return output
            