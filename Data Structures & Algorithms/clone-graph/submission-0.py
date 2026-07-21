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
        clone_map = {}
        stack = [node]
        visited = set()
        clone_map[node] = Node(node.val)
        while stack:
            curr = stack.pop()
            visited.add(curr)
            neighbors = []
            for neighbor in curr.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                if neighbor not in visited:
                    stack.append(neighbor)
                neighbors.append(clone_map[neighbor])
            
            clone_map[curr].neighbors = neighbors
        

        
        return clone_map[node]
            