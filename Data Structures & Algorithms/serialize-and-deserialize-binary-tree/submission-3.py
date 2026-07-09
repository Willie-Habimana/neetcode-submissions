# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node == None:
                res.append("N")
            else:
                res.append(str(node.val))
                if node.right:
                    stack.append(node.right)
                else:
                    stack.append(None)
                if node.left:
                    stack.append(node.left)
                else:
                    stack.append(None)

        print(",".join(res))  
        return ','.join(res)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        self.ind = 0

        def dfs():
            if arr[self.ind] == "N":
                self.ind+=1
                return None
            node = TreeNode(arr[self.ind])
            self.ind += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()






        
