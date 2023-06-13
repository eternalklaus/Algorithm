class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def bit2set(bitmask):
            numbers = set()
            for i in range(maxChoosableInteger):
                if bitmask & 1<<i == 0:
                    numbers.add(i)
            return numbers
                
        @cache
        def player1(total, bitmask):
            numbers = bit2set(bitmask)
            if total >= desiredTotal: 
                return False # 이미 상대가 이긴상태로 넘겨줌...
            
            for number in numbers:
                if player2(total+(number+1), bitmask | 1<<number) == False:
                    return True 
            return False
        
        @cache
        def player2(total, bitmask):
            numbers = bit2set(bitmask)
            if total >= desiredTotal: 
                return False 
            
            for number in numbers:
                if player1(total+(number+1), bitmask | 1<<number) == False:
                    return True 
            return False
                
                
        
        if desiredTotal == 0:
            return True 
        if desiredTotal > (maxChoosableInteger) * (maxChoosableInteger+1) / 2: # 이룰 수 없는 꿈
            return False 
        return player1(0, 0)