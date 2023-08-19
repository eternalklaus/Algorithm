class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        I, J = len(matrix), len(matrix[0])
        
        @cache
        def getnum_descending(i, j):
            output = 1 
            for ii, jj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if not 0<=ii<I or not 0<=jj<J:
                    continue 
                else: 
                    if matrix[ii][jj] < matrix[i][j]:
                        output = max(output, getnum_descending(ii, jj) + 1)
            return output 
        
        output = 1 
        for i in range(I):
            for j in range(J):
                output = max(output, getnum_descending(i, j))
        return output 
            