class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        
        output = n * m 
        
        def fillit(height, cnt):
            nonlocal output 
            if any(height) == False: # all of the spaces are filled, 
                output = min(cnt, output)
                return
            
            if cnt > output:
                return 
            
            # find the biggist square 
            maxh = max(height) # maxh * maxh 
            li = height.index(maxh)
            ri = li + 1
            while ri < m and height[ri] == maxh:
                ri += 1
            size = min(maxh, ri - li) 
            
            # "size" sized square => 1 ~ size 
            for sz in range(size, 0, -1): ###
                height_copy = height.copy() 
                for i in range(li, li+sz):
                    height_copy[i] -= sz
                fillit(height_copy, cnt+1)
        
        
        height = [n] * m # 2 2 2 -> 0,0,0 
        fillit(height, 0)
        return output 