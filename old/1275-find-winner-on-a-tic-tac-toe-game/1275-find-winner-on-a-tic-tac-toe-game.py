class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        output = 'Draw'
        L = len(moves)
        A = set([tuple(moves[i]) for i in range(L) if i % 2 == 0])
        B = set([tuple(moves[i]) for i in range(L) if i % 2 == 1])
        
        for i in range(3):
            if (i,0) in A and (i,1) in A and (i,2) in A: return 'A'
            if (i,0) in B and (i,1) in B and (i,2) in B: return 'B'
        for j in range(3):
            if (0,j) in A and (1,j) in A and (2,j) in A: return 'A'
            if (0,j) in B and (1,j) in B and (2,j) in B: return 'B'

        
        if (0,0) in A and (1,1) in A and (2,2) in A: return 'A'
        if (0,0) in B and (1,1) in B and (2,2) in B: return 'B'
        if (2,0) in A and (1,1) in A and (0,2) in A: return 'A'
        if (2,0) in B and (1,1) in B and (0,2) in B: return 'B'
            
        if len(moves) != 9:
            output = 'Pending'
        return output 
        