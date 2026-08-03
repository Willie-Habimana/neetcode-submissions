class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [None for _ in range(len(nums))]

        def dp(i):
            if i == len(nums) - 1:
                return nums[i]
            if i == len(nums) - 2:
                return max(nums[i], nums[i+1])
            if memo[i]:
                return memo[i]
            
            memo[i] = max(dp(i+2) + nums[i], dp(i+1))

            return memo[i]
        
        return dp(0)
            

        