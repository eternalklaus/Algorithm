class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(1) space
        total = len(nums)
        counter = Counter(nums)
        for ch in counter:
            if counter[ch] > total//2:
                return ch