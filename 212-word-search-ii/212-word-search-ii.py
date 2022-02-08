class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

    def addWord(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        DIR = [0, 1, 0, -1, 0]
        trieNode = TrieNode()
        ans = []
        for word in words:
            trieNode.addWord(word)

        def dfs(r, c, cur):
            if r < 0 or r == m or c < 0 or c == n or board[r][c] not in cur.children: return
            orgChar = board[r][c]
            cur = cur.children[orgChar]
            board[r][c] = '#'  # Mark as visited
            if cur.word != None:
                ans.append(cur.word)
                cur.word = None  # Avoid duplication!
            for i in range(4): dfs(r + DIR[i], c + DIR[i + 1], cur)
            board[r][c] = orgChar  # Restore to org state

        for r in range(m):
            for c in range(n):
                dfs(r, c, trieNode)
        return ans