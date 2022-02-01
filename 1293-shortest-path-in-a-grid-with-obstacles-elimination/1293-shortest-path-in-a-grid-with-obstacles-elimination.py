class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # track all possible route
        C, R = len(grid), len(grid[0])
        INF = float('inf')
        
        if k >= C+R-2:
            return C+R-2
        
        # Route can be up/left, not only down/right
        @cache
        def gogo(i, j, k, step): # i, j = current location / step = steps until reaching current location
            if not 0<=i<C: return INF
            if not 0<=j<R: return INF
            # same place
            if grid[i][j] == -1: return INF
            # it's obstacle. can I overcome it? 
            if grid[i][j] == 1:
                if k == 0: return INF# failed to overcome..
                else: k -= 1
                    
            # reached to destination
            if i == C-1 and j == R-1: 
                return step 
            
            _ = grid[i][j]
            grid[i][j] = -1
            route1 = gogo(i+1, j, k, step+1)
            route2 = gogo(i-1, j, k, step+1)
            route3 = gogo(i, j+1, k, step+1)
            route4 = gogo(i, j-1, k, step+1)
            grid[i][j] = _
            return min([route1, route2, route3, route4])
            
        output = gogo(0, 0, k, 0)
        
        if output == float('inf'): 
            return -1
        return output 