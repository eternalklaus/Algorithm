class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        traceroute = []
        n = len(board)
        i = j = 0

        def isvalid(i, j, newval, mode):
            if mode == 'coloum':
                for c in range(n):
                    if board[c][j] == newval:
                        return False 
                return True 
            
            elif mode == 'row':
                for r in range(n):
                    if board[i][r] == newval:
                        return False 
                return True 
            
            elif mode == 'rectangle':
                for c in range(int(i/3)*3, int(i/3)*3+3):
                    for r in range(int(j/3)*3, int(j/3)*3+3):
                        if board[c][r] == newval:
                            return False 
                return True 
            
        def getnewval(i, j, currentval):
            if currentval == '.': newval = 1
            else: newval = currentval + 1
            
            while newval <= n:
                if isvalid(i, j, newval, 'coloum') and isvalid(i, j, newval, 'row') and isvalid(i, j, newval, 'rectangle'):
                    return newval 

                else: newval += 1
            
            return False # cannot get newval.. something's went wrong at the past steps. 


        # Initialize traceroute
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    traceroute.append([i, j])
        
        # trace 
        pivot = 0
        while pivot < len(traceroute):
            [i, j] = traceroute[pivot]
            
            currentval = board[i][j] 
            newval = getnewval(i, j, currentval)
            print ("getnewval(%d, %d, %s) : {}".format(newval) % (i,j,str(currentval)))
            if newval == False:
                pivot -= 1
                continue 
            
            board[i][j] = newval
            print ('[SET!] board[%d][%d] = %d' % (i, j, newval))
            pivot += 1
            
        
