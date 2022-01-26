class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter 
        # first, last, L, output = 0, k-1, len(s), 0
        first, last, L, output = 0, 1, len(s), 0
        counter = Counter(s[first:last+1])
        virus = k
        
        while True:
            window = last - first + 1
            [ch_zombie, cnt_zombie] = counter.most_common(1)[0]
            cnt_human = window - cnt_zombie
            
            if cnt_human > virus: # too many humans.. decrease window size..
                counter[s[first]] -= 1
                first += 1
            
            elif cnt_human <= virus:
                output = max(output, window)
                last += 1
                if last == L: break 
                counter[s[last]] += 1
                
        return output 