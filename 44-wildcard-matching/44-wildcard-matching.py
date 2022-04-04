class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S, P = len(s), len(p)
        
        @cache 
        def check(si, pi):
            # print (s[si:], p[pi:])
            if si >= S and pi >= P:
                return True 
            if pi >= P: # pattern is all consumed ... 
                return False 
            if si >= S: # string is all consumed ... 
                return set(p[pi:]) == {'*'} # give one more chance...
            
            if p[pi] == '?' or p[pi] == s[si]:
                return check(si+1, pi+1)
            
            if p[pi] == '*':
                for sii in range(si, S+1):
                    if check(sii, pi+1): return True 
            return False 

        return check(0,0)