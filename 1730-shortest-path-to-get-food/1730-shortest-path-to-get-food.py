class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        C, R = len(grid), len(grid[0])
        (i, j) = [[i, j] for i in range(C) for j in range(R) if grid[i][j] == '*'][0] ###<-
        outputs = []
        
        queue = [(0, i, j)]
        while queue:
            steps, i, j = heappop(queue)
            if not 0<=i<C or not 0<=j<R or grid[i][j] == 'X': 
                continue 
                
            if grid[i][j] == '#':
                return steps
                
            grid[i][j] = 'X' # mark visited location(this is cheapest way to reach here)
            heappush(queue, (steps+1, i+1, j))
            heappush(queue, (steps+1, i-1, j))
            heappush(queue, (steps+1, i, j+1))
            heappush(queue, (steps+1, i, j-1))
        
        return -1