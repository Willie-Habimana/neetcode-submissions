class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None for _ in range(len(s) + 1)]
        wordSet = set(wordDict)

        def dp(i):
            if i >= len(s):
                return True
            end = i + 1

            while end <= len(s):
                if memo[end] == None:
                    memo[end] = dp(end)
                if s[i:end] in wordSet and memo[end]:
                    return True
                end += 1
            return False

        

        return dp(0)
            
        