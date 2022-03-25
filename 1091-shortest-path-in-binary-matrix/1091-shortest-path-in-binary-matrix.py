class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        L = len(grid)
        if grid[0][0] == 1: return -1 
        if L == 1: return 1 
        
        visited = {(0,0):1} # form of (loc1, loc2):3 
        queue  = [(0,0)]
        
        # 항상 while 에 들어오지않는 엣지케이스를 생각하자. 
        while queue:
            (i, j) = queue.pop(0)
            
            for ii in [i-1, i, i+1]:
                for jj in [j-1, j, j+1]:
                    if not (0<=ii<L and 0<=jj<L): continue 
                    if grid[ii][jj] == 1: continue 
                    if (ii, jj) in visited: continue 
                    if (ii, jj) == (L-1, L-1): return visited[(i, j)] + 1
                    
                    visited[(ii, jj)] = visited[(i, j)] + 1
                    queue.append((ii, jj)) # new world 
        
        return -1
