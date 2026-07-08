# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



'''
preorder
---------
Know: 
- What the root is

Don't Know: 
 - From root, we don't know if the children are right or left 


inorder
--------
Know: 
- What is the left most node
- Given a node, we know what nodes are apart of left sub-tree and right-tree

Don't Know:
- Don't know what is the root vs. what is in the right sub-tree



together
--------
- Can find the root using preorder
- from root, can know which nodes are left vs right using the inorder list

'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        if len(inorder) == 1:
            return root 

        i = 0
        while inorder[i] != preorder[0]:
            i += 1
        
        left_subtree = self.buildTree(preorder[1:i+1], inorder[:i]) if i > 0 else None  
        right_subtree = self.buildTree(preorder[i+1:], inorder[i+1:]) if i+1 < len(inorder) else None

        root.left = left_subtree
        root.right = right_subtree

        return root 
