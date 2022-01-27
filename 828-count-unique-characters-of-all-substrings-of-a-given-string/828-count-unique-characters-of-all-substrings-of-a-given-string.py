class Solution:
    def uniqueLetterString(self, s: str) -> int:
        L = len(s)
        cdict = defaultdict(list)
        for i, c in enumerate(s):
            cdict[c].append(i)
        
        # ABCD -> A ABC A
        # ABCD -> B ABC B 
        # ...
        output = 0
        for c in cdict:
            idxlist = cdict[c]
            idxlist.insert(0, -1)
            idxlist.append(L)
            #print (idxlist)

            for idx2 in range(1, len(idxlist)-1):
                idx1 = idx2-1
                idx3 = idx2+1
                val = (idxlist[idx2]-idxlist[idx1]-1+1) * (idxlist[idx3]-idxlist[idx2]-1+1) # including removing case. if length is 2, multiply 3
                if val > 0:
                    output += val
        return output