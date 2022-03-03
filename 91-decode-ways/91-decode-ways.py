class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def decodeways(s):
            if len(s) == 0: 
                return 1
            if s[0] == '0': # invalid input 
                return 0
            # s is one-digit number
            if len(s) == 1: 
                return 1
            
            # s is more then two-digit number
            if int(s[:2]) <= 26:
                return decodeways(s[1:]) + decodeways(s[2:])
            else:
                return decodeways(s[1:])
        
        return decodeways(s)
            
                