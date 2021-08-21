class Solution:
    import operator
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {'+': operator.add, '-':operator.sub, '*':operator.mul}

        def calc(list1, list2, exp):
            computedvals = [] # // computedvals = set()
            if not(list1 and list2): return list1 or list2
            for v1 in list1: 
                for v2 in list2: 
                    computedvals.append(ops[exp](v1, v2))
            return computedvals

        @cache
        def getval(lo, hi): 
            if lo>hi:  return [] 

            computedvals = []
            for i in range(lo, hi):
                if expression[i] in '+-*':
                    list1 = getval(lo, i)
                    list2 = getval(i+1, hi)
                    computedvals += calc(list1, list2, expression[i])
            
            if computedvals: return computedvals
            else: return [int(expression[lo:hi])]  # if nothing in computedvals it means *-+ isn't in expression[lo:hi]

        return getval(0, len(expression))