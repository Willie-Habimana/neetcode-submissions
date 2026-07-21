class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(len(edges) + 1)]
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        
        



        def redundant():
            stack = [1]
            seen = set()
            while stack:
                node = stack.pop()
                seen.add(node)
                for nei in adj[node]:
                    if nei not in seen:
                        stack.append(nei)

            return True if len(seen) == len(edges) else False 

        ans = None
        for edge in edges:
            adj[edge[0]].remove(edge[1])
            adj[edge[1]].remove(edge[0])
            if redundant():
                ans = edge
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])

        return ans              