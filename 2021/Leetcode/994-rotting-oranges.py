class Solution(object):
    def init_values(self, grid):
        self.grid = grid
        self.COL = len(grid)
        self.ROW = len(grid[0])
        self.queue = []
        self.days = 0

    def init_queue(self):
        for i in xrange(self.COL):
            for j in xrange(self.ROW):
                if self.grid[i][j] == 2:
                    self.queue.append([i, j])
        self.queue.append('END_OF_ROUND(contaminated succeed)') # marker

    def contamination(self, i, j):
        is_spreaded = False 
        if not (i<0 or j<0 or i>=self.COL or j>=self.ROW):
            if self.grid[i][j] == 1:
                self.grid[i][j] = 2         # contamination to adjusted oranges...
                self.queue.append([i,j])    # add newly contaminated orange into queue
                is_spreaded = True
        return is_spreaded

    def exist_fresh_orange(self):
        for i in xrange(self.COL):
            for j in xrange(self.ROW):
                if self.grid[i][j] == 1:
                    return True 
        return False 

    def orangesRotting(self, grid):
        self.init_values(grid)
        self.init_queue()

        while len(self.queue) != 0:
            poped           = self.queue.pop(0) # round start
            is_spreaded     = False
            while poped != 'END_OF_ROUND(contaminated succeed)': 
                [i, j] = poped 
                is_spreaded |= self.contamination(i, j+1)
                is_spreaded |= self.contamination(i, j-1)
                is_spreaded |= self.contamination(i+1, j)
                is_spreaded |= self.contamination(i-1, j)
                poped = self.queue.pop(0) # round continues...

            if is_spreaded: # append end marker ONLY WHEN new contamination exist
                self.days += 1
                self.queue.append('END_OF_ROUND(contaminated succeed)') 
        
        if self.exist_fresh_orange():
            return -1
        else:
            return self.days
            