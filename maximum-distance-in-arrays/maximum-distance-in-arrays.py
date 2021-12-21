class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        import heapq
        maxlist = []
        minlist = []
        for i, array in enumerate(arrays):
            heapq.heappush(maxlist, (-max(array), i))
            heapq.heappush(minlist, (min(array), i)) # attach since it's *MIN* heap 
        
        # try it al most twice
        (maxval, maxidx) = heapq.heappop(maxlist)
        (minval, minidx) = heapq.heappop(minlist)
        if maxidx != minidx:
            return -maxval-minval
    
        (maxval2, maxidx2) = heapq.heappop(maxlist)
        (minval2, minidx2) = heapq.heappop(minlist)
        return max(-maxval-minval2, -maxval2-minval)
        
        
        
        
        
        
        
        