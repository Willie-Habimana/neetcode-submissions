# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1

        q = deque()
        q.append(root) 
        depth = 0
        count = 1
        while q:
            node = q.popleft()
            count -= 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if count == 0:
                depth += 1
                count = len(q)
            
        return depth
            

            

        