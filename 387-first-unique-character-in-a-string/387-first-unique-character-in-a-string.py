class Solution:
    def firstUniqChar(self, s: str) -> int:
        indice, INF = {}, float('inf')
        
        # single enumeration is enough
        for i, c in enumerate(s):
            if c not in indice: # fresh char! first appeared! 
                indice[c] = i
            elif c in indice: # go stale... 
                indice[c] = INF 
        
        output = min(list(indice.values()))
        return output if output != INF else -1