class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        
        # remove word by word from the left part of s
        output, L = False, len(s)
        
        @cache
        def remove(idx): # returns nothing. instead, it changes output, the global variable. 
            nonlocal output
            # base cases
            if output == True or idx == L:
                output = True 
                return 
            
            for i in range(idx+1, L+1): ###
                prefix = s[idx:i]
                if prefix in wordDict:
                    remove(i)
            return 
                
        remove(0)
        return output 