class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
        adj = [[] for _ in range(n+1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        q = deque([0])
        visited = set([0])
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return len(visited) == n

        