class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for coloum in matrix:
            if target in coloum: return True
        return False