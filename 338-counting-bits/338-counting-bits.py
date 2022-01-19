class Solution:
    def countBits(self, n: int) -> List[int]:
        # repetitive length = 1, 2, 4, 8, ..
        L = n + 1
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        output, gap, counter = [0, 1], 2, 2
        for i in range(2, L):
            if counter == 0:
                counter = gap
                gap = gap * 2 
            output.append(output[i-gap] + 1)
            counter -= 1
        return output 
            
        