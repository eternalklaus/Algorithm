class Solution(object): 
    def search_maxtime(self):
        maxval = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.time[i][j] > maxval:
                    maxval = self.time[i][j]
        return maxval

    def count_rotdate(self, i, j, elapsedtime):
        if i >= self.height or j >= self.width or i < 0 or j < 0:
            return
        print i, j
        if self.grid[i][j] == 1: # fresh orange!
            
            

    def orangesRotting(self, grid):
        self.grid = grid 
        self.height = len(grid)
        self.width = len(grid[0])
        self.time = [[0 for i in range(self.width)] for j in range(self.height)]
        self.elapsedtime = 0

        for i in xrange(self.height):
            for j in xrange(self.width):
                if self.grid[i][j] == 2: # rotten
                    self.count_rotdate(i, j+1, 1) # east
                    self.count_rotdate(i+1, j, 1) # south
                    self.count_rotdate(i, j-1, 1) # west
                    self.count_rotdate(i-1, j, 1) # north
        
        return self.search_maxtime
        