class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # register all point into the dictionary
        from collections import defaultdict 
        roads = defaultdict(list)

        def register_roads(tickets):
            for ticket in tickets:
                [src, dst] = ticket
                roads[src].append(dst)
            return roads
        
        def greedy(itineray, roads, nroads):
            if nroads == 0: 
                return itineray 
            
            src = itineray[-1]
            if not roads[src]: 
                return False

            dsts = sorted(roads[src])
            for dst in dsts:
                # backtracking - popping
                itineray.append(dst)
                roads[src].remove(dst) # // remove is delete component by value 
                
                result = greedy(itineray, roads, nroads-1) # // takes only first component. its similar to greedy...?
                if result: return result

                # backtracking - repushing
                itineray.pop()
                roads[src].append(dst)


        roads = register_roads(tickets)
        return greedy(['JFK'], roads, len(tickets))