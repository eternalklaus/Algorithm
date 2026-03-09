class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x:(x[0],-x[1]))
        
        values = [(0,0)]
        for price, beauty in items:
            p,b = values[-1]
            if p == price: continue 
            
            maxb = max(b, beauty)
            values.append((price, maxb))
        
        output = []
        for p in queries:
            i = bisect.bisect(values, (p, 10**9+1))
            output.append(values[i-1][1])
        return output