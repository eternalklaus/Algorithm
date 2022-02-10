class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        COL, ROW = len(heights), len(heights[0])

        def ingrid(i, j):
            if 0<=i<COL and 0<=j<ROW: return True 
            return False 

        Pacific, Atlantic = set(), set()
        pq, aq = [], [] # queue for visit

        # 0. Initialize each beaches
        for j in range(ROW):
            pq.append((0, j))
            aq.append((COL-1, j))
        for i in range(COL):
            pq.append((i, 0))
            aq.append((i, ROW-1))
        
        # 1. Pacific
        while pq:
            (pi, pj) = pq.pop()
            Pacific.add((pi, pj))

            for i, j in [(pi+1, pj), (pi-1, pj), (pi, pj+1), (pi, pj-1)]:
                if not ingrid(i, j): continue 
                if (i, j) in Pacific: continue 
                if heights[pi][pj] <= heights[i][j]: # lets climb up! 
                    pq.append((i, j))
        
        # 2. Atlantic
        while aq:
            (ai, aj) = aq.pop()
            Atlantic.add((ai, aj))

            for i, j in [(ai+1, aj), (ai-1, aj), (ai, aj+1), (ai, aj-1)]:
                if not ingrid(i, j): continue 
                if (i, j) in Atlantic: continue 
                if heights[ai][aj] <= heights[i][j]: # lets climb up! 
                    aq.append((i, j))
        
        # Common set of Pacific and Atlantic
        # return [x for x in Pacific if x in Atlantic]
        return Pacific & Atlantic