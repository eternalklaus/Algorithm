class Leaderboard:

    def __init__(self):
        self.scores = {-1:0}
        self.rank = [-1] # top player list 

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] += score 
        else:
            self.scores[playerId] = score 
        
        # insertion sort would be the best (decreasing order)
        if playerId in self.rank: # remove original ranking information
            self.rank.remove(playerId) 
        for i, p in enumerate(self.rank):
            if self.scores[playerId] > self.scores[p]: # i an the stronger one.
                self.rank.insert(i, playerId)
                break 

    def top(self, K: int) -> int:
        output = 0
        for p in self.rank:
            if K: 
                output += self.scores[p]
                K -= 1
            else: 
                break
        return output

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
        self.rank.remove(playerId)
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)