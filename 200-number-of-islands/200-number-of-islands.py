class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # find connected 1s
        COL, ROW = len(grid), len(grid[0])
        
        def connect_stones(i, j):
            for newi, newj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not (0<=newi<COL and 0<=newj<ROW): continue
                if grid[newi][newj] == '1':
                    grid[newi][newj] = '0' # visited check!
                    connect_stones(newi, newj)


        output = 0
        for i in range(COL):
            for j in range(ROW):
                if grid[i][j] == '1':
                    connect_stones(i, j)
                    output += 1
        return output 