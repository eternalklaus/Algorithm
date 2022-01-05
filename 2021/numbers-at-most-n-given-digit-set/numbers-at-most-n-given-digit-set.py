class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        output = 0
        maxnum = []
        numbers = digits
        while n:
            i = str(n % 10)
            n = n // 10 
            maxnum.insert(0, str(i))
        
        # base case
        for i in range(1, len(maxnum)):
            output += len(numbers) ** i 

        def calcit(idx, leftdigit):
            # base case
            # if leftdigit == 0: => still we have to count the 3,4,7
            if leftdigit == -1:
                return 1

            maxval = maxnum[idx]
            output = 0
            for num in numbers:
                if num < maxval: 
                    output += len(numbers) ** leftdigit  
                elif num == maxval: # identical number 
                    output += calcit(idx+1, leftdigit-1)
                else: # num becomes bigger then boundary number
                    break 
            return output 
                
        # boundary case 
        output += calcit(0, len(maxnum)-1) # first index is 0
        return output