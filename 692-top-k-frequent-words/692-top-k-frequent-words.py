class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter, defaultdict
        counter = Counter(words)
        ### sorted(counter, key=lambda x:counter[x])
        
        dd = defaultdict(list)
        for word, cnt in counter.items():
            dd[cnt].append(word)
        
        dd = {k:dd[k] for k in sorted(dd, key=lambda cnt:-cnt)}
        total, output = 0, []
        for cnt in dd:
            wordlist = dd[cnt]
            wordlist.sort()
            output += wordlist 
            total += len(wordlist)
            if total >= k: 
                break 
        return output[:k]