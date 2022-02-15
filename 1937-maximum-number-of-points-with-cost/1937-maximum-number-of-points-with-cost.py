class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROW, COL = len(points), len(points[0])
        points.insert(0, [0 for j in range(COL)])
        rlgrid  = [[0 for j in range(COL)] for i in range(ROW+1)]
        lrgrid  = [[0 for j in range(COL)] for i in range(ROW+1)]
        
        for i in range(1, ROW+1):
            for j in range(COL):
                points[i][j] = points[i][j] + max(lrgrid[i-1][j], rlgrid[i-1][j])
            
            lrgrid[i][0] = points[i][0]
            for j in range(1, COL):
                lrgrid[i][j] = max(lrgrid[i][j-1] - 1, points[i][j])

            rlgrid[i][COL-1] = points[i][COL-1]
            for j in range(COL-2, -1, -1):
                rlgrid[i][j] = max(rlgrid[i][j+1] - 1, points[i][j])
            
        return max(points[ROW])