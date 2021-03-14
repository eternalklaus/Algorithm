class Solution(object):
    def findKthLargest(self, nums, k):
        # terminate condition
        pivot = 0
        lnums = []
        rnums = []
        for i in range(1, len(nums)): # sort by [max ... min] order
            if nums[i] >= nums[pivot]:
                lnums.append(nums[i])
            elif nums[i] < nums[pivot]:
                rnums.append(nums[i])
        
        if len(lnums) == k-1: # found exact component!
            return nums[pivot]
        elif len(lnums) < k: # search again with right list
            return self.findKthLargest(rnums, k - len(lnums) - 1) # !!! [here] k - len(lnums) incures recursive loop..
        elif len(lnums) >= k: # search again with left list
            return self.findKthLargest(lnums, k) 

        
sl = Solution()
print sl.findKthLargest([7,6,5,4,3,2,1], 2)