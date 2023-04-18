class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        G = defaultdict(list)
        L = len(vals)
        
        for a,b in edges:
            # value=3 인 노드에는 value가 1,2인 노드들만 연결되었다고 저장할수있다
            if vals[a] < vals[b]:
                a,b = b,a
            G[a].append(b)
         
        V = defaultdict(list) # value - indexes
        for i, val in enumerate(vals):
            V[val].append(i)
        
        parent = [i for i in range(L)]
        def connect(G, idx):
            for idx2 in G[idx]:
                p1, p2 = find(idx), find(idx2)
                p1, p2 = min(p1, p2), max(p1, p2)
                parent[p2] = p1
                find(idx)
                find(idx2)
        
        def find(idx):
            if parent[idx] == idx: return idx
            return find(parent[idx])
        
        V = dict(sorted(V.items()))
        # print (V)
        
        output = 0
        for val, indice in V.items():
            # 같은 루트가 나오는지 체크를 해서, 
            # idx1, idx2 가 같은 루트라면, 그 카운터를 더해주는거지
            family = Counter()
            # print (val, indice)
            
            for idx in indice:
                connect(G, idx)
                p = parent[idx]
                family[p] += 1
            # print (family)
            
            for p in family:
                pp = find(p)
                if pp != p: # p가 최종 parent가 아니라면, 
                    family[pp] += family[p]
                    family[p] = 0
            
            for p, cnt in family.items():
                if cnt <= 1: continue 
                output += (cnt) * (cnt - 1) // 2
        return output + len(vals)