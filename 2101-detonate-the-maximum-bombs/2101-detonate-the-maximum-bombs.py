class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        from functools import lru_cache
        L = len(bombs)
        
        # directed graph
        G = defaultdict(list)
        
        
        def connected(i, j):
            x1,y1,r1 = bombs[i]
            x2,y2,r2 = bombs[j]
            if (x1-x2)**2 + (y1-y2)**2 <= r1**2: ###
                return True
            return False 
            
            
        L = len(bombs)
        for i in range(L):
            for j in range(L):
                if i == j: continue 
                if connected(i, j): 
                    G[i].append(j)
                if connected(j, i):
                    G[j].append(i)
        
        def visit(i, visited):
            if i in visited: return 0
            
            visited.add(i)
            for j in G[i]:
                visit(j, visited)
                
            
        
        output = 0
        for i in range(L): # the visiting order matters... 
            visited = set()
            visit(i, visited)
            output = max(output, len(visited))
        return output 
            
                
                