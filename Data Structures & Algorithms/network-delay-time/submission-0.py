class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        dist = {node: math.inf for node in range(1, n+1)}

        def dfs(node, time):
            if time >= dist[node]:
                return
            

            dist[node] = time
            for nei in adj[node]:
                dfs(nei[0], time + nei[1])
        
        dfs(k, 0)
        ans = max(dist.values())
        return ans if ans < math.inf else -1

        