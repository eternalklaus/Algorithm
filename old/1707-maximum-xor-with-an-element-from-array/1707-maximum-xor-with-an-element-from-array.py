import math

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        maxdepth = int(math.log2(10**9) + 1)  # Maximum bit length
        bits = [1 << i for i in range(maxdepth, -1, -1)]
        queryorder = [i for i in range(len(queries))]
        queryorder.sort(key = lambda x:queries[x][1]) #
        nums.sort() #

        class Trie:
            def __init__(self):
                self.children = {}

            def addNodeAndMove(self, value):
                if value not in self.children:
                    self.children[value] = Trie()
                return self.children[value]

            def move(self, value):
                if value not in self.children:
                    value = 1 - value # 차선책 이동.. m보다 크지 않은진 고려하지 않아도 됨!
                return value, self.children[value]

        def query(x, root):
            if not root.children: # m보다 작은 num의 트라이가 구축되지 않은 상태
                return -1
            
            num, node = 0, root
            for bit in bits:
                if bit & x == bit: # 0으로 이동하는게 유리함 
                    bitvalue, node = node.move(0)
                else:
                    bitvalue, node = node.move(1)
                num += bit * bitvalue
            return num


        def buildTrie(num, root):
            node = root
            for bit in bits:
                if bit & num: 
                    node = node.addNodeAndMove(1)
                else:
                    node = node.addNodeAndMove(0)

        output, root = [], Trie()
        output = [-1] * len(queries)
        for qi in queryorder:
            x, m = queries[qi]
            while nums and nums[0] <= m: ### m 이하인 것들 트라이 구축. 천재적이다 세상엔 천재가 많다 
                num = nums.pop(0)
                buildTrie(num, root)
            
            result = query(x, root)
            output[qi] = result ^ x if result != -1 else -1
        
        return output
