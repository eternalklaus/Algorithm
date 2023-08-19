class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort(reverse=True)
        total = len(tasks)
        
        @cache
        def dfs(bitmask, remaintime):
            minbinsize = bitmask.count('1')
            if minbinsize == 0: return 0
            
            for idx, bit in enumerate(bitmask):
                if bit == '0': continue
                newbitmask = bitmask[:idx] + '0' + bitmask[idx+1:]
                
                if remaintime - tasks[idx] >= 0: # absorb into exising bin
                    minbinsize = min(minbinsize, dfs(newbitmask, remaintime - tasks[idx]))
                else: # create new bin and start new bincounting
                    minbinsize = min(minbinsize, dfs(newbitmask, sessionTime - tasks[idx]) + 1)
            
            return minbinsize
    
        bitmask = bin(2**total - 1)[2:]
        return dfs(bitmask, 0)
            
            
            