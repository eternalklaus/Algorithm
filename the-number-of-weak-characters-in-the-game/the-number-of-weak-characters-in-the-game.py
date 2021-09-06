class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        properties.sort(key=lambda x:(-x[0], x[1]))
        maxd, count = 0, 0
        for (a, d) in properties:
            if d < maxd:
                count += 1
            else:
                maxd = d
        return count