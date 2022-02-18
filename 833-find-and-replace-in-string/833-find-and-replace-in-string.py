class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        # if replacement is overlapped, stop operation
        L, output, prevend = len(indices), '', 0
        #index = sorted([i for i in range(L)], key = lambda x: indices[x])
        
        #for i in index:
        for idx, src, tgt in sorted(zip(indices, sources, targets)):
            # idx, src, tgt = indices[i], sources[i], targets[i]
            
            # Condition 2. If it does not occur, do nothing.
            if s[idx:idx+len(src)] != src:  
                continue 
            
            if prevend > idx:
                return False 

            output += s[prevend:idx]
            output += tgt 
            prevend = idx + len(src)
        
        output += s[prevend:]
        return output 