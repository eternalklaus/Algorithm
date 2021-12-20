class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        s = '*1[' + s + ']'
        
        def trimstack():
            stri, rept = '', ''
            # pop chars
            while (c:=stack.pop()) != '[': # caution (! the walrus operator
                stri = c + stri
            
            # pop numbers
            while '0' <= (n:=stack.pop()) <= '9':
                rept = n + rept 
            stack.append(n) # restore more-popped one 
            rept = int(rept)

            # re-push string 
            stack.append(rept * stri)
            
            
        for c in s:
            if c == ']':
                trimstack()
            else:
                stack.append(c)
        
        return stack.pop()