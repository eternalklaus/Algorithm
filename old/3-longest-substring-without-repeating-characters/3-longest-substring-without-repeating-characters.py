class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first, last, L = 0, 0, len(s)
        counter, output = Counter(), 0
        # increase window
        for last in range(L):
            counter[s[last]] += 1
            # newbie is one and only. so update the length!
            if counter[s[last]] == 1: 
                output = max(last-first+1, output)
                continue 
            # else, decrease the window
            while counter[s[last]] > 1:
                counter[s[first]] -= 1
                first += 1
        return output 
        '''
        from collections import Counter 
        li, ri, L = 0, 0, len(s)
        currentlen, output = 0, 0
        counter = Counter()
        
        # Two pointer approach 
        # Time complexity: O(n) Space Complexity: O(26)=O(1)
        while ri < L:
            c = s[ri]
            if counter[c] == 0: # increase ri (expand it)
                counter[c] += 1
                ri += 1 
                currentlen += 1
                output = max(output, currentlen)
                
            else: # decrease li (shirink the substring)
                while True :
                    counter[s[li]] -= 1
                    li += 1
                    currentlen -= 1
                    if s[li-1] == c: 
                        break 
        return output      
        '''
        
            