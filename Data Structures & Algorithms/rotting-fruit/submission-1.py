class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        sources = []
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    sources.append((i,j))
        
        q = deque(sources)
        visited = set(sources)
        rotten = len(q)
        minute = 0
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        while q:
            curr = q.popleft()
            for d in directions:
                r = curr[0] + d[0]
                c = curr[1] + d[1]
                if (r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) 
                    and (r,c) not in visited and grid[r][c] == 1):
                    visited.add((r,c))
                    q.append((r,c))
            rotten -= 1
            if rotten == 0:
                rotten = len(q)
                if rotten > 0:
                    minute += 1
        
        
        return minute if len(visited) == total else -1

            


        