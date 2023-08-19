class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        I, J = len(grid), len(grid[0])
        i, j = [(i, j) for i in range(I) for j in range(J) if grid[i][j] == '*'][0]
        queue = [(0, i, j)]
        
        while queue:
            weight, i, j = heapq.heappop(queue)
            # print (weight, i, j)
            for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not (0<=ii<I and 0<=jj<J):
                    continue 
                if grid[ii][jj] == 'X':
                    continue 
                if grid[ii][jj] == '#': 
                    return weight + 1
                if grid[ii][jj] == 'O': 
                    grid[ii][jj] = 'X' # visited mark
                    heapq.heappush(queue, (weight + 1, ii, jj))
        return -1