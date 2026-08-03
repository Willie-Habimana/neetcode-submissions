class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        def dp(i,j):
            if i == m - 1 and j == n - 1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            
            ways = 0
            if i < m - 1:
                ways += dp(i+1,j)
            if j < n - 1:
                ways += dp(i, j+1)
            
            memo[i][j] = ways
            return ways
        
        return dp(0,0)
            
        