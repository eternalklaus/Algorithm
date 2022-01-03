class Solution:
    def alienOrder(self, words: List[str]) -> str:
        in_degree = Counter({c : 0 for word in words for c in word})
        adj_list = defaultdict(set)
        
        for first_word, second_word in zip(words, words[1:]): ### <= zip! 
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""
    
        # ok understood so far
        output = []
        queue = [c for c in in_degree if in_degree[c] == 0]
        while queue:
            c = queue.pop(0)
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0: # leaf
                    queue.append(d)
                    
        if len(output) < len(in_degree): # circle exist 
            return ''
        return "".join(output)