'''
1. Is there minus value exist in list?
2. Is it possible to add same index's value?
3. Is there only one pair of result or multiple pair?
'''
class Solution(object):
    def twoSum(self, nums, target):
        _size = len(nums)
        for i in range(0, _size):
            for j in range(i + 1, _size):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return False
