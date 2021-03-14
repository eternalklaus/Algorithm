'''
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''
class Solution(object):
    def searchRange(self, nums, target):
        i = 0
        j = len(nums) - 1
        I = -1
        J = -1
        while i <= j:
            if I != -1 and J != -1: break 

            if I == -1:
                if nums[i] == target:
                    I = i 
                else:
                    i += 1
            
            if J == -1:
                if nums[j] == target:
                    J = j
                else:
                    j -= 1
        
        return [I, J]

