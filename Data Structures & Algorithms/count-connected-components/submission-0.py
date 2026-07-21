class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        count = 0

        def dfs(i, parent):
            seen.add(i)
            for nei in adj[i]:
                if nei == parent:
                    continue
                if nei not in seen:
                    dfs(nei, i)


        for i in range(n):
            if i not in seen:
                dfs(i, None)
                count += 1
        
        return count
        