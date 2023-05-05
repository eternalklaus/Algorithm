class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        import heapq
        costs = {} # costs : {(x,y):cost}
        heap = [(0, start[0], start[1])] # heap  : w, x, y
        while heap:
            (weight,x,y) = heapq.heappop(heap)
            for x1,y1,x2,y2,specialweight in specialRoads:
                # 다 연결된거나 다름없잖아?
                # compare route x,y -> x2,y2 and x,y->x1,y1->x2,y2
                # and if route is new discovered route (not in the costs), add those in heap
                
                #         x,y              ->         x2,y2
                route1 = weight + abs(x2-x)+abs(y2-y)
                
                #         x,y              ->         x1,y1    ->     x2,y2
                route2 = weight + abs(x1-x) + abs(y1-y) + specialweight
                
                newroute = min(route1, route2)
                originalroute = costs.get((x2,y2), float('inf'))
                
                if newroute < originalroute:
                    heapq.heappush(heap, (newroute, x2, y2))
                    costs[(x2,y2)] = newroute
            
        # print (costs)
        # get weight to target
        tx, ty = target
        output = float('inf')
        for (x,y), cost in costs.items():
            output = min(cost + abs(tx-x) + abs(ty-y), output)
        return output