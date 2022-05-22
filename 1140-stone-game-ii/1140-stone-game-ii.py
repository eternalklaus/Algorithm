class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def minimax(M, li, turn):
            if li >= len(piles):
                return 0
            if turn == 'A': # max
                return max([sum(piles[li:ri]) + minimax(max(M, ri-li), ri, 'B') for ri in range(li+1, li+(M*2)+1)])
            if turn == 'B': # mini
                return min([minimax(max(M, ri-li), ri, 'A') for ri in range(li+1, li+(M*2)+1)])
        return minimax(1, 0, 'A')