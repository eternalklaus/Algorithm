class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.locations = []
        def moveone(startloc):
            (i, j) = startloc 
            if i==-1 and j==-1:
                return (0, 0)
            if i == n-1 and j == n-1:
                return False 
            if j == n-1:
                return (i+1, 0)
            else:
                return (i, j+1)
            
        def getattackloc(i, j):
            attackloc = []
            # | 
            for k in range(n):
                attackloc.append((k, j))
            # -
            for k in range(n):
                attackloc.append((i, k))
            # /
            for k in range(n):
                if i+k>=n or j+k>=n: break
                attackloc.append((i+k, j+k))
            for k in range(n):
                if i-k<0 or j-k<0: break
                attackloc.append((i-k, j-k))
            # \
            for k in range(n):
                if i+k>=n or j-k<0: break
                attackloc.append((i+k, j-k))
            for k in range(n):
                if i-k<0 or j+k>=n: break
                attackloc.append((i-k, j+k))
            return attackloc
            
        def picknewloc(location, avoidloc):
            newloc = moveone(avoidloc)
            while newloc:
                (newi, newj) = newloc
                attackloc = getattackloc(newi, newj)
                for al in attackloc: # [] and () confusion. set type identically!
                    if al in location:
                        break
                
                else: # survived from for loop
                    return newloc
                
                avoidloc = newloc
                newloc = moveone(avoidloc)

            return False

        def backtrack(location, avoidloc):
            if len(location) == n:
                self.locations.append(location)
                return 
            else:
                while True:
                    loc = picknewloc(location, avoidloc) # excluding loc. <= remember point!
                    if loc == False and len(location) == 0: # at first input, impossible avoidloc is granted
                        break
                    elif loc == False:
                        avoid2 = location.pop()
                        backtrack(location, avoid2)            
                    elif loc:
                        location2 = location.copy() # <= remember point!
                        location2.append(loc)
                        backtrack(location2, loc)
                    
                    avoidloc = moveone(avoidloc)
                    if avoidloc == False: break
        
        def formatting(locations):
            retlists = []
            for location in locations:
                retlist = []
                for i in range(n):
                    row = ""
                    for j in range(n):
                        if (i, j) in location:
                            row += 'Q'
                        else:
                            row += '.'
                    retlist.append(row)
                retlists.append(retlist)

            return retlists

        backtrack([], (-1,-1))

        removedupliacte()
        # return self.locations # if first starting point is [0,2], starting point [-1,-1] [0,0] [0,1] returns duplicated list..hmm..
        return formatting(self.locations)