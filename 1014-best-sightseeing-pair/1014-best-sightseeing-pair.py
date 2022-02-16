class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        pick1, output = values[0], values[0] + values[1] - 1
        
        for i, pick in enumerate(values[1:], 1):
            output = max(output, pick1 + pick - i)
            pick1 = max(pick1, pick + i)

        return output 