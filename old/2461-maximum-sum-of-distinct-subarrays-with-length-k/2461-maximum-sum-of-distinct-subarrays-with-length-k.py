class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # left 이동 케이스: len > k, nums[i] exists in sets
        # right 이동 케이스: always
        left, right = 0, -1
        output = 0
        window = {}
        windowsum = 0
        while True:
            right += 1
            if right >= len(nums): break
            
            if nums[right] in window: 
                idx = window[nums[right]]
                left = idx + 1
                right = idx
                window = {} # 윈도우 호핑 초기화
                windowsum = 0
            
            else:
                while right - left + 1 > k:
                    del window[nums[left]]
                    windowsum -= nums[left]
                    left += 1
                window[nums[right]] = right
                windowsum += nums[right]
            
            if len(window) == k:
                output = max(windowsum, output)
        return output


