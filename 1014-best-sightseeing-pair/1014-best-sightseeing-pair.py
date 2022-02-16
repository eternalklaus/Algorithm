class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # sweeping approach?
        
        L = len(values)
        lr, rl = [0]*L, [0]*L
        
        # left -> right
        lr[0] = values[0] # initialize
        for i in range(1, L):
            lr[i] = max(lr[i-1]-1, values[i])
        # print (lr)
        
        # left <- right
        rl[-1] = values[-1]
        for i in range(L-2, -1, -1):
            rl[i] = max(rl[i+1]-1, values[i])
        # print (rl)
        
        # get output
        output = 0
        for i in range(L-1):
            output = max(output, lr[i]+rl[i+1]-1)
        return output 
        