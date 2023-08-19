class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def match(word, w):
            if len(word) != len(w): return False 
            for c1,c2 in zip(word, w):
                if c1 == c2 or c2 == ' ': # exactly match or wildcard match
                    continue
                return False
            return True
            
        def compare(board):
            for w in board:
                w = ''.join(w)
                words = w.split('#')
                for w in words:
                    if match(word, w): return True
                    if match(word[::-1], w): return True
        
        return compare(board) or compare(zip(*board))