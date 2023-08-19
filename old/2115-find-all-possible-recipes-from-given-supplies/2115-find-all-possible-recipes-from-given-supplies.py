class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        srcdst = defaultdict(list)
        dstsrc = defaultdict(list)
        for dst, srcs in zip(recipes, ingredients):
            # if dst in supplies: continue ###no
            for src in srcs:
                if src in supplies: continue # don't take count into
                srcdst[src].append(dst)
                dstsrc[dst].append(src) 
        
        # Get initial leaves
        leaves = []
        for dst in recipes:
            if not dstsrc[dst]: 
                leaves.append(dst)
        print (leaves)
        # Topological sort 
        output = []
        while leaves:
            src = leaves.pop(0) # leaf becomes another source 
            output.append(src)
            dsts = srcdst[src]
            # Check if this dst became leaf 
            for dst in dsts: 
                dstsrc[dst].remove(src) # remove dependency 
                if not dstsrc[dst]: 
                    leaves.append(dst)
        return output 
            