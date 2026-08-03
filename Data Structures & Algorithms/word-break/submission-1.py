class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = [None]*(len(s)+1)
        def dp(start):
            if start == len(s):
                return True
            
            for i in range(start+1, len(s) + 1):
                word = s[start:i]
                if memo[i] == None: 
                    memo[i] = dp(i)
                if word in wordSet and memo[i]:
                    return True
            
            return False
    
        return dp(0)
                    
                    
            
                
       
            
        