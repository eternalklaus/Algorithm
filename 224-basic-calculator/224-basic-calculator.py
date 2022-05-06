class Solution:
    def calculate(self, s: str) -> int:
        # push it simply, pop it calculation
        def getval(stack):
            # pop stack until '(' appears 
            output, val = 0, 0
            while stack:
                x = stack.pop()
                if x == '(': break
                    
                if x.isnumeric() or x[1:].isnumeric():
                    val = int(x)
                elif x == '-':
                    output -= val 
                    val = 0
                elif x == '+':
                    output += val 
                    val = 0
                    
            return output + val
        
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ')':
                val = getval(stack)
                
                stack.append(str(val))
                i += 1
                continue 
            
            elif s[i].isnumeric():
                ri = i
                while ri < len(s) and s[ri].isnumeric():
                    ri += 1
                stack.append(s[i:ri])
                i = ri
                continue 
            
            else:
                stack.append(s[i]) # if +, -, (
                i += 1
                continue
                
        print (stack)
        return getval(stack)