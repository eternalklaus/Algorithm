class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        I, J = len(mat), len(mat[0])
        points = [(i, j) for i in range(I) for j in range(J)]
        output = float('inf')

        def allzero(mat):
            for i in range(I):
                for j in range(J):
                    if mat[i][j] == 1: return False 
            return True 

        def subset(index, current, mat):
            nonlocal output 
            # print (mat, index, current)
            
            # Case 0. base cases 
            if allzero(mat):
                # print (mat)
                output = min(output, len(current)) # update output 
                return 
            if index >= len(points): 
                return 
            
            for idx in range(index, len(points)):
                newcurrent, newmat = deepcopy(current), deepcopy(mat) ###!!!
                newcurrent.append(idx)
                (i, j) = points[idx]

                # flip
                for ii, jj in [(i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0<=ii<I and 0<=jj<J:
                        newmat[ii][jj] ^= 1 
                subset(idx+1, newcurrent, newmat)
        
        subset(0, [], mat)
        return output if output != float('inf') else -1
