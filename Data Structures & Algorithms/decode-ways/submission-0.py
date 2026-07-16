class Solution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.ans = 0
        self.cache = {}
        if s[0] == '0':
            return 0

        return self.dp(0)
        
    def dp(self, i):
        if i >= len(self.s):
            return 1

        if self.s[i] == '0':
            return 0
        
        if i == len(self.s) - 1:
            return 1


        if i in self.cache:
            return self.cache[i]
        
        
        
        one = self.dp(i+1)
        two = self.dp(i+2) if ((self.s[i] == '1' and ord('0') <= ord(self.s[i+1]) <= ord('9')) or 
                                self.s[i] == '2' and ord('0') <= ord(self.s[i+1]) <= ord('6')) else 0
        
        self.cache[i] = one + two
        return self.cache[i]
        
        