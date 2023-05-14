class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = defaultdict(list)
        groupking = [i for i in range(n)]
        
        def union(i, j):
            # root를 찾기 위한 find
            root = min(find(i), find(j))
            groupking[i] = root
            groupking[j] = root
            # 업데이트 싸악-을 위한 find
            find(i), find(j)
        
        def find(i):
            if groupking[i] == i:
                return i
            root = find(groupking[i])
            # 여기서 찾아주면서 싸악- 새 신을 섬기는거지
            groupking[i] = root
            return root
        
        # union-find
        for i, j in edges:
            connected[i].append(j)
            connected[j].append(i)
            connected[i].append(i)
            union(i, j)
        
        def identical(a, b):
            if set(a) == set(b): return True
            return False
        
        
        # check whether among all connected nodes has connection with each other
        groups = defaultdict(list)
        for i in range(n):
            groups[groupking[i]].append(i)
        
        output = 0
        for groupking, members in groups.items():
            members.sort()
            is_thisgroup_perfact = 1
            for i in members:
                # _ = connected[i] + [i] # 왜 이렇게하니까 connected가 바뀌는거같지...?
                
                if identical(members, connected[i] + [i]):
                    continue
                else: 
                    is_thisgroup_perfact = 0
            output += is_thisgroup_perfact
        return output
            