class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        from collections import defaultdict

        if len(sentence1) != len(sentence2): return False
        pairs = defaultdict(set)
        for w1, w2 in similarPairs:
            pairs[w1].add(w2)
            pairs[w2].add(w1)
        
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2 or w1 in pairs[w2]:
                continue 
            return False
        return True
