class Solution:
    def uniqueLetterString(self, s: str) -> int:
        L = len(s)
        cdict = defaultdict(list)
        for i, c in enumerate(s):
            cdict[c].append(i)
        
        # A: ABCD -> A ABC A
        #            -1 0  3
        #          value =
        # B: ABCD -> B ABC B 
        # ...
        # 
        output = 0
        for c in cdict:
            idxlist = cdict[c]
            idxlist.insert(0, -1)
            idxlist.append(L) 

            for idx2 in range(1, len(idxlist)-1):
                idx1 = idx2-1
                idx3 = idx2+1
                # including removing case. if length is 2, multiply 3
                output += (idxlist[idx2]-idxlist[idx1]-1+1) * (idxlist[idx3]-idxlist[idx2]-1+1) 
                
        return output