class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        i, stack, L = 0, [], len(s)
        
        def stackcalc():
            nonlocal stack 
            preval, output = '0', 0
            
            while stack:
                x = stack.pop()
                if x == '(': break 
                    
                if x == '+':
                    output += int(preval)
                    preval = '0'
                elif x == '-':
                    output -= int(preval)
                    preval = '0'
                else: # numeric value 
                    preval = x 
            output += int(preval)
            return str(output)
        
        while i<L:
            # print (stack)
            if s[i] == ')': 
                val = stackcalc() 
                stack.append(val)
                i += 1
                
            elif s[i].isnumeric():
                ri = i+1
                while ri < L and s[ri].isnumeric():
                    ri += 1 
                stack.append(s[i:ri])
                i = ri
            
            else: # (, +, -
                stack.append(s[i])
                i += 1
        
        return stackcalc()