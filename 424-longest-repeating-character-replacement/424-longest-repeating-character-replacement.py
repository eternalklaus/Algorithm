class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        first, last, L = 0, 0, len(s)
        counter = Counter()
        output = 0
        
        # increase window size
        for last in range(L):
            counter[s[last]]+=1
            most_common = counter.most_common(1)[0][1] # most num of superial char 
            total_length = last - first + 1
            tochange = total_length - most_common 
            
            if tochange <= k: # valid
                output = max(output, total_length)
            
            # decrease window size
            else: # invalid
                while tochange > k: # while invalid, decrease window size
                    counter[s[first]]-=1
                    first += 1
                    most_common = counter.most_common(1)[0][1]
                    total_length = last-first+1
                    tochange = total_length - most_common
        return output 