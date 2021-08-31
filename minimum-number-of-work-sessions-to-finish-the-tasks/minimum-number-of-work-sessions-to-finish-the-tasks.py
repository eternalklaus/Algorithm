class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        session = [] # save time in here
        mintotal = float('inf')
        def dfs(idx):
            nonlocal session, mintotal
            if idx == len(tasks):
                mintotal = min(mintotal, len(session))
                return
            
            # add optimization 
            if len(session) > mintotal:
                return 

            # 1) try add on existing bins
            for i, time in enumerate(session):
                 if session[i] + tasks[idx] <= sessionTime: # if tasks[idx] is packable
                        session[i] += tasks[idx] # pack
                        dfs(idx+1)
                        session[i] -= tasks[idx] # unpack
            
            # 2) add standalone bin
            session.append(tasks[idx])
            dfs(idx+1)
            session.pop()
        
        dfs(0)
        return mintotal
            