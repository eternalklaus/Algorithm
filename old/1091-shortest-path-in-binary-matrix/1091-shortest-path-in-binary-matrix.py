class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        L = len(grid)
        visited, queue = {}, [] # if L == 1: return 1 
        
        if grid[0][0] == 0:
            visited = {(0,0):1} # form of (loc1, loc2):3 
            queue  = [(0,0)]
        
        while queue:
            (i, j) = queue.pop(0)
            
            for ii in [i-1, i, i+1]:
                for jj in [j-1, j, j+1]:
                    if not (0<=ii<L and 0<=jj<L): continue 
                    if grid[ii][jj] == 1: continue 
                    if (ii, jj) in visited: continue 

                    visited[(ii, jj)] = visited[(i, j)] + 1
                    queue.append((ii, jj)) # new world 
        
        if output := visited.get((L-1, L-1)):
            return output 
        return -1
