class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers)-1
        while lp < rp:
            value = numbers[lp] + numbers[rp]
            if value == target:
                return [lp+1, rp+1]
            elif value < target:
                lp += 1
            elif value > target:
                rp -= 1
        
            