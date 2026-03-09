class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        lmini = 0
        lmaxi = 0
        for i, x in enumerate(nums[indexDifference:], indexDifference):
            i1, i2 = i-indexDifference, i
            if nums[i1] < nums[lmini]:
                lmini = i1
            if nums[i1] > nums[lmaxi]:
                lmaxi = i1
                
            if nums[i] - nums[lmini] >= valueDifference:
                return [lmini, i]
            if nums[lmaxi] - nums[i] >= valueDifference:
                return [lmaxi, i]

            
        return [-1, -1]
            
            

