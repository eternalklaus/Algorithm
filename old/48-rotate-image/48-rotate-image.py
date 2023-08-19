class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        L = len(matrix)
        # rotate up-down
        for i in range(L//2):
            for j in range(L):
                matrix[i][j], matrix[L-1-i][j] = matrix[L-1-i][j] , matrix[i][j]
                
        # rotate down-right (change i, j)
        for i in range(L):
            for j in range(i, L):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
        