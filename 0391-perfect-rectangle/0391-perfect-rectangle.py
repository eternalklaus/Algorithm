class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        MAX = 10**5
        minx = miny = MAX+1
        maxx = maxy = -MAX-1
        
        getarea = lambda: (x2-x1) * (y2-y1) ### x를 명시해주지 않을시 들어온 파라미터 이름 따라감
        
        area = 0
        vertex = set()
        for x1,y1,x2,y2 in rectangles:
            area += getarea() ### 파라미터를 안건네준다..?
            minx, miny = min(minx, x1), min(miny, y1)
            maxx, maxy = max(maxx, x2), max(maxy, y2)
            # 양쪽 네꼭지점 제외하고는 2회 or 4회 나타난다 
            vertex ^= {(x1,y1),(x1,y2),(x2,y1),(x2,y2)}
        
        if vertex != {(minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)}:
            return False
        
        x1,y1,x2,y2 = minx, miny, maxx, maxy
        if area != getarea():
            return False
        return True