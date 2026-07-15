class Solution:
    def rob(self, nums: List[int]) -> int:
        self.cache = {}
        self.nums = nums
        return max(self.dp(0), self.dp(1))



    def dp(self, i):
        if i >= len(self.nums):
            return 0
        
        if i in self.cache:
            return self.cache[i]
        
        skip_one = self.dp(i+2)
        skip_two = self.dp(i+3)

        self.cache[i] = max(skip_one, skip_two) + self.nums[i]

        return self.cache[i]

        



        