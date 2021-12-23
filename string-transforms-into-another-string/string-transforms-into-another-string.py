class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        import string
        
        # just see pattern. 
        N = len(str1)
        cache = {}
        
        # condition 1 - all char matched one by one
        for i in range(N):
            c1 = str1[i]
            c2 = str2[i]
            if c1 not in cache: 
                cache[c1] = c2
            
            if cache[c1] != c2:
                return False 
        
        
        # condition 2 - no cycle 
        if len(set(cache.values())) < 26: # no need to check because enough temporary char exist
            return True
        if str1 == str2: # two strings are identical
            return True
        for c in cache:
            stack = []
            
            while c in cache and 'a' <= c <= 'z':
                if c in stack: 
                    return False 
                stack.append(c)
                c = cache[c]
            
            LASTC = c.upper()
            
            while stack:
                c = stack.pop() 
                cache[c] = LASTC
        return True
                