class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # constant space

        COL, ROW = len(matrix), len(matrix[0])
        colbit = 0
        rowbit = 0

        for i in range(COL):
            for j in range(ROW):
                if matrix[i][j] is not 0: 
                    continue 
                colbit |= 1 << i
                rowbit |= 1 << j 
        
        for i in range(COL):
            for j in range(ROW):
                if (1<<i) & colbit or (1<<j) & rowbit: 
                    matrix[i][j] = 0
                    


