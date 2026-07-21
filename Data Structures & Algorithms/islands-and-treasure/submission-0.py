class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        sources = []
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    sources.append((i,j))
        
        q = deque(sources)
        visited = set(sources)
        distance = 1
        size = len(q)
        while q:
            curr = q.popleft()
            for d in directions:
                r = curr[0] + d[0]
                c = curr[1] + d[1]
                if (r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])
                    and (r,c) not in visited and grid[r][c] > 0):
                    grid[r][c] = min(distance, grid[r][c])
                    visited.add((r,c))
                    q.append((r,c))
            size -=1 
            if size == 0:
                distance += 1
                size = len(q)
        
        





        
        