class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [None for _ in range(len(nums))]

        def dp(i):
            if i >= len(nums) - 1:
                return True
            if memo[i] != None:
                return memo[i]

            for j in range(nums[i], 0, -1):
                if dp(i+j):
                    memo[i] = True
                    return True
            
            memo[i] = False
            return False
        
        return dp(0)

            

            



        