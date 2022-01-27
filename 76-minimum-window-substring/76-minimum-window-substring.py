class Solution: #TODO: 이거 토대로 풀이 올리기 
    def minWindow(self, s: str, t: str) -> str:
        
        first, last, L = 0, 0, len(s)
        output = s+'a'
        outputlen = len(output)
        counter = Counter(t)
        toclear = len(counter) ### unique chars to be cleared!
        
        def increase(c):
            nonlocal counter
            if c in counter: ### O(1), if it's comparing with list, O(n) 
                counter[c] += 1
        
        def decrease(c):
            nonlocal counter
            if c in counter: 
                counter[c] -= 1


        if counter[s[0]] == 1: toclear -= 1
        decrease(s[0]) # initialize        

        while True:
            # decrease window with moving [first --> last]
            if toclear == 0:
                # update output 
                if last - first + 1 < outputlen: ### O(1), if last - first + 1< len(output):
                    output = s[first:last+1]
                    outputlen = len(output)
                # move first
                increase(s[first])
                if counter[s[first]] == 1: toclear += 1 # zero -> one increased
                first += 1 
                
            # increase window with moving [first last] -->
            else: 
                last += 1
                if last >= L: break 
                if counter[s[last]] == 1: toclear -= 1 
                decrease(s[last])
                # if counter[s[last]] == 0: toclear -= 1 # 여기다하면 원래 0인놈들과 구분이 안되니 안돼!
        
        if outputlen > len(s):
            return ''
        return output 