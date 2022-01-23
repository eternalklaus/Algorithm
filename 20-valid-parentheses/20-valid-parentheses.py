class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in bracket:
                stack.append(c)
            else:
                if not stack: 
                    return False 
                
                c_close = c
                c_open  = stack.pop() 
                if c_open not in bracket or bracket[c_open] != c_close:
                    return False 
        
        return not stack