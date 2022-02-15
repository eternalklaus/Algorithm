class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        I, J = len(points), len(points[0])
        
        temp = [0] * J
        
        for i in range(I):
            # accumulate upper line
            
            
            for j in range(J):
                points[i][j] = points[i][j] + temp[j]
            
            # clear temp 
            temp = [0] * J
            
            # get lmax 
            temp[0] = points[i][0]
            for j in range(1, J):
                temp[j] = max(temp[j-1] - 1, points[i][j])
                
            # get rmax 
            temp[-1] = max(points[i][-1], temp[-1])
            for j in range(J-2, -1, -1):
                temp[j] = max(temp[j+1] - 1, temp[j]) # compare precalculated(lr) one
            
        return max(points[-1])
    
    # [5,2,1,2]
    # [2,1,5,2]
    # [5,5,5,0]