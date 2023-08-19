class Leaderboard:
    from collections import Counter 
    def __init__(self):
        self.score = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.score[playerId] += score 

    def top(self, K: int) -> int:
        return sum([x for (_, x) in self.score.most_common(K)])

    def reset(self, playerId: int) -> None:
        self.score[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)