class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        cache = {}

        def dp(i):
            if i == len(nums) - 1:
                return 1
            if i in cache:
                return cache[i]

            ret = 1
            for j in range(i+1, len(nums)):
                length = dp(j)
                if nums[i] < nums[j]:
                    ret = max(ret, length+1)
            cache[i] = ret
            return ret
        

        dp(0)

        return max(cache.values())



                
        