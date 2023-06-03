class Solution:
    def minimumCost(self, s: str) -> int:
        L = len(s)
        def cost(i):
            return min(i, L-i)
        
        befc, output = s[0], 0
        for i, c in enumerate(s):
            if befc != c:
                output += cost(i) # change [0:i] vs change [i+1:]
            befc = c
        return output 