class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        L = len(matrix)
        for i in range(L//2):
            for j in range(i, L - i - 1):
                i1, j1 = i, j 
                i2, j2 = j, L-i-1
                i3, j3 = L-i-1, L-j-1
                i4, j4 = L-j-1, i
                
                matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = matrix[i4][j4], matrix[i1][j1], matrix[i2][j2], matrix[i3][j3]
                