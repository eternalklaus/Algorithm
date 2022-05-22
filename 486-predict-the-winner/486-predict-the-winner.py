class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # optimally
        from functools import lru_cache
        
        @lru_cache
        def minimax(turn, li, ri):
            if li == ri: return 0
            
            if turn == 1:
                return max(nums[ri-1] + minimax(2, li, ri-1), nums[li] +  minimax(2, li+1, ri))
            if turn == 2:
                return min(minimax(1, li, ri-1), minimax(1, li+1, ri))
        
        player1 = minimax(1, 0, len(nums))
        # print (player1)
        return player1 >= sum(nums)-player1
        