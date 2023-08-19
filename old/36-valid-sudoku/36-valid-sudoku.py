class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row, col, sub-box
        L = len(board)
        
        collist, rowlist = set(), set()
        for i in range(L):
            collist.clear()
            rowlist.clear()
            for j in range(L):
                if board[i][j].isdigit() and board[i][j] in collist: return False 
                if board[j][i].isdigit() and board[j][i] in rowlist: return False 
                collist.add(board[i][j])
                rowlist.add(board[j][i])
        
        def validbox(idxi, idxj):
            move = [-1, 0, 1]
            boxlist = set()
            for i in move:
                for j in move:
                    if not board[idxi+i][idxj+j].isdigit(): continue 
                    if board[idxi+i][idxj+j] in boxlist: 
                        return False 
                    boxlist.add(board[idxi+i][idxj+j])
            return True 
        
        mi, mj = 1, 1
        boxlist = set()
        for i in range(1, L, 3):
            boxlist.clear()
            for j in range(1, L, 3):
                if not validbox(i, j): return False 
        return True
                