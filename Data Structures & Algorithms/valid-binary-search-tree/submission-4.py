# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left = self.helper(root.left, root.val, -math.inf)
        right = self.helper(root.right, math.inf, root.val)
        return left and right 
    



    def helper(self, root, maximum, minimum):
        if root == None:
            return True
        
        if root.val >= maximum or root.val <= minimum:
            return False
        
        left = self.helper(root.left, min(maximum, root.val), minimum)
        right = self.helper(root.right, maximum, max(minimum, root.val))

        return left and right

        
        




        
        
            


        