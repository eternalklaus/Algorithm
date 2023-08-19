class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skillGraph = defaultdict(set)
        N = len(req_skills)
        for idx, skills in enumerate(people):
            for skill in skills:
                skillGraph[skill].add(idx)
        
        ans = list(range(N+1)) ### <- default list
        
        def DFS(peopleSet, k): # compare k-st required skill
            nonlocal ans
            if k == N: # finished skill searching
                if len(ans) > len(peopleSet):
                    ans = list(peopleSet)
                return
            if len(peopleSet) >= len(ans): ### <- if not end but size overed, cut it
                return
            
            skillers = skillGraph[req_skills[k]]
            for p in peopleSet:    
                if p in skillers: #if the people has that skill
                    DFS(peopleSet, k+1)
                    return
            for p in skillers:
                peopleSet.add(p)
                DFS(peopleSet, k+1)
                peopleSet.remove(p)
            
        DFS(set(), 0)
        return ans