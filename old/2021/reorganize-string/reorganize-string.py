class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        counter, output = Counter(s), '0'
        
        while counter:
            elders = sorted(counter.keys(), key=lambda x:-counter[x])
            # print (elders)
            if len(elders) == 1: # last case 
                elder1 = elders[0]
                elder2 = ''
                counter[elder1] -= 1
                if counter[elder1] == 0: del counter[elder1]
                
            else: # left more then 2
                elder1 = elders[0]
                elder2 = elders[1]
                counter[elder1] -= 1
                counter[elder2] -= 1
                if counter[elder1] == 0: del counter[elder1]
                if counter[elder2] == 0: del counter[elder2]
            
            if output[-1] == elder1:
                return ''
            else:
                output = output + elder1 + elder2
        
        return output[1:]