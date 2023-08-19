class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        import operator    
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul
        }

        result = []

        
        def calc(list1, op, list2):
            result = []
            for i in list1:
                for j in list2:
                    result.append(ops[op](i, j))
            return result
        
        @cache 
        def dac(exp): # devide and conquar
            result = []
            for i, c in enumerate(exp):
                if c in '+-*':
                   result += (calc(dac(exp[:i]), exp[i], dac(exp[i+1:])))
            
            if not result: # '+-*' not in exp
                result.append(int(exp))
            
            return result
        


        return dac(expression)