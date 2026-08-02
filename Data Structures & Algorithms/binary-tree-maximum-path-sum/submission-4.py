# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -math.inf
        self.helper(root)
        return self.ans




    def helper(self, root):
        if root == None:
            return -math.inf
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        self.ans = max(self.ans, left, right, left + right + root.val, root.val, root.val + left, root.val + right)

        return max(left, right, 0) + root.val


        