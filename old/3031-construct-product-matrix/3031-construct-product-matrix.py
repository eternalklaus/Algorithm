class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        I, J = len(grid), len(grid[0])
        pref, suff = [1], [1]

        for i in range(I):
            for j in range(J):
                pref.append(grid[i][j] * pref[-1] % 12345)

        for i in reversed(range(I)):
            for j in reversed(range(J)): ### 이부분
                suff.append(grid[i][j] * suff[-1] % 12345)
        suff.reverse()
        
        for i in range(I):
            for j in range(J):
                prefidx = i * J + j ###
                suffidx = prefidx + 1
                grid[i][j] = pref[prefidx] * suff[suffidx] % 12345
        
        return (grid)
        print ('after return')
