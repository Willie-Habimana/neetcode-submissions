"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        og_to_copy = {}
        stack = [node]
        seen = set([node])
        while stack:
            og = stack.pop()
            for nei in og.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)
            og_to_copy[og] = Node(og.val)
        
        stack = [node]
        seen = set([node])
        while stack:
            og = stack.pop()
            for nei in og.neighbors:
                og_to_copy[og].neighbors.append(og_to_copy[nei])
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)

        return og_to_copy[node]
        
            

        


        