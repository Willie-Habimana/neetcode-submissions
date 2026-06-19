# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.depth(root)
        return self.ans
        

    def depth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        diameter = left_depth + right_depth

        self.ans = max(self.ans, diameter)

        return max(left_depth, right_depth) + 1
        


        