class Solution:
    def countSubstrings(self, s: str) -> int:
        output, L = 0, len(s)
        @cache # <- prevents duplicated calculation 
        def expand_palindrom(first, last):
            nonlocal output 
            # base cases
            if first < 0 or last >= L: 
                return 
            
            if s[first] == s[last]:
                output += 1                
                expand_palindrom(first-1, last+1)
                return True 
        
        for i in range(L):
            expand_palindrom(i, i) # odd length of palindrom
            expand_palindrom(i-1, i) # even length of palindrom 
            
        return output 