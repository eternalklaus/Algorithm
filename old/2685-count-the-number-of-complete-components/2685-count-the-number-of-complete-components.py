class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # 내가 생각하던 알고리즘에 문제가 있음을 깨달았다. 
        # 거바 여기서도 한바쿠 돌자너~ https://chiefcoder.tistory.com/55
        
        # union find
        roots = [i for i in range(n)]
        
        def find(i):
            if roots[i] == i: 
                return i
            output = find(roots[i])
            roots[i] = output
            return output
        
        def union(i, j):
            iroot, jroot = find(i), find(j)
            iroot, jroot = min(iroot,jroot), max(iroot,jroot)
            roots[jroot] = iroot
            find(i), find(j) # 싸악- 업데이트
        
        for i, j in edges:
            union(i, j)
        
        ### 이거 꼭 해줘야 함!!!
        for i in range(n):
            find(i)
        
        # grouping
        group = defaultdict(list)
        for i, root in enumerate(roots):
            group[root].append(i)
        
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        output = 0
        for root, member in group.items():
            if all([len(graph[m])==len(member)-1 for m in member]):
                output += 1
        return output
            