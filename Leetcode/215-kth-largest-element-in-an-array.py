# Input: nums = [3,2,1,5,6,4], k = 2


class Solution(object):
    def findKthLargest(self, nums, k):
        # terminate condition
        if len(nums) <= 1: 
            
        
        pivot = 0
        lnums = []
        rnums = []
        for i in range(1, len(nums)):
            if nums[i] < nums[pivot]:
                lnums.append(nums[i])
            elif nums[i] >= nums[pivot]:
                rnums.append(nums[i])
        
        if len(lnums) == k-1:
            return nums[pivot]
        elif len(lnums) >= k:
            return self.findKthLargest(lnums, k) # We don't have to sort rnums
        elif len(lnums) < k:
            return self.findKthLargest(rnums, k - len(lnums))
        
        
