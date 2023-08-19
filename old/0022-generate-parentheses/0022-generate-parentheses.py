class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking 
        
        output = []
        
        def backtracking(line, pushcnt, popcnt):
            if len(line) == 2*n:
                output.append(line)
                return 
            
            if pushcnt == n:
                backtracking(line + ')', pushcnt, popcnt+1)
                return
            
            if pushcnt == popcnt:
                backtracking(line + '(', pushcnt+1, popcnt)
                return
            
            backtracking(line + ')', pushcnt, popcnt+1)
            backtracking(line + '(', pushcnt+1, popcnt)
            return
        
        backtracking('', 0, 0)
        return output 
            