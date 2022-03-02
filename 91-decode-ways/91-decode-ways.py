class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def getnum(s):
            # base cases
            if len(s) == 0: 
                return 1
            if s[0] == '0': # invalid string, stop recursive calling. 
                return 0
            
            if len(s) >= 2 and int(s[:2]) <= 26:
                return getnum(s[1:]) + getnum(s[2:])
            else: # only 1-digit number is strippable
                return getnum(s[1:])
        
        return getnum(s)
                
                
            