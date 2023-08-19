class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        g0, g0_invert = grid[0], [x==0 for x in grid[0]]
        for g in grid:
            if g == g0 or g == g0_invert:
                continue 
            else:
                return False 
        return True 