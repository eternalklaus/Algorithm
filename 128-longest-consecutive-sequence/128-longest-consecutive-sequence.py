class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        output = 0
        
        while nums:
            n = nums.pop()
            cnt = 1
            rn, ln = n+1, n-1
            
            while rn in nums:
                nums.remove(rn)
                cnt, rn = cnt+1, rn+1
            
            while ln in nums:
                nums.remove(ln)
                cnt, ln = cnt+1, ln-1
            output = max(output, cnt)
            
        return output 