class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        stack = [0]
        seen = set([0])
        while stack:
            node = stack.pop()
            seen.add(node)
            for nex in graph[node]:
                if nex not in seen:
                    stack.append(nex)
        

        return True if len(seen) == n else False
        