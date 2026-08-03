class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def dp(c1, c2):
            if c1 == len(text1) or c2 == len(text2):
                return 0 
            if memo[c1][c2] != -1:
                return memo[c1][c2]

            res = 0
            if text1[c1] == text2[c2]:
                res = dp(c1 + 1, c2 + 1) + 1
            else:
                res = max(dp(c1+1,c2), dp(c1,c2+1))
            
            memo[c1][c2] = res
            return res
        
        return dp(0,0)


        