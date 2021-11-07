class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        Q = []
        for [x, y] in points:
            heappush(Q, ((x**2+y**2), x, y))
        
        output = []
        while k > 0:
            (dist, x, y) = heappop(Q)
            output.append([x,y])
            k -= 1
        
        return output
            