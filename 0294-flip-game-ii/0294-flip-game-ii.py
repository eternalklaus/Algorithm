class Solution:
    def canWin(self, currentState: str) -> bool:
        # 나: 최대한 뒤집는다
        # 상대: (거드름을피우며) 최대한 방해한다
        
        @cache
        def minimax(currentState, player):
            if '++' not in currentState:
                return 3-player
            
            indexs = [i for i in range(len(currentState)) if currentState[i:i+2] == '++']
            
            if player == 1:
                for idx in indexs:
                    if minimax(currentState[:idx] + '--' + currentState[idx+2:], 2) == 1: # 하나라도 나한테 유리한 증거가 나오면 올인
                        return 1
                return 2
            
            if player == 2:
                for idx in indexs:
                    if minimax(currentState[:idx] + '--' + currentState[idx+2:], 1) == 2: 
                        return 2
                return 1
        
        
        return minimax(currentState, 1) == 1