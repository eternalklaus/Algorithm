class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = filter(lambda x: x in nums2, nums1)
        return set(output)