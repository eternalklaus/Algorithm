class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        from collections import deque
        I, J = len(grid), len(grid[0])
        
        # Step1. get the mantatten dist of each cells 
        q = deque()
        sgrid = [[-1 for j in range(J)] for i in range(I)] # sgrid = safeness value of grid
        for i in range(I):
            for j in range(J):
                if grid[i][j] == 1: 
                    q.append((i,j))
                    sgrid[i][j] = 0
        while q:
            (i, j) = q.popleft()
            for (ii, jj) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0<=ii<I and 0<=jj<J): continue
                if not (sgrid[ii][jj] == -1): continue # already visited
                q.append((ii, jj))
                sgrid[ii][jj] = sgrid[i][j] + 1
        
        # Step2. Search cells with prioritzing higher safeness distance first
        maxheap, visited = [], set()
        heapq.heappush( maxheap, (-sgrid[0][0], 0,0) ) # (safeness, x, y)
        while maxheap:
            (safeness, i, j) = heapq.heappop(maxheap)
            safeness = -safeness # correction 

            for (ii, jj) in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0<=ii<I and 0<=jj<J): continue
                if (ii, jj) in visited: continue # already visited
                visited.add((ii, jj))

                # 현재까지 경로의 세이프니스 vs 현재셀의 세이프니스... 이중 나쁜것을 취한다 
                currsafeness = min(safeness, sgrid[ii][jj])
                sgrid[ii][jj] = currsafeness # 현재셀의 세이프니스를 업데이트
                heapq.heappush( maxheap, (-currsafeness, ii, jj) )
        
        if (I-1, J-1) in visited:
            return sgrid[I-1][J-1]
        return 0