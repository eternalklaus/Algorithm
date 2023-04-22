class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # size = n 인곳의 push-pop 조합 
        
        # state: ( -> 1, (( -> 2, () -> 0
        # usedpush: (()( -> 3. so it used all of the push life!
        output = []
        
        @cache
        def dfs(line, state, usedpush): 
            if len(line) == 2*n:
                output.append(line)
                return
            
            if usedpush == n: # only choice(close) - consumed all the opportunity of pushes../
                dfs(line+')', state-1, usedpush)
                return
            
            if state == 0: # only choice(open)
                dfs(line+'(', state+1, usedpush+1)
                return
            
            dfs(line+')', state-1, usedpush)
            dfs(line+'(', state+1, usedpush+1)
        
        dfs('', 0, 0)
        return output
                