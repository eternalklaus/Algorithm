class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Time: O(n) Space: O(1) 
        N = len(arrays)
        max1, maxi1 = max( (arrays[idx][-1], idx) for idx in range(N) )
        min1, mini1 = min( (arrays[idx][0], idx) for idx in range(N) )
        
        if maxi1 != mini1:
            return max1-min1
        
        arrays.pop(maxi1) # remove the idx-st value from arrays
        N = N-1
        max2, maxi2 = max( (arrays[idx][-1], idx) for idx in range(N) )
        min2, mini2 = min( (arrays[idx][0], idx) for idx in range(N) )
        
        return max(max1-min2, max2-min1)
        # Time: O(nlogn) Space: O(n)
        '''
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
        '''
        
        
        
        
        
        
        