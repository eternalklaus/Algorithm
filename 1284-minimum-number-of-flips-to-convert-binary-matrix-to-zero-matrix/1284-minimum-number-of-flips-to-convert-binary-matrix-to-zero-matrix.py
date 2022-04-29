class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        I, J = len(mat), len(mat[0])
        points = [(i, j) for i in range(I) for j in range(J)]
        
        def allzero():
            for i in range(I):
                for j in range(J):
                    if mat[i][j] == 1: return False 
            return True
        
        def flip(point):
            nonlocal mat
            i, j = point
            for ii, jj in [(i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0<=ii<I and 0<=jj<J:
                    mat[ii][jj] ^= 1
            
        self.output = float('inf')
        def flipit(current, idx):
            nonlocal mat
            # check whether current mat is filled with 0 
            if allzero(): # check mat
                self.output = min(self.output, len(current))
                return 
            
            for i in range(idx, len(points)):
                current.append(i)
                flip(points[i]) # flip mat 
                flipit(current, i+1)
                current.pop()
                flip(points[i]) # unflip
        
        flipit([], 0)
        return self.output if self.output != float('inf') else -1