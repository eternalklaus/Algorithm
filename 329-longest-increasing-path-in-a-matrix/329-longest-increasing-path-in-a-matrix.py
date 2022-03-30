class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # recursive!
        # dynamic programming 
        I, J = len(matrix), len(matrix[0])
        
        @cache 
        def recursive(i, j): # returns maximum path including matrix[i][j] as maximum dest
            output = 1
            for ii, jj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if not 0<=ii<I or not 0<=jj<J: continue 
                if matrix[ii][jj] < matrix[i][j]: 
                    output = max(output, recursive(ii, jj) + 1)
            return output 
        
        output = 0
        for i in range(I):
            for j in range(J):
                output = max(output, recursive(i, j))
        return output 
                    