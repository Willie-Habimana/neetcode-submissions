class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def dp(c1, c2):
            if memo[c1][c2] != -1:
                return memo[c1][c2]
            
            res = 1
            for i in range(c1 + 1, len(text1)):
                for j in range(c2 + 1, len(text2)):
                    if text1[i] == text2[j]:
                        res = max(res, dp(i,j) + 1)
                        break
            
            memo[c1][c2] = res
            return res
        
        res = 0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    res = max(res, dp(i,j))
        
        return res


        