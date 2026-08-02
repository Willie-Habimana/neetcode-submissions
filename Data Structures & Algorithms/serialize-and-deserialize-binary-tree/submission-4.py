# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""
        s = ''
        s += str(root.val)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                s += ","
                s += str(node.left.val)
                q.append(node.left)
            else:
                s += ","
                s += "."
            if node.right:
                s += ","
                s += str(node.right.val)
                q.append(node.right)
            else:
                s += ","
                s += "."
        
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        arr = data.split(",")
        q = deque(arr)
        head = TreeNode(q.popleft())
        node_q = deque([head])
        while node_q and q:
            curr = node_q.popleft()
            left = q.popleft()
            right = q.popleft()
            if left != ".":
                curr.left = TreeNode(int(left))
                node_q.append(curr.left)
            if right != ".":
                curr.right = TreeNode(int(right))
                node_q.append(curr.right)
        
        return head
            









        
