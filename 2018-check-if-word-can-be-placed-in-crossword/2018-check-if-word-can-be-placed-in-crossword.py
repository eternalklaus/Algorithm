class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        I, J = len(board), len(board[0])
        
        def compare(candidate, word):
            # print ('-'+candidate+'-', word)
            if len(candidate) != len(word): return False
            result1, result2 = True, True
            
            for c1, c2 in zip(candidate, word):
                if c1 == c2: continue 
                if c1 == ' ': continue
                else: 
                    result1 = False
                    break
            
            for c1, c2 in zip(candidate, word[::-1]):
                if c1 == c2: continue 
                if c1 == ' ': continue 
                else: 
                    result2 = False
                    break
            
            return result1 or result2
            
        candidate = ''
        # left to right check
        for i in range(I):
            for j in range(J):
                c = board[i][j]
                if c == '#':
                    if compare(candidate, word): return True
                    candidate = ''
                    continue 
                candidate += c
                if j == J-1:
                    if compare(candidate, word): return True
                    candidate = ''
                    continue 
        
        candidate = ''
        # top to bottom check
        for j in range(J):
            for i in range(I):
                c = board[i][j]
                if c == '#':
                    if compare(candidate, word): return True
                    candidate = ''
                    continue
                candidate += c
                if i == I-1:
                    if compare(candidate, word): return True
                    candidate = ''
                    continue 