# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        q = deque([root])
        curr_level = []
        count = 1
        while q:
            node = q.popleft()
            curr_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            
            count -= 1
            if count == 0:
                count = len(q)
                ans.append(curr_level)
                curr_level = []
        
        return ans

        