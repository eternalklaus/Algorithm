class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        emptyheight = [n] * m
        self.output = n*m
        
        def fillit(eh, cnt): # empty height 
            if cnt > self.output: 
                return
            if any(eh) == False: ###!!!
                self.output = min(self.output, cnt)
                return 
            
            # get maximum height that can e filled 
            maxh = max(eh)
            li = eh.index(maxh)
            ri = li + 1
            while ri < m and eh[ri] == maxh:
                ri += 1
            
            size = min(maxh, ri-li)#!!!
            
            # fill sized box
            for sz in range(size, 0, -1):
                eh_copy = deepcopy(eh)
                for i in range(li, li+sz):
                    eh_copy[i] -= sz
                fillit(eh_copy, cnt+1)
        
        fillit(emptyheight, 0)
        return self.output 
            
                