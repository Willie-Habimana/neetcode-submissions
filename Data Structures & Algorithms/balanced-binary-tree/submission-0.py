# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.helper(root)
        return self.ans




    def helper(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left_height = self.helper(root.left)
        right_height = self.helper(root.right)

        if abs(right_height - left_height) > 1:
            self.ans = False
        
        return max(left_height, right_height) + 1




        