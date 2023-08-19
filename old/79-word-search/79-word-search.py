class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(point, idx):
            # base case
            if idx == len(word):
                return True 
            
            i, j = point 
            
            # base case: out of board
            if not ((0<= i < len(board)) and (0 <= j < len(board[0]))): # d morgan's law
                return False 
            
            # not match
            if board[i][j] != word[idx]:
                return False 
            
            # recursiely call search
            board[i][j] =  '' # ord(board[i][j]) ### mark this char has been checked
            output = search([i+1,j], idx+1) or search([i,j+1], idx+1) or search([i-1,j], idx+1) or search([i,j-1], idx+1)
            board[i][j] =  word[idx] # chr(board[i][j]) 
            return output 
        
        start = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search([i, j], 0):
                    return True 
        return False
                     