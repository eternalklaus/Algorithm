class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointer approach 
        nums.sort()
        checked = set()
        output = set() 
        
        # first value 
        for li in range(len(nums)):
            if nums[li] in checked:
                continue 
            if nums[li] > 0: # n1 should be negative number 
                break 
            
            checked.add(nums[li])
            mi, ri = li+1, len(nums)-1
            
            
            while mi < ri:
                if nums[mi] + nums[ri] == -nums[li]:
                    output.add(tuple([nums[li], nums[mi], nums[ri]]))
                    mi += 1
                    ri -= 1
                    
                elif nums[mi] + nums[ri] > -nums[li]:
                    ri -= 1
                
                elif nums[mi] + nums[ri] < -nums[li]:
                    mi += 1
            
        return output
                    
            
                
                
        