# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        stack = [root]

        while stack:
            node = stack.pop()
            if len(heap) < k:
                heapq.heappush(heap, -node.val)
            else:
                heapq.heappushpop(heap, -node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return -heap[0]


        