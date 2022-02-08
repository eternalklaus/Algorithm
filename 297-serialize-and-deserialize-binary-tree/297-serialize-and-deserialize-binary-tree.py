# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root) -> str:
        # left to right bfs, None node = # 
        queue, output = [root], ''
        while queue: 
            queuesize = len(queue)

            for i in range(queuesize): # loop in this cycle only
                node = queue.pop(0) 
                if not node: 
                    output += '|#'
                else:
                    output += f'|{node.val}'
                    queue.append(node.left)
                    queue.append(node.right)
        # print (output)
        return output

    def deserialize(self, data) -> TreeNode:
        def createnode(valstr):
            if valstr == '#':
                return None 
            return TreeNode(int(valstr))

        vallist = data.split('|')[1:]
        valstr = vallist.pop(0)
        root = createnode(valstr)
        prevlevel = [root]

        while vallist:
            prevlevel_size = len(prevlevel)
            for _ in range(prevlevel_size):
                prevnode = prevlevel.pop(0)
                prevnode.left = createnode(vallist.pop(0))
                prevnode.right = createnode(vallist.pop(0))

                if prevnode.left: 
                    prevlevel.append(prevnode.left)
                if prevnode.right: 
                    prevlevel.append(prevnode.right)
        return root
