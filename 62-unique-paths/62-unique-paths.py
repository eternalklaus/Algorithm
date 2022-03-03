class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        I, J = m, n
        
        line = [1] * J
        for i in range(I-1):
            for j in range(J):
                if j == 0: continue 
                line[j] = line[j] + line[j-1]
        
        return line[J-1]