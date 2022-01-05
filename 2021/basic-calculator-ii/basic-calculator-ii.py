class Solution:
    def calculate(self, s: str) -> int:
        import math
        stack = []
        def update(num, opr):
            if opr == '+':
                stack.append(num)
            elif opr == '-':
                stack.append(-num)
            elif opr == '*':
                a = stack.pop()
                b = num 
                stack.append(a*b)
            elif opr == '/':
                a = stack.pop()
                b = num 
                result = a / b 
                if result > 0:
                    stack.append(math.floor(result))
                else:
                    stack.append(math.ceil(result))
            
        num = 0
        prevnum, prevopr = 0, '+'

        for c in s:
            if c in ['+', '-', '*', '/']:
                # calculate previous operation
                update(prevnum, prevopr)
                prevnum = 0 
                prevopr = c 
            elif c.isdigit():
                prevnum = prevnum * 10 + int(c)
        
        update(prevnum, prevopr) # last update 
        
        return sum(stack)
