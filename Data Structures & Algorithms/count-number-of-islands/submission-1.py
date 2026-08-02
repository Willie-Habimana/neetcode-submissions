class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        ans = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(i,j):
            seen.add((i,j))
            for d in directions:
                r = i + d[0]
                c = j + d[1]
                if ((r >= 0 and c >=0 and r < len(grid) and c < len(grid[0]))
                     and (r,c) not in seen and grid[r][c] == '1'):
                     dfs(r,c)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in seen:
                    dfs(i,j)
                    ans += 1
        
        return ans
                

