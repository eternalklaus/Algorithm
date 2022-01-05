class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        grid = [[0]*n for i in range(n)] # WHF

        def setgrid(life):
            nonlocal grid
            while life > 0:
                # initialize grid
                newgrid = [[0]*n for i in range(n)]
                # check all the locations of the grid 
                for i in range(n): 
                    for j in range(n):
                        possibility = grid[i][j]/8 
                        for dr, dc in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)): # <= cool
                            newi = i + dr 
                            newj = j + dc 
                            if 0 <= newi < n and 0 <= newj < n:
                                newgrid[newi][newj] += possibility 

                grid = newgrid 
                life -= 1
            
        
        grid[row][column] = 1
        setgrid(k)
        return sum(map(sum, grid)) # <= cool
    