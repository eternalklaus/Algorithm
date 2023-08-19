class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        L = len(nums)
        
        # Time: O(nlogn) Space: O(1)
        '''
        nums.sort()
        for i in range(L):
            if nums[i] != i:
                return i
        return L
        '''
        # [Follow up]
        # Time: O(n) space: O(1)
        total = L * (L+1) // 2 
        return total - sum(nums)