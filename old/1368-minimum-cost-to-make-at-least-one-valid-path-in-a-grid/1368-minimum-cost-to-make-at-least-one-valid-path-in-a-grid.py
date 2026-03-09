class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        I, J, inf = len(grid),len(grid[0]),float('inf')
        delta = [(0,0), (0,1), (0,-1), (1,0), (-1,0)] # (0,0) is a placeholder..
        visited = {}
        trace = []

        def valid(i,j):
            return 0<=i<I and 0<=j<J and (i,j) not in visited

        def go_dfs(i,j,cost): ### i,j 캐시해보자 cost 전역변수로... 
            if not valid(i,j): return
            trace.append((i,j))
            visited[(i,j)] = cost
            di, dj = delta[grid[i][j]]
            go_dfs(i+di,j+dj,cost)
        
        go_dfs(0,0,0)
        traces = deque([trace])

        while traces:
            __trace = traces.popleft()
            if not __trace: continue

            for i,j in __trace:
                cost = visited[(i,j)] + 1
                for di, dj in delta: 
                    trace = []
                    go_dfs(i+di, j+dj, cost)
                    traces.append(trace)
        
        return visited[(I-1,J-1)]