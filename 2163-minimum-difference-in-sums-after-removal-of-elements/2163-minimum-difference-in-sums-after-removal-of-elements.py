class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        
        # remove large num from left part, remove small num from right part
        # sweeping from left to right, and add up to n, from n, remove largest number and add new nums[i]
        
        
        minusnums = [-n for n in nums]
        lrsum, rlsum = [0] * (3*n), [0] * (3*n)
        lrheap, rlheap = minusnums[:n], nums[n*2:]
        heapq.heapify(lrheap) # max heap 
        heapq.heapify(rlheap) # min heap
        
        # Left -> Right 
        lrsum[n-1] = sum(nums[:n]) # only valid in demilitarized zond (n [n] n)
        for i in range(n, 2*n): 
            b = nums[i]
            a = heapq.heappop(lrheap)
            heapq.heappush(lrheap, -b)
            
            lrsum[i] = lrsum[i-1] - (-a) + b
        print (lrsum)
        
        # Left <- Right 
        rlsum[n* 2] = sum(nums[n*2:])
        for i in range(n*2-1, n-1, -1):
            b = nums[i]
            a = heapq.heappop(rlheap)
            heapq.heappush(rlheap, b)
            
            rlsum[i] = rlsum[i+1] - a + b
        print (rlsum)
        
        output = float('inf')
        for i in range(n-1, n*2):
            output = min(output, lrsum[i]-rlsum[i+1])
        return output 