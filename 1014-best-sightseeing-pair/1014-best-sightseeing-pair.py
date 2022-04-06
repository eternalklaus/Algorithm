class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
        # pick1 ~ pick2 
        # hold -> sold 랑 유사하구나! 
        hold, sold  = values[0] + 0, 0
        for i, value in enumerate(values[1:], 1):
            sold = max(sold, hold + value - i)
            hold = max(hold, value + i)
        return sold 
