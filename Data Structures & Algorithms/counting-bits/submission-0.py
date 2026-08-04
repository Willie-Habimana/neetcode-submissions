class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            res = 0
            while i:
                res += 1
                i = i & (i-1)
        
            ans.append(res)
        
        return ans
                
        