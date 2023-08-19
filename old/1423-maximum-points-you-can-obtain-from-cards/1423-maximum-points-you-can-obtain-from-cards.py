class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)
        
        L = len(cardPoints)
        
        lpivot, rpivot = k - 1, L
        total = sum(cardPoints[:k])
        output = total 
        while lpivot >= 0:
            total -= cardPoints[lpivot]
            lpivot -= 1
            rpivot -= 1
            total += cardPoints[rpivot]
            
            output = max(output, total)
        return output 