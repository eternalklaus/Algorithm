class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mailowner, root = {}, [idx for idx in range(len(accounts))]
        def find(idx):
            if root[idx] != idx:
                root[idx] = find(root[idx]) # path compression 
            return root[idx]
        
        def union(idx1, idx2):
            r1, r2 = find(idx1), find(idx2)
            r1, r2 = min(r1, r2), max(r1, r2)
            root[r2] = r1 
            
        # 1. draw graph (only graph! nothing else!)
        for idx, account in enumerate(accounts):
            _, mails = account[0], account[1:]
            for mail in mails:
                if mail in mailowner: # already registered mail -> then union it
                    idx1, idx2 = idx, mailowner[mail]
                    union(idx1, idx2) 
                else: # first appeared in the graph -> then register it
                    mailowner[mail] = idx 
        
        output = defaultdict(list)
        # 2. translate mailowner -> output
        for mail, idx in mailowner.items():
            output[find(idx)].append(mail)
        
        # 3. return output 
        for idx, mails in output.items():
            mails.sort()
            mails.insert(0, accounts[idx][0]) # insert name 
        return output.values()
        