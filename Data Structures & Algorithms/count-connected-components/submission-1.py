class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = set()
        ans = 0

        def dfs(source):
            stack = [source]
            while stack:
                node = stack.pop()
                visited.add(node)
                for nei in adj[node]:
                    if nei not in visited:
                        stack.append(nei)

        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
        
        return ans


        