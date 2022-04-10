class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # linear time approach 
        
        # O(n)
        set_timePoints = set(timePoints) 
        if len(set_timePoints) != len(timePoints):
            return 0
        timePoints = list(set_timePoints)
        
        # sort timepoints 
        timePoints.sort()
        
        # get minimum difference 
        mindiff, L = 60 * 24, len(timePoints)
        timePoints += timePoints
        
        def diff(time1, time2):
            h1, m1 = time1.split(':')
            h2, m2 = time2.split(':')
            m1 = int(h1) * 60 + int(m1)
            m2 = int(h2) * 60 + int(m2)
            return (m2 - m1) % (24*60)
        
        for i in range(L):
            time1, time2 = timePoints[i], timePoints[i+1]
            mindiff = min(mindiff, diff(time1, time2))
        return mindiff