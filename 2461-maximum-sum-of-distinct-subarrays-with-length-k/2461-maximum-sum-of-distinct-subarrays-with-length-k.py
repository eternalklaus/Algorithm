class Solution:
    from collections import Counter
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter()
        left = 0
        right = -1
        count_of_one = 0
        currentsum = 0
        maximumsum = 0
        while True:
            # right - left + 1 should be k
            right += 1
            if right == len(nums): break
            counter[nums[right]] += 1
            if counter[nums[right]] == 1: count_of_one += 1
            if counter[nums[right]] == 2: count_of_one -= 1
            currentsum += nums[right]

            if right - left + 1 < k: 
                continue # 아직 비교할 단계가 아니고, 슬라이딩윈도우가 커져가고 있는 단계
            if right - left + 1 > k: # 윈도우 사이즈가 초과됨
                counter[nums[left]] -= 1
                if counter[nums[left]] == 1: count_of_one += 1
                if counter[nums[left]] == 0: count_of_one -= 1
                currentsum -= nums[left]
                left += 1
            
            # print (nums[left:right+1], count_of_one, currentsum)
            if count_of_one == k: 
                maximumsum = max(maximumsum, currentsum)

        return maximumsum
            