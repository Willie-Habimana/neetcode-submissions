# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, math.inf, -math.inf)

    def helper(self, root: Optional[TreeNode], max_val: int, min_val: int) -> bool:
        if root == None:
            return True
        
        if root.val >= max_val or root.val <= min_val:
            return False
        
        if not self.helper(root.left, min(root.val, max_val), min_val):
            return False
        if not self.helper(root.right, max_val, max(root.val, min_val)):
            return False
        
        return True


        
        
            


        