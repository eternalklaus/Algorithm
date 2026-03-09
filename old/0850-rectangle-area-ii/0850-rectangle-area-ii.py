class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MAX, MOD = 10**9+1, 10**9+7
        # get area considering overlapped area
        def calcarea(ylst):
            mina=maxb=-1
            ylst.append((MAX, MAX))
            ylst.sort()
            output = 0
            for a,b in ylst:
                if maxb < a: 
                    output += (maxb-mina)
                    output %= MOD
                    mina, maxb = a, b
                else:
                    maxb = max(maxb, b)
            return output % MOD
        
        cnt = defaultdict(Counter)
        for x1,y1,x2,y2 in rectangles:
            cnt[x1][(y1,y2)] += 1
            cnt[x2][(y1,y2)] -= 1
        
        xlst = sorted(cnt.keys())
        ypaircnt = Counter()
        output = 0
        for x, xright in zip(xlst, xlst[1:]):
            width = xright-x
            for ypair in cnt[x]:
                ypaircnt[ypair] += cnt[x][ypair]
            ylst = [ypair for ypair in ypaircnt if ypaircnt[ypair] > 0]
            output += width * calcarea(ylst)
            output %= MOD
        return output