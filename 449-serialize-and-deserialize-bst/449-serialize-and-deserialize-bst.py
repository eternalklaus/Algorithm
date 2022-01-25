# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        # we can flatten the nodes thoughtlessly
        output = ''
        
        def dfs(node):
            nonlocal output 
            if not node: return
            # serialize value of node
            output = output + '$' + str(node.val) 
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return output 
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        print (data)
        if not data: return None 
        
        vals = data.split('$')[1:] ###XXX
        vals = list(map(int, vals)) ###XXX
        
        # initialize root
        root = TreeNode(vals[0])
        
        # fill the nodes 
        for val in vals[1:]:
            node = root
            n = TreeNode(val) # create new node
            # fill the n(node) in the right place 
            while True:
                if node.val < val: # move to right
                    if node.right == None: 
                        node.right = n
                        break
                    else:
                        node = node.right 
                        continue 
                else: # move to left 
                    if node.left == None:
                        node.left = n
                        break 
                    else:
                        node = node.left 
                        continue
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans