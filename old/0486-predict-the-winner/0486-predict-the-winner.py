class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def player1(turn, li, ri):
            if li > ri:
                return 0
            if turn == 1:
                future1 = nums[li] + player1(2, li+1, ri)
                future2 = nums[ri] + player1(2, li, ri-1)
                return max(future1, future2)
            if turn == 2:
                future1 = player1(1, li+1, ri)
                future2 = player1(1, li, ri-1)
                return min(future1, future2)
            
        score = player1(1, 0, len(nums)-1)
        total = sum(nums)
        return score >= total - score 