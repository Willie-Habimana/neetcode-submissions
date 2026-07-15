class Solution:
    def rob(self, nums: List[int]) -> int:
        self.first = False
        self.nums = nums
        self.cache = {}

        return self.dp(0)

    def dp(self, i):
        if i >= len(self.nums):
            return 0
        
        if i == len(self.nums) - 1:
            if self.first:
                return 0
            else:
                return self.nums[-1]
        
        if (i, self.first) in self.cache:
            return self.cache[(i, self.first)]
        
        skip = self.dp(i+1)
        if i == 0:
            self.first = True
        take = self.dp(i+2) + self.nums[i]
        if i == 0:
            self.first = False
        self.cache[(i, self.first)] = max(skip, take)
        return self.cache[(i, self.first)]





        