class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        while len(output) < n + 1:
            output = output + [x+1 for x in output]
        return output[:n+1]