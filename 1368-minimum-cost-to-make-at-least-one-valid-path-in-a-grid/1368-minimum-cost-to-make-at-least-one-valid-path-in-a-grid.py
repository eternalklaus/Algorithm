class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # min cut? 
        heap = [(0, (0,0))]
        I,J = len(grid), len(grid[0])
        dest = (I-1, J-1)
        visited = set([])
        delta = [(0,0), (0,1), (0,-1), (1,0), (-1,0)] # (0,0) is a placeholder..
        
        while True:
            cost, point = heapq.heappop(heap)
            if point == dest: return cost
                
            visited.add(point)
            i,j = point
            sign = grid[i][j]
            for s, (di, dj) in enumerate(delta):
                if 0<=i+di<I and 0<=j+dj<J:
                    if (i+di,j+dj) not in visited:
                        heapq.heappush(heap, (cost + (s != sign),(i+di,j+dj)))