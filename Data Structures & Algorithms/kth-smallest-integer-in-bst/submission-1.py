# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.k = k
        self.ans = None
        self.inorder(root)
        return self.ans
    
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        self.count += 1
        if self.count == self.k:
            self.ans = root.val
            return
        self.inorder(root.right)

            

        
