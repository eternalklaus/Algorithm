class Solution:
    # Time Complexity: O(n!), n == length of s
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict) # remove duplicated word
        output, L = False, len(s) 
        
        # remove prefix word by word
        @cache
        def remove(idx) -> None: 
            nonlocal output
            # base cases
            if idx == L:
                output = True 
                return 
            
            for i in range(idx+1, L+1): ### index caution
                prefix = s[idx:i]
                if prefix in wordDict:
                    remove(i)
            return 
                
        remove(0)
        return output 