class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ?: single char
        # *: sequance chars 
        # ab*def abcdef abddd def ddd def
        # if some chars appears after *, 
        S, P = len(s), len(p)
        
        @cache 
        def ismatch(si, pi): ### what if s is empty string?
            # print (s[si:], p[pi:])
            if si >= S and pi >= P:
                return True
            if pi >= P: # pattern is exhausted even though string still remained
                return False 
            if si >= S: # '', "***"
                if p[pi] == '*':
                    return ismatch(si, pi+1) 
                else: 
                    return False 

            if s[si] == p[pi] or p[pi] == '?':
                return ismatch(si+1, pi+1)
            if p[pi] == '*':
                for ssi in range(si, S+1): # from si to S ... 
                    if ismatch(ssi, pi+1): return True 
                
            return False 
            
        return ismatch(0, 0)
