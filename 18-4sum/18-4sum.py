class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        L, output = len(nums), set()
        
        # pick two number from the left 
        for i1 in range(L):
            for i2 in range(i1+1, L):
                newtarget = target - nums[i1] - nums[i2]
                li, ri = i2+1, L-1
                while li < ri:
                    temp = nums[li] + nums[ri]
                    if temp == newtarget:
                        output.add((nums[i1], nums[i2], nums[li], nums[ri]))
                        ri -= 1
                        li += 1
                        ### break <- do not break. there can be another pairs.
                    elif temp > newtarget:
                        ri -= 1
                    if temp < newtarget:
                        li += 1
        return output 