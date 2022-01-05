class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        for i in range(1, n+1):
            output.append(str(i))
        
        output.sort()
        return map(int, output)
            