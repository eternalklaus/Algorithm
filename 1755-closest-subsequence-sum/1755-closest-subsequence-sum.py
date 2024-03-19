class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def fn(nums):
            ans = {0}
            for x in nums: 
                ans |= {x + y for y in ans}
            return ans 
        
        L = len(nums)
        output = inf
        nums0 = sorted(fn(nums[:L//2])) ### //2가 없으면 memory limit exceeded..
        nums1 = fn(nums[L//2:])
        for a in nums1:
            i = bisect.bisect_left(nums0, goal-a) ###
            b1 = nums0[min(i, len(nums0)-1)]
            b2 = nums0[max(0,i-1)]
            output = min(output, abs(a+b1-goal), abs(a+b2-goal))
        return output
        