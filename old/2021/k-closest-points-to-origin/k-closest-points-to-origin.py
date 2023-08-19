class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dists = {}
        
        for [x,y] in points:
            dist = x**2 + y**2
            if dist not in dists: 
                dists[dist] = []
            dists[dist].append([x,y])
        
        output = []
        for dist in sorted(dists.keys()):
            output += dists[dist]
            if len(output) >= k: break
        return output[:k]
                
            