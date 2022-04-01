class Solution:
    import math 
    def evalRPN(self, tokens: List[str]) -> int:
        # push numbers into stack, and if we encounter operator, pop two numbers
        stack = []
        for token in tokens:
            if token.isnumeric() or token[1:].isnumeric(): # token.startswith('-'): 
                stack.append(token) 
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                result = eval(f'{num1} {token} {num2}')
                if result % 1:
                    if result > 0: result = math.floor(result)
                    else: result = math.ceil(result)
                stack.append(result)
        return int(stack[0])