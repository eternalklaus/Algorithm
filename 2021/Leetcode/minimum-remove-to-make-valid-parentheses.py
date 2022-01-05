class Solution(object):
    
    def minRemoveToMakeValid(self, s):
        stack_open = []   # stack for holding indce of '(' to remove
        stack_close = []  # stack for holding indce of ')' to remove
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack_open.append(i)
            elif s[i] == ')': # '(' and ')' matched
                if len(stack_open) > 0:
                    stack_open.pop()
                else:
                    stack_close.append(i) # sole ')'
            i += 1
        
        
        ### Remove the charectors indexed by stacks - open, close
        stack = stack_open + stack_close
        for i in stack:
            s = s[:i] + '#' + s[i+1:]
        return s.replace('#','') 
        
