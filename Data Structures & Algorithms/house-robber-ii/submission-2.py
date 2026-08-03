class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dp(i, first = None):
            if i == len(nums) - 1:
                if first:
                    return 0
                return nums[i]
            if i == len(nums) - 2:
                if first:
                    return nums[i]
                return max(nums[i], nums[i+1])
            if (i, first) in memo:
                return memo[(i, first)]
            if i == 0:
                first = True
            take = dp(i+2, first) + nums[i]
            if i == 0:
                first = False
            leave = dp(i+1, first)
            memo[(i, first)] = max(take, leave)
            return memo[(i, first)]
        
        return dp(0)
        
        