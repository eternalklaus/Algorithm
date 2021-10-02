class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # from heigest day, the next days are vain
        stack= []
        total = len(temperatures)
        output = [0 for _ in range(total)]
        
        for i in range(total-1, -1, -1): # reversed order
            day1, day2 = i, i
            while stack:
                d = stack.pop() 
                if temperatures[d] > temperatures[day1]:
                    day2 = d
                    stack.append(day2) # re-push most warm day into stack
                    print ("%d(%dC) > %d(%dC)" % (day1, temperatures[day1], day2, temperatures[day2]))
                    break
            
            stack.append(day1) # push current day into stack
            output[i] = day2 - day1
        return output
                    
                