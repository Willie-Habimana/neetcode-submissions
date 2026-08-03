class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None for i in range(n+1)]
        def dp(i):
            if i == 1:
                return 1
            if i == 2:
                return 2
            if memo[i]:
                return memo[i]
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        
        return dp(n)

        