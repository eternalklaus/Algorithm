class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # 1. build the graph
        # 2. dfs it 
        
        G = defaultdict(list)
        L = len(bombs)
        
        def connected(i, j):
            x1, y1, r1 = bombs[i]
            x2, y2, r2 = bombs[j]
            if (x1-x2)**2 + (y1-y2)**2 <= r1**2:
                return True
            return False
        
        for i in range(L):
            for j in range(L):
                if i == j: continue 
                if connected(i, j): G[i].append(j)
                if connected(j, i): G[j].append(i)
        
        
        def dfs(i, exploded):
            exploded.add(i)
            for nexti in G[i]:
                if nexti in exploded: continue 
                dfs(nexti, exploded)
                
            
        output = 0
        for i in range(L):
            exploded = set()
            dfs(i, exploded)
            output = max(output, len(exploded))
        return output 