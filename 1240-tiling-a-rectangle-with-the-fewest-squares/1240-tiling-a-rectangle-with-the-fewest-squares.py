class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        
        def getminbox(heights):
            maxheight = max(heights)
            li = heights.index(maxheight)
            ri = li + 1 
            while ri < m and heights[ri] == maxheight:
                ri += 1 
            return maxheight, (ri-li), li

        # rule 1. 무조건 ceil부터 채운다. 따라서 heights는 아래에서부터 채울수있는 높이다
       
        self.output = n * m

        def fillit(heights, cnt): ### heights = empty spaces height  
            if any(heights) == False: # all is 0
                self.output = min(self.output, cnt)
                return 
            if cnt > self.output:
                return 
            height, width, li = getminbox(heights)
            boxsize = min(height, width)
            # fill every sized boxes
            # for size in range(1, boxsize+1): ###!!! 아... 가장 큰것부터 채워주는 센스... 
            for size in range(boxsize, 0, -1):
                newheights = heights.copy()
                for i in range(li, li + size):
                    newheights[i] -= size 
                fillit(newheights, cnt+1)
        
        fillit([n] * m, 0)
        return self.output 