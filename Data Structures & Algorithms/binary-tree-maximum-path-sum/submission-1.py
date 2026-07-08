# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        self.maxPath(root)
        return self.ans




    def maxPath(self, root): 
        if root == None:
            return -math.inf
        
        left_max_path = self.maxPath(root.left)
        right_max_path = self.maxPath(root.right)

        self.ans = max(self.ans, root.val + right_max_path + left_max_path, root.val, root.val + left_max_path, root.val + right_max_path, left_max_path, right_max_path)

        return max(root.val, root.val + left_max_path, root.val + right_max_path)
        
        