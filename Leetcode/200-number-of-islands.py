class Solution(object):
    def countcontinent(self, i, j):
        ### Boundary check
        if i >= self.height or j >= self.width: return 
        if i < 0 or j < 0: return

        if self.grid[i][j] == "1":
            self.grid[i][j] = "checked"

            ### check east expand
            self.countcontinent(i, j+1)
        
            ### check south expand
            self.countcontinent(i+1, j)

            ### check west expand
            self.countcontinent(i, j-1)
            
            ### check north expand
            self.countcontinent(i-1, j)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid 
        self.height = len(grid)
        self.width = len(grid[0])
        self.count = 0 

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == "1":
                    self.countcontinent(i, j)
                    self.count += 1
        
        return self.count