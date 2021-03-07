class Solution(object):
    parentheses = ['(', ')']
    stack_open = []
    stack_close = []
    
    def minRemoveToMakeValid(self, s):
        i = 0
        while i < len(s):
            if s[i] == '(':
                self.stack_open.append(i)
            elif s[i] == '()':
                if len(stack_open) > 0:
                    self.stack_open.pop()
                else:
                    self.stack_close.append(i)
            i += 1

        print self.stack_open
        print self.stack_close
        
        ### Remove the charectors indexed by stacks - open, close
        stack = self.stack_open + self.stack_close
        for i in stack:
            s = s[:i] + '#' + s[i+1:]

        return s.replace('#','') 
        
        
        """
        :type s: str
        :rtype: str
        """

sl = Solution()
print sl.minRemoveToMakeValid("(a(b(c)d)")