class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # from heigest day, the next days are vain
        stack= []
        total = len(temperatures)
        output = [0 for _ in range(total)]
        
        for i in range(total-1, -1, -1): # reversed order
            diff = 0
            while stack:
                pt, pi = stack.pop() # previous t, previous i
                if pt > temperatures[i]:
                    diff = pi - i
                    stack.append((pt, pi)) # re-push most warm day into stack
                    break
            
            stack.append((temperatures[i], i)) # push current day into stack
            output[i] = diff
        return output
                    
                