class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures = [(temperatures[i], i) for i in range(len(temperatures))]
        output = []
        
        stack = [(-1,-1)]
        for t, i in temperatures[::-1]:
            while stack: # 스택에서 나보다 (같거나) 약한놈들 kill
                top = stack[-1][0]
                
                if top <= t:
                    stack.pop()
                else:
                    break
            
            if stack: # 스택에 나보다 큰놈이 생존해있다면
                ri = stack[-1][1]
                dist = ri - i
                output.append(dist)
            else:
                output.append(0)
            
            stack.append((t, i))
        
        return output[::-1]