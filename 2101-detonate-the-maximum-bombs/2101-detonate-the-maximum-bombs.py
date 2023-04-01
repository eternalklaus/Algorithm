class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        connected = defaultdict(list)
        L = len(bombs)
        
        def isConnected(i, j):
            x1, y1, r1 = bombs[i]
            x2, y2, r2 = bombs[j]
            if pow(x1-x2, 2) + pow(y1-y2, 2) <= pow(r1, 2):
                return True 
            return False 
        
        # create connected graph
        for i in range(L):
            for j in range(L):
                if i == j: continue
                if isConnected(i, j):
                    connected[i].append(j)
                
        # for i, l in connected.items():
        #     print (i, l)
        
        # TODO: team can be represented as bit -> can be cached!
        def dfs(i, team): # accumulate visited
            team.add(i)
            for nexti in connected[i]:
                if nexti in team: continue 
                dfs(nexti, team)
        
        output = 0
        for i in range(L):
            team = set()
            dfs(i, team)
            output = max(len(team), output)
        return output 
                    