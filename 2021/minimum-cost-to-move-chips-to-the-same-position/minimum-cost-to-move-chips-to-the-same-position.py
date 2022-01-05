class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # move 2 step = cost 0
        # move 1 step = cost 1
        
        # all of the coins will choke together into 2 (No money is wasted)
        pos = {0:0, 1:0}
        for p in position:
            if p % 2 == 0:
                pos[0] += 1
            else:
                pos[1] += 1
        
        # We should cost money
        return min(pos[0], pos[1])
        
        