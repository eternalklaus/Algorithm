class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        counter = Counter(words)
        return sorted(counter, key=lambda x: (-counter[x],x))[:k] # sort by counter, sort by word