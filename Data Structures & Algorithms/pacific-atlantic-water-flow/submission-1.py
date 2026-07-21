class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = set()
        directions = [(1,0), (-1,0), (0,-1), (0,1)]

        def bfs(queue):
            q = queue
            reachable = set()
            while q:
                curr = q.popleft()
                height = -math.inf if curr not in reachable else heights[curr[0]][curr[1]]
                for d in directions:
                    r = curr[0] + d[0]
                    c = curr[1] + d[1]
                    if (r >= 0 and c >= 0 and r < len(heights) and c < len(heights[0])
                        and (r,c) not in reachable and heights[r][c] >= height ):
                        reachable.add((r,c))
                        q.append((r,c))
            
            return reachable
            

        pacific = deque()
        atlantic = deque()

        for i in range(len(heights)):
            pacific.append((i, -1))
            atlantic.append((i, len(heights[0])))
        for i in range(len(heights[0])):
            pacific.append((-1, i))
            atlantic.append((len(heights), i))

        p = bfs(pacific)
        a = bfs(atlantic)

        combined = p.intersection(a)

        return [[i,j] for (i,j) in combined]
        


            


      