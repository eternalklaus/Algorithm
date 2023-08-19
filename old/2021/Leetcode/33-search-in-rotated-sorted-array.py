class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi: # lo <= hi. becuse we returns mid.  
            mid = (lo + hi) // 2 # Fixed rule
            
            if nums[mid] == target:
                return mid 
            # left is normal, right is rotated
            if nums[lo] <= nums[mid]: # <= consider the case "lo == mid" as normal
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1 # we can exclude mid since we returns mid
                else:
                    lo = mid + 1
            else: # left is rotated, right is normal  
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1