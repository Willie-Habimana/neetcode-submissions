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
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        i = 0
        p = 1
        seen = set()
        while i < len(inorder) and preorder[0] != inorder[i]:
            seen.add(inorder[i])
            i += 1
        while p < len(preorder) and preorder[p] in seen:
            p += 1
        root.left = self.buildTree(preorder[1:p], inorder[:i])
        root.right = self.buildTree(preorder[p:], inorder[i+1:])

        return root

 






















        
