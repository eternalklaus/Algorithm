class Solution:
    def countAndSay(self, n: int) -> str:
        def sayit(target:str) -> str: 
            output, li, L = '', 0, len(target)
            while li < L:
                c = target[li]
                ri = li + 1
                while ri < L and target[ri] == c:
                    ri += 1
                    
                output += str(ri - li) + str(c)
                li = ri
            return output 
        
        output = '1'
        for i in range(n-1): # if 1 -> 0st run it
            output = sayit(output)
        return output
        
            