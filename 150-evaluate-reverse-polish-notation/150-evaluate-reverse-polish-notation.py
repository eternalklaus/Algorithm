class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isnumeric() or token[1:].isnumeric(): ### - value isn't considered as numeric
                stack.append(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(eval(f'{num1} {token} {num2}'))) ### // 보다 더 심오한 무언가가 있음 
        return stack[0]
                