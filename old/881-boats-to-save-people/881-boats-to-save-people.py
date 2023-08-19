class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        output = 0

        # two pointer 
        li, ri = 0, len(people)-1
        while li <= ri:
            capacity = limit 
            # increase li 
            capacity -= people[li]
            li += 1
            # decrease ri 
            if people[ri] <= capacity:
                ri -= 1
            output += 1
        return output 
