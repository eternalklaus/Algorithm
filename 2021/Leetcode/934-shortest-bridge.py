class Solution:
    def findcontinent(self):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if self.A[i][j] == 1: 
                    return i, j
    
    def expand(self, i, j):
        if i<0 or j<0 or i>=len(self.A) or j>len(self.A[0]):
            return 
        
        if self.A[i][j] == 1: 
            self.tmpisland.add([i, j])
            self.expand(i+1, j)
            self.expand(i-1, j)
            self.expand(i, j+1)
            self.expand(i, j-1)

    def neighbor(self, i, j):
        for c, r in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if 0 <= c < len(self.A) and 0 <= r < len(self.A[0]):
                yield c, r 

    def dist(self, island_1, island_2):
        

    def shortestBridge(self, A: List[List[int]]) -> int:
        self.A = A
        self.island_1 = set()
        self.island_2 = set()

        i, j = self.findcontinent()
        self.tmpisland = set()
        self.expand(i, j)
        self.island_1 = self.tmpisland.copy() 

        i, j = self.findcontinent()
        self.tmpisland = set()
        self.expand(i, j)
        self.island_2 = self.tmpisland.copy() 

        return dist(self.island_1, self.island_2)