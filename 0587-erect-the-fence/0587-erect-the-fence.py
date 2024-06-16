class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        start = min(trees, key=lambda x:(x[1],x[0]))
        
        def polar_angle(point): # sort trees in counterclockwise order based on polar angle from the start...
            x1,x2 = start[0],point[0]
            y1,y2 = start[1],point[1]
            return atan2(y2-y1, x2-x1)

        def distance(point):
            x1,x2 = start[0],point[0]
            y1,y2 = start[1],point[1]
            return (y2-y1)**2 + (x2-x1)**2

        trees.sort(key=lambda p:(polar_angle(p),distance(p))) 
        
        def counter_clockwise(p1,p2,p3):
            (x1,y1),(x2,y2),(x3,y3) = p1,p2,p3
            return (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2) >= 0 # all the trees that included in the fence(vertice)..

        # graham scan
        upper = []
        for point in trees:
            while len(upper) >= 2 and not counter_clockwise(upper[-2],upper[-1],point):
                upper.pop()
            upper.append(point)
        
        trees = reversed(trees)
        lower = []
        for point in trees:
            while len(lower) >= 2 and not counter_clockwise(lower[-2],lower[-1],point):
                lower.pop()
            lower.append(point)
        
        return list(set(map(tuple, lower+upper)))
