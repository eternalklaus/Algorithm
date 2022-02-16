class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort() # 1 3 9 2 4 18
        counter, balance, output = Counter(), 0, []
        
        for val in changed:
            
            if counter[val] == 0: # on
                counter[val * 2] += 1
                balance += 1
                output.append(val)
            
            elif counter[val] >= 1:
                counter[val] -= 1
                balance -= 1
        
        # print (balance, output)
        if balance == 0:
            return output 
        return []