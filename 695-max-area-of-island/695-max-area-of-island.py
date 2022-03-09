class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        I, J = len(grid), len(grid[0])
        def getarea(i, j):
            if not (0<=i<I and 0<=j<J):
                return 0
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0 # prevents duplicated counting
            output = 1
            for ii, jj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                output += getarea(ii, jj)
            return output 
            
        output = 0
        for i in range(I):
            for j in range(J):
                if grid[i][j] == 1:
                    output = max(output, getarea(i, j))
        return output
            