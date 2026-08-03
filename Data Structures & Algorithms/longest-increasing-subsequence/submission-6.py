class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1 for _ in range(len(nums))]

        def dp(start):
            if start == len(nums) - 1:
                memo[start] = 1
                return 1

            if memo[start] != -1:
                return memo[start]


            ret = 1
            for i in range(start+1, len(nums)):
                if nums[i] > nums[start]:
                    ret = max(ret, dp(i) + 1)

            memo[start] = ret
            return memo[start]
        
        for i in range(len(nums)):
            dp(i)
        
        return max(memo)

        
                

        