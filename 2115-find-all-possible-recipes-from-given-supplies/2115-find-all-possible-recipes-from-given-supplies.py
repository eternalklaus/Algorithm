class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # find out initial leaf 
        '''
        prereq          next 
        yeast, flour -> bred
        bread, meat  -> sandwich 
        '''
        firstnext = defaultdict(set)
        nextfirst = defaultdict(set)
        supplies, output = set(supplies), set()
        
        # Build relationship graph
        for i, next in enumerate(recipes):
            for first in ingredients[i]:
                if first not in supplies: ###!!! 
                    firstnext[first].add(next)
                    nextfirst[next].add(first)
        
        # Set initial leaves
        leaves = []
        for next in recipes:
            if len(nextfirst[next]) == 0:
                leaves.append(next)
        
        # Drop leaf one by one 
        while leaves:
            leaf = leaves.pop()
            output.add(leaf)
            
            for next in firstnext[leaf]:
                nextfirst[next].remove(leaf) # remove leaf from To-prerequisite list...
                if len(nextfirst[next]) == 0:
                    leaves.append(next)
        return output 
            
                
                
                