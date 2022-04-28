# [1,4,5,6] -> 0:0 1:1 ### bisect = "equal or bigger
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = [-p for p in people]
        people.sort()
        output = 0
        while people: # [-4, -3, -2, -1]
            p1_val = people.pop(0)
            p2_val = limit + p1_val 
            p2_idx = bisect.bisect(people, -p2_val-1) # bigger value!!! if finding 1 and [1], returns idx 1. 
            # print (people)
            # print (p1_val, p2_val, p2_idx)
            if p2_idx < len(people):
                people.pop(p2_idx)
            
            output += 1
                
        return output 