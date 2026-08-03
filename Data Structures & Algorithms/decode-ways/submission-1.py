class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [None for _ in range(len(s))]

        def dp(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s) - 1:
                return 1
            if memo[i]:
                return memo[i]

            memo[i] = dp(i+1)
            if s[i] == '1':
                memo[i] += dp(i+2)
            if i + 1 < len(s) and s[i] == '2' and int(s[i+1]) <= 6:
                memo[i] += dp(i+2)
            
            return memo[i]
        
        return dp(0)










        