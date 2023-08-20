class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        ### subsequence 용어정의 
        # https://www.geeksforgeeks.org/subarraysubstring-vs-subsequence-and-programs-to-generate-them/

        # k개를 뽑아서 최대 득점을 만들자 

        # Assuming,
        #   general profit: profit
        #   bounus profit:  diversity**2
        # Consider maximizing general profit,
        #   but simultaneously, consider bonus profit by modulating the elements 

        # 1. select the items solely based on general profit first.
        # 2. remove lowest profit from duplicated group
        items.sort(reverse = True)
        selected, candidate2select = items[:k], items[k:]
        candidate2delete = []
        category = set()
        for p, c in selected:
            if c in category:
                candidate2delete.append((p, c)) # store other following items
            category.add(c)
        

        # calculate current elegance
        elegance = sum([x[0] for x in selected]) + len(category)**2
        output = elegance

        diversity = len(category)

        while candidate2select and candidate2delete:
            sp, sc = candidate2select.pop(0) # select the largest from pool
            if sc in category: continue # duplicated category -> skip
            
            dp, dc = candidate2delete.pop() # delete the smallest from selected
            category.add(sc)
            elegance = elegance - (len(category)-1)**2 + len(category)**2 - dp + sp 
            output = max(output, elegance)
        return output



            


        

