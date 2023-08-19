class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # inclusive queries
        vowel = {'a', 'e', 'i', 'o', 'u'}
        for idx, word in enumerate(words):
            if words[idx][0] in vowel and words[idx][-1] in vowel:
                words[idx] = 1
            else:
                words[idx] = 0
        
        accum = [0 for _ in range(len(words))]
        accum[0] = words[0]
        
        for idx, val in enumerate(words[1:], 1):
            accum[idx] += (accum[idx-1] + val)
        
        output = []
        for i, j in queries:
            if i == 0:
                output.append(accum[j])
            else:
                output.append(accum[j] - accum[i-1])
        return output