

["DetectSquares", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "count"]
[[], [[5, 10]], [[10, 5]], [[10, 10]], [[3, 0]], [[8, 0]], [[8, 5]], [[9, 0]], [[9, 8]], [[1, 8]], [[0, 0]], [[8, 0]], [[8, 8]], [[1, 9]], [[2, 9]], [[2, 10]], [[7, 8]], [[2, 3]], [[2, 8]], [[9, 10]], [[9, 5]], [[4, 5]], [[0, 9]], [[4, 5]], [[4, 9]], [[1, 10]], [[10, 1]], [[10, 10]], [[10, 0]], [[2, 0]], [[2, 8]], [[7, 6]], [[4, 6]], [[4, 9]], [[10, 9]], [[10, 0]], [[1, 0]], [[1,9]]]

class DetectSquares:
    from collections import defaultdict, Counter 
    def __init__(self):
        self.xy = defaultdict(set) # ex) {1:set(3,5,6,7,8,8...), 2:set(4,8,9....)
        self.yx = defaultdict(set)
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point 
        self.xy[x].add(y)
        self.yx[y].add(x)
        self.points[(x,y)] += 1 

    def count(self, point: List[int]) -> int:
        x, y = point 
        output = 0
        # Count x, y1/y2/y3/y4 ... 
        
        for yprime in self.xy[x]:
            size, cnt = abs(y - yprime), 0
            # check right side 
            if (x+size, y) in self.points and (x+size, yprime) in self.points: 
                if yprime != y: #!!!
                    c1, c2, c3, c4 = 1, self.points[(x,yprime)], self.points[(x+size,y)], self.points[(x+size,yprime)]
                    output += (c1 * c2 * c3 * c4)

            # check lefft side 
            if (x-size, y) in self.points and (x-size, yprime) in self.points:
                if yprime != y: #!!!
                    c1, c2, c3, c4 = 1, self.points[(x,yprime)], self.points[(x-size,y)], self.points[(x-size,yprime)]
                    output += (c1 * c2 * c3 * c4)

        return output 
