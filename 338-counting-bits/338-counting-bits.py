class Solution:
    def countBits(self, n: int) -> List[int]:
        L = n + 1
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        # Add values one by one. leverage that output has below pattern
        # [0, 1] [0+1, 1+1]
        # [0, 1,    1,   2] [1+1, 2+1, 2+1, 3+1]
        # ...
        # such pattern repeates every 1, 2, 4, 8, 16 ..
        '''
        output, gap, counter = [0, 1], 2, 2
        for i in range(2, L):
            if counter == 0:
                counter = gap
                gap = gap * 2 
            output.append(output[i-gap] + 1)
            counter -= 1
        return output 
        '''
        output = [0, 1]
        while len(output) < L:
            output += [x+1 for x in output]
        return output[:L]
        