# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root, -math.inf)
        return self.ans



    def helper(self, root: TreeNode, max_val: int) -> None:
        if root == None:
            return
        if root.val >= max_val:
            max_val = root.val
            self.ans += 1

        left = self.helper(root.left, max_val) 
        right = self.helper(root.right, max_val)

        return
            
        