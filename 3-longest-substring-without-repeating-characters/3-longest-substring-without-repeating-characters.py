class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if encounter char exising in current session, +li until remove the char. 
        from collections import Counter 
        li, ri, L = 0, 0, len(s)
        currentlen, output = 0, 0
        counter = Counter()
        
        # two pointer approach 
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
                
                
            