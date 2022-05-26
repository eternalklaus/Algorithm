class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # remainder = [(maxChoosableInteger-i) for i in range(maxChoosableInteger)]
        remainder = [i+1 for i in range(maxChoosableInteger)]
        @cache
        def can_win(total, remainder):
            # print (total, remainder)
            if total >= desiredTotal:
                return False # 이미 이전에 조건을 충족해버림..
            
            for num in remainder:
                if can_win(total + num, tuple([n for n in remainder if n != num])) == False: # 상대가 진다면?
                    return True
            return False 
        
        if desiredTotal == 0:
            return True 
        if sum(remainder) < desiredTotal:
            return False 
        return can_win(0, tuple(remainder))