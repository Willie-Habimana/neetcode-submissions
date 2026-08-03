class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None for _ in range(len(s))]
        wordSet = set(wordDict)

        def dp(i):
            if i >= len(s):
                return True
            if memo[i] != None:
                return memo[i]
            end = i + 1

            while end <= len(s):
                if s[i:end] in wordSet:
                    if dp(end):
                        memo[i] = True
                        return True
                end += 1
            memo[i] = False
            return False

        

        return dp(0)
            
        