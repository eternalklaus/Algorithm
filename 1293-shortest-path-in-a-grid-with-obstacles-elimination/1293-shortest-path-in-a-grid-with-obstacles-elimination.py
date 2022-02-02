class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Tip: manhatan distance
        life = k
        C, R, INF = len(grid), len(grid[0]), float('inf')
        
        @cache
        def gogo(i, j, life, steps):
            # base case
            if not 0<=i<C or not 0<=j<R: return INF # invalid location
            if i == C-1 and j == R-1: return steps # Reached destination
            if grid[i][j] == -1: return INF # Encountered the place that I already visited
            if (C-i-1) + (R-j-1) < life: return steps + (C-i-1) + (R-j-1)# Manhattan distance case
                
            # 1. Encountered block 
            if grid[i][j] == 1:
                if life < 1: return INF
                else: life -= 1
            
            # 2. Move on to 4-direction
            gridij = grid[i][j]
            grid[i][j] = -1
            step1 = gogo(i+1, j, life, steps+1)
            step2 = gogo(i-1, j, life, steps+1)
            step3 = gogo(i, j+1, life, steps+1)
            step4 = gogo(i, j-1, life, steps+1)
            grid[i][j] = gridij
            return min([step1, step2, step3, step4])
        
        output = gogo(0,0,k,0)
        if output >= INF:
            return -1
        return output 
            
            