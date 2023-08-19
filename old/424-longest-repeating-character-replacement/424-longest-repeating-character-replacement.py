class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        AAABBBBBC -> 9 - 5 = 4 B, 5
        '''
        # start, end s[start:end]
        first, last = 0, 0 # s[first:last+1]
        L = len(s)
        counter = Counter()
        output = 0
        
        for last in range(L):
            c = s[last]
            counter[c] += 1
            windowsize = last - first + 1
            many = counter.most_common(1)[0][1]
            tochange = windowsize - many
            
            if tochange <= k: 
                output = max(output, windowsize)
                continue 
            # decrease window size
            # first -> . . . . last 
            else: 
                while tochange > k:
                    c = s[first]
                    counter[c] -= 1
                    first += 1
                    windowsize = last - first + 1
                    many = counter.most_common(1)[0][1]
                    tochange = windowsize - many
        
        return output 
        